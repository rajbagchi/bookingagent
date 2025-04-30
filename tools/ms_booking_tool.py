from langchain.tools import tool

_APPT_SLUGS = {
    "land_use": "LandUseAppointment",
    "environmental": "EnvironmentalAppointment",
    "zoning_tree": "ZoningTreeCode",
    "residential_building": "ResidentialBuildingCode",
    "commercial_building": "CommercialBuildingCode",
    "structural_engineering": "StructuralEngineering",
    "site_development": "SiteDevelopment",
    "residential_permit_tech": "ResidentialPermitTechnician",
    "commercial_permit_tech": "CommercialPermitTechnician",
    "stars": "STARSAppointment",
    "water_services": "WaterServices",
    "water_quality_backflow": "WaterQualityBackflow",
    "sewer_stormwater": "SewerStormwater",
    "fire_safety": "FireSafety",
    "transportation_residential": "TransportationResidential",
    "transportation_commercial": "TransportationCommercial",
    "urban_forestry": "UrbanForestryTreeTech",
    "mechanical_engineering": "MechanicalEngineering",
    "land_division": "LandDivisionAdjustment",
    "design_historic": "DesignHistoricReviews"
}

_BASE_URL = ("https://outlook.office365.com/owa/calendar/"
             "DevelopmentServices15MinuteQuestions@portlandoregon.gov/bookings/")

@tool
def get_booking_link(topic_key: str) -> str:
    """Return booking link for an appointment type."""
    slug = _APPT_SLUGS.get(topic_key)
    if not slug:
        return "❌ Unknown appointment type. Available: " + ", ".join(_APPT_SLUGS.keys())
    return _BASE_URL + slug
