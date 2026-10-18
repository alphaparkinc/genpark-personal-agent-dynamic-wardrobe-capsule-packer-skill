"""
Personal Agent Capsule Wardrobe Packer (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
from typing import Dict, Any, List

class PersonalAgentCapsuleWardrobePacker:
    def __init__(self, packer_name: str = "GenPark-CapsulePacker-Core"):
        self.packer_name = packer_name

    def curate_capsule_packing_list(self, trip_destination: str, trip_duration_days: int, weather_forecast: Dict[str, Any], activities: List[str] = None) -> Dict[str, Any]:
        t_min = float(weather_forecast.get("temp_min_c", 18.0))
        t_max = float(weather_forecast.get("temp_max_c", 25.0))
        rain_prob = float(weather_forecast.get("rain_probability_pct", 10.0))
        acts = [a.lower() for a in (activities or ["casual sightseeing"])]
        
        items = []
        # Base interchangeable tops & bottoms (using 5-4-3-2-1 rule adapted to duration)
        tops_qty = min(5, max(3, trip_duration_days - 1))
        bottoms_qty = min(3, max(2, trip_duration_days // 2))
        
        items.append({"category": "TOPS", "item": f"{tops_qty}x Merino Wool / Breathable Shirts (Neutral Black/Navy/White)", "qty": tops_qty})
        items.append({"category": "BOTTOMS", "item": f"{bottoms_qty}x Tailored Stretch Trousers / Chinos", "qty": bottoms_qty})
        items.append({"category": "SHOES", "item": "1x Versatile Walking Sneakers + 1x Dress Loafers", "qty": 2})
        
        # Weather adaptations
        if t_min < 12.0:
            items.append({"category": "OUTERWEAR", "item": "1x Packable Down Jacket / Wool Overcoat", "qty": 1})
        elif t_min < 18.0:
            items.append({"category": "LAYER", "item": "1x Lightweight Cashmere / Knit Cardigan", "qty": 1})
            
        if rain_prob > 35.0:
            items.append({"category": "WEATHER_PROTECTION", "item": "1x Ultra-lightweight Waterproof Shell Jacket", "qty": 1})
            
        # Activity adaptations
        if any("keynote" in a or "dining" in a or "gala" in a for a in acts):
            items.append({"category": "FORMAL", "item": "1x Deconstructed Blazer / Cocktail Attire Piece", "qty": 1})
            
        if any("running" in a or "gym" in a for a in acts):
            items.append({"category": "FITNESS", "item": "1x Packable Running Kit & Compression Socks", "qty": 1})
            
        total_pieces = sum(it["qty"] for it in items)
        carry_on_friendly = total_pieces <= 14
        
        return {
            "packer": self.packer_name,
            "destination": trip_destination,
            "duration_days": trip_duration_days,
            "temperature_range": f"{t_min}C to {t_max}C",
            "rain_forecast": f"{rain_prob}%",
            "total_capsule_pieces": total_pieces,
            "carry_on_compliant": carry_on_friendly,
            "capsule_manifest": items,
            "verdict": "CAPSULE_WARDROBE_CURATED"
        }
