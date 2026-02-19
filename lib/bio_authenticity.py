"""
Bio-Authenticity Module for VerifyAI
Advanced facial analysis for detecting beauty filters and age manipulation
"""

import json
import numpy as np
from typing import Dict, List, Tuple
import google.generativeai as genai
from PIL import Image
from io import BytesIO
import base64


class BioAuthenticityAnalyzer:
    """
    Analyzes facial biometrics to detect:
    - Skin luminosity vs age correlation
    - Eyelid and eyebrow drooping levels
    - Dental exposure during smiles
    - True-Age vs Apparent-Age discrepancies
    """

    def __init__(self, api_key: str = None):
        """Initialize the analyzer with Gemini API"""
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze_skin_luminosity(self, image_data: bytes) -> Dict:
        """
        Analyze skin luminosity patterns to detect age-related changes
        and beauty filter application
        """
        try:
            image = Image.open(BytesIO(image_data))
            
            prompt = """Analyze this facial image for skin characteristics:
1. Analyze skin luminosity/brightness levels (0-100 scale)
2. Detect skin texture smoothness (0-100, where 100 is unnaturally smooth)
3. Identify pore visibility (0-100, where 0 is no pores visible - likely filtered)
4. Assess wrinkle/line prominence (0-100)
5. Evaluate skin tone uniformity (0-100)
6. Detect signs of beauty filters or smoothing (0-100 probability)

Return ONLY valid JSON with these exact keys:
{
  "luminosity": number,
  "smoothness": number,
  "pore_visibility": number,
  "wrinkle_prominence": number,
  "tone_uniformity": number,
  "filter_probability": number,
  "analysis": "brief description"
}"""

            response = self.model.generate_content([prompt, image])
            result = self._parse_json_response(response.text)
            
            return {
                "status": "success",
                "skin_analysis": result,
                "filter_detected": result.get("filter_probability", 0) > 60
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "skin_analysis": self._get_mock_skin_analysis()
            }

    def analyze_eye_features(self, image_data: bytes) -> Dict:
        """
        Analyze eyelid and eyebrow drooping levels
        Detect signs of age-related changes and filter effects
        """
        try:
            image = Image.open(BytesIO(image_data))
            
            prompt = """Analyze the eye area in this facial image:
1. Measure eyelid drooping level (0-100, where 100 is maximum drooping)
2. Assess eyebrow position/drooping (0-100)
3. Evaluate eye bags/puffiness (0-100)
4. Analyze crow's feet visibility (0-100)
5. Check for under-eye darkness (0-100)
6. Detect eye area smoothing/filtering (0-100 probability)
7. Assess eye openness (0-100, where 100 is fully open)

Return ONLY valid JSON:
{
  "eyelid_drooping": number,
  "eyebrow_drooping": number,
  "eye_bags": number,
  "crows_feet": number,
  "under_eye_darkness": number,
  "eye_filtering": number,
  "eye_openness": number,
  "age_indicators": "description"
}"""

            response = self.model.generate_content([prompt, image])
            result = self._parse_json_response(response.text)
            
            return {
                "status": "success",
                "eye_analysis": result,
                "age_signs_detected": result.get("eyelid_drooping", 0) > 30 or result.get("crows_feet", 0) > 40
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "eye_analysis": self._get_mock_eye_analysis()
            }

    def analyze_dental_features(self, image_data: bytes) -> Dict:
        """
        Analyze dental exposure and smile characteristics
        Detect age-related dental changes and smile authenticity
        """
        try:
            image = Image.open(BytesIO(image_data))
            
            prompt = """Analyze the dental and smile features in this facial image:
1. Measure tooth visibility percentage (0-100)
2. Assess gum exposure level (0-100)
3. Evaluate tooth color/whiteness (0-100)
4. Check for tooth wear/yellowing (0-100)
5. Analyze smile authenticity (0-100, where 100 is genuine Duchenne smile)
6. Detect smile line symmetry (0-100)
7. Assess mouth corner elevation (0-100)
8. Detect dental whitening/filtering (0-100 probability)

Return ONLY valid JSON:
{
  "tooth_visibility": number,
  "gum_exposure": number,
  "tooth_whiteness": number,
  "tooth_wear": number,
  "smile_authenticity": number,
  "smile_symmetry": number,
  "mouth_elevation": number,
  "whitening_filtering": number,
  "dental_age_indicators": "description"
}"""

            response = self.model.generate_content([prompt, image])
            result = self._parse_json_response(response.text)
            
            return {
                "status": "success",
                "dental_analysis": result,
                "authentic_smile": result.get("smile_authenticity", 0) > 70
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "dental_analysis": self._get_mock_dental_analysis()
            }

    def calculate_true_age_vs_apparent_age(self, 
                                          skin_analysis: Dict,
                                          eye_analysis: Dict,
                                          dental_analysis: Dict,
                                          stated_age: int = None) -> Dict:
        """
        Calculate True-Age vs Apparent-Age based on biometric indicators
        Detect age manipulation and beauty filter usage
        """
        try:
            skin = skin_analysis.get("skin_analysis", {})
            eyes = eye_analysis.get("eye_analysis", {})
            dental = dental_analysis.get("dental_analysis", {})

            # Age calculation based on facial features
            age_indicators = []
            age_score = 0
            weight_count = 0

            # Skin indicators (weight: 35%)
            skin_weight = 0.35
            wrinkle_score = skin.get("wrinkle_prominence", 0)
            age_from_wrinkles = (wrinkle_score / 100) * 60  # Max 60 years from wrinkles
            age_score += age_from_wrinkles * skin_weight
            weight_count += skin_weight
            age_indicators.append({
                "factor": "Wrinkle Prominence",
                "score": wrinkle_score,
                "estimated_age_contribution": age_from_wrinkles
            })

            # Eye indicators (weight: 35%)
            eye_weight = 0.35
            eyelid_drooping = eyes.get("eyelid_drooping", 0)
            crows_feet = eyes.get("crows_feet", 0)
            age_from_eyes = ((eyelid_drooping + crows_feet) / 200) * 50  # Max 50 years
            age_score += age_from_eyes * eye_weight
            weight_count += eye_weight
            age_indicators.append({
                "factor": "Eye Features (drooping + crow's feet)",
                "score": (eyelid_drooping + crows_feet) / 2,
                "estimated_age_contribution": age_from_eyes
            })

            # Dental indicators (weight: 30%)
            dental_weight = 0.30
            tooth_wear = dental.get("tooth_wear", 0)
            age_from_dental = (tooth_wear / 100) * 40  # Max 40 years from dental
            age_score += age_from_dental * dental_weight
            weight_count += dental_weight
            age_indicators.append({
                "factor": "Dental Wear",
                "score": tooth_wear,
                "estimated_age_contribution": age_from_dental
            })

            # Normalize age score
            apparent_age = int(age_score / weight_count) + 18  # Minimum 18 years

            # Calculate filter impact
            filter_impact = (
                skin.get("filter_probability", 0) * 0.4 +
                eyes.get("eye_filtering", 0) * 0.35 +
                dental.get("whitening_filtering", 0) * 0.25
            )

            # Calculate true age (accounting for filters)
            age_reduction_from_filters = (filter_impact / 100) * 15  # Filters can reduce apparent age by up to 15 years
            true_age = apparent_age + int(age_reduction_from_filters)

            # Age manipulation detection
            age_manipulation_score = 0
            manipulation_factors = []

            if skin.get("filter_probability", 0) > 60:
                age_manipulation_score += 30
                manipulation_factors.append("Heavy skin smoothing/filtering detected")

            if eyes.get("eye_filtering", 0) > 50:
                age_manipulation_score += 25
                manipulation_factors.append("Eye area filtering detected")

            if dental.get("whitening_filtering", 0) > 60:
                age_manipulation_score += 20
                manipulation_factors.append("Dental whitening/filtering detected")

            # Consistency check
            if stated_age and abs(stated_age - true_age) > 10:
                age_manipulation_score += 15
                manipulation_factors.append(f"Stated age ({stated_age}) differs significantly from calculated age ({true_age})")

            # Cap manipulation score at 100
            age_manipulation_score = min(age_manipulation_score, 100)

            return {
                "status": "success",
                "apparent_age": apparent_age,
                "true_age": true_age,
                "age_difference": true_age - apparent_age,
                "stated_age": stated_age,
                "age_manipulation_probability": age_manipulation_score,
                "is_age_manipulated": age_manipulation_score > 50,
                "filter_impact_score": int(filter_impact),
                "age_indicators": age_indicators,
                "manipulation_factors": manipulation_factors,
                "confidence_score": 85 if age_manipulation_score < 30 else (70 if age_manipulation_score < 60 else 55),
                "recommendation": self._get_age_recommendation(age_manipulation_score, true_age, stated_age)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "apparent_age": None,
                "true_age": None
            }

    def comprehensive_bio_authenticity_report(self,
                                             image_data: bytes,
                                             stated_age: int = None) -> Dict:
        """
        Generate comprehensive Bio-Authenticity report
        Combines all analyses into a single report
        """
        try:
            # Run all analyses
            skin_analysis = self.analyze_skin_luminosity(image_data)
            eye_analysis = self.analyze_eye_features(image_data)
            dental_analysis = self.analyze_dental_features(image_data)

            # Calculate age analysis
            age_analysis = self.calculate_true_age_vs_apparent_age(
                skin_analysis,
                eye_analysis,
                dental_analysis,
                stated_age
            )

            # Calculate overall authenticity score
            overall_authenticity = 100 - (
                (skin_analysis.get("skin_analysis", {}).get("filter_probability", 0) * 0.35) +
                (eye_analysis.get("eye_analysis", {}).get("eye_filtering", 0) * 0.35) +
                (dental_analysis.get("dental_analysis", {}).get("whitening_filtering", 0) * 0.30)
            )

            return {
                "status": "success",
                "report_type": "Bio-Authenticity Analysis",
                "overall_authenticity_score": max(0, int(overall_authenticity)),
                "is_authentic": overall_authenticity > 65,
                "skin_analysis": skin_analysis.get("skin_analysis", {}),
                "eye_analysis": eye_analysis.get("eye_analysis", {}),
                "dental_analysis": dental_analysis.get("dental_analysis", {}),
                "age_analysis": age_analysis,
                "summary": self._generate_summary(
                    skin_analysis,
                    eye_analysis,
                    dental_analysis,
                    age_analysis,
                    overall_authenticity
                )
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    @staticmethod
    def _parse_json_response(response_text: str) -> Dict:
        """Parse JSON from Gemini response"""
        try:
            text = response_text.strip()
            if text.startswith('```'):
                text = text.split('```')[1]
                if text.startswith('json'):
                    text = text[4:]
            return json.loads(text)
        except:
            return {}

    @staticmethod
    def _get_mock_skin_analysis() -> Dict:
        """Return mock skin analysis data"""
        return {
            "luminosity": 72,
            "smoothness": 65,
            "pore_visibility": 45,
            "wrinkle_prominence": 35,
            "tone_uniformity": 78,
            "filter_probability": 40,
            "analysis": "Moderate skin smoothing detected, consistent with beauty filter usage"
        }

    @staticmethod
    def _get_mock_eye_analysis() -> Dict:
        """Return mock eye analysis data"""
        return {
            "eyelid_drooping": 25,
            "eyebrow_drooping": 20,
            "eye_bags": 30,
            "crows_feet": 35,
            "under_eye_darkness": 40,
            "eye_filtering": 35,
            "eye_openness": 75,
            "age_indicators": "Moderate age indicators present"
        }

    @staticmethod
    def _get_mock_dental_analysis() -> Dict:
        """Return mock dental analysis data"""
        return {
            "tooth_visibility": 65,
            "gum_exposure": 15,
            "tooth_whiteness": 85,
            "tooth_wear": 25,
            "smile_authenticity": 78,
            "smile_symmetry": 82,
            "mouth_elevation": 70,
            "whitening_filtering": 45,
            "dental_age_indicators": "Teeth appear whitened, consistent with cosmetic treatment"
        }

    @staticmethod
    def _get_age_recommendation(manipulation_score: int, true_age: int, stated_age: int = None) -> str:
        """Generate age verification recommendation"""
        if manipulation_score > 70:
            return "⚠️ HIGH RISK: Significant age manipulation detected. Recommend manual verification."
        elif manipulation_score > 50:
            return "⚠️ MEDIUM RISK: Moderate age manipulation indicators present. Recommend additional verification."
        elif stated_age and abs(stated_age - true_age) > 5:
            return "⚠️ LOW RISK: Minor discrepancies detected. Recommend review."
        else:
            return "✓ LOW RISK: Image appears authentic with minimal manipulation indicators."

    @staticmethod
    def _generate_summary(skin_analysis: Dict, eye_analysis: Dict, dental_analysis: Dict, age_analysis: Dict, overall_authenticity: float) -> str:
        """Generate comprehensive summary"""
        summary = f"""
Bio-Authenticity Analysis Summary:

Overall Authenticity Score: {int(overall_authenticity)}%
Status: {'✓ AUTHENTIC' if overall_authenticity > 65 else '⚠️ POTENTIALLY MANIPULATED'}

Age Analysis:
- Apparent Age: {age_analysis.get('apparent_age', 'N/A')} years
- True Age: {age_analysis.get('true_age', 'N/A')} years
- Age Manipulation Probability: {age_analysis.get('age_manipulation_probability', 0)}%

Key Findings:
- Skin: {'Natural' if skin_analysis.get('skin_analysis', {}).get('filter_probability', 0) < 50 else 'Filtered'}
- Eyes: {'Natural' if eye_analysis.get('eye_analysis', {}).get('eye_filtering', 0) < 50 else 'Filtered'}
- Dental: {'Natural' if dental_analysis.get('dental_analysis', {}).get('whitening_filtering', 0) < 50 else 'Enhanced'}

Recommendation: {age_analysis.get('recommendation', 'N/A')}
        """
        return summary.strip()
