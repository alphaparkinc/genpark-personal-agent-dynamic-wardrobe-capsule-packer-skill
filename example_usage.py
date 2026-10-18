from client import PersonalAgentCapsuleWardrobePacker

def main():
    packer = PersonalAgentCapsuleWardrobePacker()
    wf = {"temp_min_c": 14.0, "temp_max_c": 22.0, "rain_probability_pct": 20.0}
    res = packer.curate_capsule_packing_list("San Francisco", 5, wf, ["AI Summit Keynote", "Running in Marina"])
    print("--- Capsule Wardrobe Travel Plan ---")
    print(f"Destination: {res['destination']} ({res['duration_days']} Days) | Temp: {res['temperature_range']}")
    print(f"Carry-on Compliant: {res['carry_on_compliant']} ({res['total_capsule_pieces']} pieces)")
    for it in res['capsule_manifest']:
        print(f"* [{it['category']}] {it['item']}")

if __name__ == "__main__":
    main()
