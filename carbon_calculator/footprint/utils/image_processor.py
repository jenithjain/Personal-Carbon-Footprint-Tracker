import cv2
import numpy as np
import pytesseract
from PIL import Image
import io
import base64
import re

class ImageProcessor:
    def __init__(self):
        # Configure pytesseract path if needed
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Common ingredient keywords
        self.ingredient_keywords = [
            'ingredients:', 'contains:', 'ingredients list:',
            'ingredients list', 'ingredients contains'
        ]

    def base64_to_cv2(self, base64_string):
        """Convert base64 image to CV2 format"""
        try:
            # Remove data URL prefix if present
            if ',' in base64_string:
                base64_string = base64_string.split(',')[1]
            
            # Decode base64 string
            img_data = base64.b64decode(base64_string)
            nparr = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is None:
                raise ValueError("Failed to decode image")
                
            return img
            
        except Exception as e:
            raise ValueError(f"Error converting image: {str(e)}")

    def preprocess_image(self, image):
        """Preprocess image for better text detection"""
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Noise removal
        kernel = np.ones((2,2), np.uint8)
        processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        return processed

    def extract_ingredients(self, base64_image):
        """Extract ingredients from image"""
        try:
            # Convert base64 to CV2 image
            image = self.base64_to_cv2(base64_image)
            
            # Mock ingredients for testing
            mock_ingredients = [
                {'name': 'Palm Oil', 'impact': 'high', 'co2': 0.8},
                {'name': 'Sugar', 'impact': 'medium', 'co2': 0.3},
                {'name': 'Wheat Flour', 'impact': 'low', 'co2': 0.2},
                {'name': 'Cocoa', 'impact': 'high', 'co2': 0.7},
                {'name': 'Milk Powder', 'impact': 'high', 'co2': 0.6}
            ]
            
            return {
                "success": True,
                "ingredients": mock_ingredients
            }
            
        except Exception as e:
            return {
                "error": f"Error processing image: {str(e)}"
            }

    def parse_ingredients(self, text):
        """Parse ingredients from text"""
        # Remove common prefixes
        for keyword in self.ingredient_keywords:
            text = text.lower().replace(keyword, '')
        
        # Split by common delimiters
        ingredients = re.split('[,.]', text)
        
        # Clean up ingredients
        cleaned = []
        for ing in ingredients:
            ing = ing.strip()
            if ing and len(ing) > 1:  # Avoid empty or single-char ingredients
                cleaned.append(ing.capitalize())
        
        return cleaned

    def classify_ingredients(self, ingredients):
        """Classify ingredients by environmental impact"""
        # Mock classification - In real implementation, this would use a database or API
        high_impact = ['palm oil', 'beef', 'lamb', 'cheese', 'chocolate']
        medium_impact = ['chicken', 'pork', 'sugar', 'milk', 'cream']
        
        classified = []
        for ing in ingredients:
            ing_lower = ing.lower()
            if any(item in ing_lower for item in high_impact):
                impact = 'high'
                co2 = round(0.8 + np.random.random() * 0.4, 2)
            elif any(item in ing_lower for item in medium_impact):
                impact = 'medium'
                co2 = round(0.3 + np.random.random() * 0.3, 2)
            else:
                impact = 'low'
                co2 = round(0.1 + np.random.random() * 0.2, 2)
            
            classified.append({
                'name': ing,
                'impact': impact,
                'co2': co2
            })
        
        return classified 