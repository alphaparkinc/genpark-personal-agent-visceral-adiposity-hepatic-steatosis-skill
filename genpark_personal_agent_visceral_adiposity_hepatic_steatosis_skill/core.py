# -*- coding: utf-8 -*-
"""Visceral Adiposity & Hepatic Steatosis Screener for GenPark Personal Agent."""
import json
from typing import Dict, Any

class VisceralAdipositySteatosisScreener:
    @staticmethod
    def compute_visceral_adiposity_index(waist_circumference_cm: float, bmi: float, triglycerides_mmol_l: float, hdl_mmol_l: float, gender: str) -> Dict[str, Any]:
        # Amato et al. VAI formulas:
        if gender.lower() == "male":
            wc_term = waist_circumference_cm / (39.68 + (1.88 * bmi))
            tg_term = triglycerides_mmol_l / 1.03
            hdl_term = 1.31 / max(0.1, hdl_mmol_l)
            vai = round(wc_term * tg_term * hdl_term, 2)
        else:
            wc_term = waist_circumference_cm / (36.58 + (1.89 * bmi))
            tg_term = triglycerides_mmol_l / 0.81
            hdl_term = 1.52 / max(0.1, hdl_mmol_l)
            vai = round(wc_term * tg_term * hdl_term, 2)
            
        if vai <= 1.0:
            tier = "OPTIMAL_ZERO_VISCERAL_FAT_DYSFUNCTION"
            risk = "Low risk for non-alcoholic fatty liver disease (NAFLD) and insulin resistance."
        elif vai <= 2.5:
            tier = "MODERATE_ADIPOSE_TISSUE_DYSFUNCTION"
            risk = "Subclinical visceral fat expansion; moderate cardiovascular disease risk."
        else:
            tier = "SEVERE_VISCERAL_OBESITY_STEATOSIS"
            risk = "High probability of hepatic steatosis, elevated cardiometabolic risk, and systemic cytokine inflammation."

        return {
            "gender": gender,
            "visceral_adiposity_index_vai": vai,
            "clinical_tier": tier,
            "pathophysiological_risk": risk
        }

    @staticmethod
    def synthesize_visceral_fat_reduction_plan(vai_score: float) -> Dict[str, Any]:
        return {
            "current_vai": vai_score,
            "target_vai": 1.0,
            "evidence_based_protocols": [
                "Implement 16:8 time-restricted feeding to exhaust liver glycogen and mobilize hepatic lipid droplets",
                "Perform 150 min/week Zone 2 aerobic cycling to upregulate mitochondrial beta-oxidation in hepatocytes",
                "Eliminate all liquid fructose / high-fructose corn syrup to stop de novo lipogenesis (DNL)",
                "Choline & Inositol supplementation (500mg each) to support VLDL export from liver"
            ]
        }
