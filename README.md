
# 📊 Bloom Filter Implementation

## Overview

This repository contains a **full-fledged implementation of Bloom Filter**, focusing on **efficient membership testing**, **false positive rate analysis**, and **parameter optimization**.  
It is modularized and includes logging, plotting, and dynamic parameter handling.  
The repository demonstrates **theoretical vs experimental** behavior of Bloom Filters.

---
## 💡 Key Concepts

- **Bloom Filter** is a **probabilistic data structure** designed for fast set membership queries with space efficiency.
- It supports **"probably in set"** and **"definitely not in set"** queries.
- Controlled **false positive rate**, tunable via:
  - **Number of hash functions (k)**
  - **Bit array size (m)**
- Space-efficient alternative to traditional sets for large datasets like IP addresses, logs, etc.

---

## ⚙️ Functionalities

### ✅ 1. Bloom Filter Implementation
- Modular `BloomFilter` class.
- Dynamic computation of optimal parameters based on desired false positive rate:
  \\\( m = -\\frac{n \\times \\log(p)}{(\\ln 2)^2} \\)
  \\\( k = \\frac{m}{n} \\times \\ln 2 \\)
- Efficient `add()` and `exists()` functions.
- Seed-based multiple hash functions for better distribution.

### ✅ 2. User Input Handling
- Dynamically takes:
  - Size of IP address dataset.
  - Number of hash functions (or calculates based on false positive rate).
  - Multiplier for Bloom Filter size.
- Validates user input ranges.

### ✅ 3. Random IP Address Generation
- Generates IPv4 addresses of format `xxx.xxx.xxx.xxx`.
- Stores in `ip_addresses.txt`.
- Can handle large datasets (10K, 20K IPs).

### ✅ 4. False Positive Rate Analysis
- Trains Bloom Filter on **half of the IPs**, tests on all IPs.
- Calculates empirical false positive rate:
  \\\( \\text{False Positive Rate} = \\frac{\\text{False Positives}}{\\text{Test Size} - \\text{Training Size}} \\)

### ✅ 5. Visualization & Plotting
- Graph: **False Positive Rate (%) vs Number of Hash Functions**.
- Annotations for:
  - **Optimal number of hash functions** (minimum false positive rate).
  - Configuration details (multiplier, IP size).

### ✅ 6. Logging
- Replaces all `print()` with `logging`:
  - Logs info and status updates.
  - Warning for invalid inputs.
  - False positive rate calculation result.
- Saves logs in `logging_info.txt`.

---

## 📈 Example Graph Built

- **False Positive Rate (%) vs Number of Hash Functions**
- Annotates:
  - Minimum false positive rate.
  - Corresponding number of hash functions.
- Shows IP size and multiplier as notes inside the graph.

---

