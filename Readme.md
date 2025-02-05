# ESO Trial Score & Vitality Calculator

## Overview
This project provides a Python library for calculating and verifying vitality in **Elder Scrolls Online (ESO) trial runs**. The function accurately derives the vitality number from a given trial score and run duration while ensuring correctness within ESO’s scoring system.
> [!NOTE]
> This tool was developed as part of the WildBot project for the [WildHeart](https://discord.gg/WildHeart) community on Discord.
> I've decided to share it as an Open-Source in hope to make it easier for the community to develop more tools, so please do use it!

## Features
- Calculates vitality based on the trial's **base score and duration**.
- Supports both **standard and bonus base scores** for trials that have additional scoring rules.
- **Verifies the calculated vitality** to ensure correctness.
- Works for all ESO Veteran **Hard-Mode** trials (full HM clear).

## Installation
Clone the repository:
```sh
$ git clone https://github.com/SkullElf/eso-trial-vitality.git
$ cd eso-trial-vitality
```

## Usage
Import the utility function and pass the **trial name, score, and duration in seconds**.

```python
from vitality import calculate_vitality

result = calculate_vitality("Rockgrove", 309756, 886)  # 14 minutes and 46 seconds
print(result)  # Output: "X/36" or "X/36 with bonus" or "N/A"
```

## Examples
```python
# Example 1 - Rockgrove
result = calculate_vitality("Rockgrove", 309756, 886)
print("Rockgrove example:", result)  # Expected output: X/36 or X/36 with bonus

# Example 2 - Lucent Citadel
result = calculate_vitality("Lucent Citadel", 261808, 1209)
print("Lucent Citadel example:", result)

# Example 3 - Sanity's Edge
result = calculate_vitality("Sanity's Edge", 275680, 1222)
print("Sanity's Edge example:", result)

# Example 4 - Invalid result (Cloudrest with an incorrect score)
result = calculate_vitality("Cloudrest", 980000, 700)
print("Cloudrest example:", result)  # Expected output: N/A
```

## Supported Trials
This library supports the following ESO trials:
- **Aetherian Archive**
- **Hel Ra Citadel**
- **Sanctum Ophidia**
- **Maw of Lorkhaj**
- **Halls of Fabrication**
- **Asylum Sanctorium**
- **Cloudrest** (with bonus variation for trash)
- **Sunspire**
- **Kyne's Aegis**
- **Rockgrove** (with bonus variation for Snake & Wounded Soldiers)
- **Dreadsail Reef**
- **Sanity's Edge**
- **Lucent Citadel**

## Contributing
Pull requests are welcome! If you have suggestions or improvements, feel free to fork the repo and submit a PR.

## Credits
This project was developed by **SkullElf**, with contributions from the **WildHeart and Nexus communities**. Special thanks to @Fostecks for sharing and maintaining the ESO’s trials scoring calculator, based on which this tool was built.

## License
This project is open-source under the **MIT License**.

