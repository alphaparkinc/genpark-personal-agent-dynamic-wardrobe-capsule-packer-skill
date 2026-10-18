#!/usr/bin/env python3
import json
import sys
from client import PersonalAgentCapsuleWardrobePacker

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        packer = PersonalAgentCapsuleWardrobePacker()
        wf = {"temp_min_c": 8.0, "temp_max_c": 16.0, "rain_probability_pct": 50.0}
        res = packer.curate_capsule_packing_list("London", 4, wf, ["keynotes", "casual sightseeing"])
        assert res["carry_on_compliant"] is True
        assert any("Waterproof" in it["item"] for it in res["capsule_manifest"])
        print(f"[TEST PASS] Capsule Wardrobe Pieces: {res['total_capsule_pieces']} (Carry-on: {res['carry_on_compliant']})")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-capsule-packer", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "curate_capsule_packing_list", "description": "Curate weather-adaptive minimalist capsule wardrobe"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                packer = PersonalAgentCapsuleWardrobePacker()
                out = packer.curate_capsule_packing_list(
                    args.get("trip_destination", "City"),
                    int(args.get("trip_duration_days", 3)),
                    args.get("weather_forecast", {}),
                    args.get("activities", [])
                )
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
