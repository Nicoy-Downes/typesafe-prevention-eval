# Experiment Mapping

OPTION_A_CRITERIA = {
    "primary": (
        "Typically population-wide interventions to prevent disease before it starts "
        "or to mitigate the impact of risk factors. For example, reducing air pollution, "
        "stopping young people smoking, or vaccination."
    ),
    "secondary": (
        "Early detection and prevention of early disease progression. "
        "For example, screening programmes or weight loss drugs."
    ),
    "tertiary": (
        "Managing an existing condition to prevent worsening severity, "
        "reduce complications, and improve quality of life."
    ),
    "not_prevention": (
        "The text does not describe a prevention-related intervention. "
        "It concerns treatment, basic research, data infrastructure, or other topics "
        "not related to preventing disease or managing risk."
    ),
}

OPTION_B_CRITERIA = {
    "primary": (
        "For healthy individuals, on an individual, group or population level, "
        "preventing the occurrence of ill-health or care needs. For example, health "
        "communication, wellbeing, policy or regulation of unhealthy commodities, "
        "finding and staying in work, diet, public health policy, behaviour or "
        "environmental change for risk reduction, vaccination, understanding personalised "
        "risk, chemoprevention."
    ),
    "early_detection": (
        "Secondary prevention: Research focusing on detecting disease or care needs early "
        "to enable effective treatment or support. For example, screening, case-finding, "
        "speeding up diagnosis within a pathway, surveillance for early detection."
    ),
    "risk_intervention": (
        "Secondary prevention: For people at increased risk of poor health, treating and "
        "addressing targeted risk indicators, including pre-disease conditions. For example, "
        "statins to reduce hypercholesterolaemia, lifestyle changes for overweight, treating "
        "pre-cancerous changes, targeted wellbeing interventions for at-risk groups."
    ),
    "treatment_management": (
        "Tertiary prevention: For those with a new or chronic condition, reducing progression "
        "after diagnosis, preventing or detecting relapse or recurrence, stopping development "
        "of further health conditions, enabling recovery, self- or supported management."
    ),
    "not_prevention": (
        "The text does not describe a prevention-related intervention. "
        "It concerns treatment, basic research, data infrastructure, or other topics "
        "not related to preventing disease or managing risk."
    ),
}

# Evaluation Mapping

OPTION_A_MAP = {
    "primary": "Primary",
    "secondary": "Secondary",
    "tertiary": "Tertiary/Treatment",
    "not_prevention": "Not Prevention",
}

OPTION_B_MAP = {
    "primary": "Primary",
    "early_detection": "Secondary",
    "risk_intervention": "Secondary",
    "treatment_management": "Tertiary/Treatment",
    "not_prevention": "Not Prevention",
}

HUMAN_LABELS = ["Primary", "Secondary", "Tertiary/Treatment", "Not Prevention"]

OPTION_B_LABELS = [
    "primary",
    "early_detection",
    "risk_intervention",
    "treatment_management",
    "not_prevention",
]

