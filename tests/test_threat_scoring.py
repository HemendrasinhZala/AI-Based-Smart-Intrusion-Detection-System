"""
===========================================================
AI Intrusion Detection System
Threat Scoring Test

Author : Hemendrasinh Zala
===========================================================
"""

from core.threat_scoring import ThreatScoring


def print_result(title, score, level):
    print("=" * 50)
    print(title)
    print(f"Threat Score : {score}")
    print(f"Threat Level : {level}")
    print("=" * 50)
    print()


def main():

    threat = ThreatScoring()

    # ----------------------------------------
    # Test 1 : No Motion
    # ----------------------------------------

    score = threat.calculate_score(
        motion_detected=False,
        human_detected=False,
        confidence=0.0,
        human_count=0
    )

    print_result(
        "Test 1 : No Motion",
        score,
        threat.get_threat_level()
    )

    # ----------------------------------------
    # Test 2 : Motion Only
    # ----------------------------------------

    score = threat.calculate_score(
        motion_detected=True,
        human_detected=False,
        confidence=0.0,
        human_count=0
    )

    print_result(
        "Test 2 : Motion Only",
        score,
        threat.get_threat_level()
    )

    # ----------------------------------------
    # Test 3 : Human Detected
    # ----------------------------------------

    score = threat.calculate_score(
        motion_detected=True,
        human_detected=True,
        confidence=0.75,
        human_count=1
    )

    print_result(
        "Test 3 : Human (75%)",
        score,
        threat.get_threat_level()
    )

    # ----------------------------------------
    # Test 4 : High Confidence
    # ----------------------------------------

    score = threat.calculate_score(
        motion_detected=True,
        human_detected=True,
        confidence=0.95,
        human_count=1
    )

    print_result(
        "Test 4 : Human (95%)",
        score,
        threat.get_threat_level()
    )

    # ----------------------------------------
    # Test 5 : Multiple Humans
    # ----------------------------------------

    score = threat.calculate_score(
        motion_detected=True,
        human_detected=True,
        confidence=0.98,
        human_count=3
    )

    print_result(
        "Test 5 : Three Humans",
        score,
        threat.get_threat_level()
    )

    # ----------------------------------------
    # High Threat Check
    # ----------------------------------------

    print("High Threat :", threat.is_high_threat())


if __name__ == "__main__":
    main()