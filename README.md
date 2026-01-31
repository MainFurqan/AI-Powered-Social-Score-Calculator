![Social Score Calculator Flowchart](flowchart.png)

# 📊 AI Powered Social Score Calculator

## 📌 Project Overview

This project focuses on designing and implementing a **data-driven Social Score algorithm** to evaluate Instagram influencers from a brand’s perspective. The Social Score quantifies an influencer’s effectiveness by combining **engagement behavior, audience quality, visibility, and reach** into a single interpretable metric.

The system is built using **scraped Instagram profile data**, statistical feature engineering, and **LLM-based audience intent analysis** (Gemini) to ensure that not just volume, but *quality and relevance* of interactions are captured.

---

## 🎯 Objective

To compute a **robust, normalized Social Score** for each influencer that helps brands:

* Compare influencers objectively
* Identify high-quality audiences
* Reduce reliance on vanity metrics
* Make data-backed influencer marketing decisions

---

## 🧠 Social Score Architecture

The Social Score is composed of **four major components**, derived from industry research and weighted according to their relative importance for brand impact.

| Component            | Description                                | Weight  |
| -------------------- | ------------------------------------------ | ------- |
| **Q2 Engagement**    | High-quality engagement (likes + comments) | **50%** |
| **Audience Quality** | Relevance and purchase intent of comments  | **25%** |
| **Q2 Views**         | Video visibility relative to audience size | **17%** |
| **Followers**        | Influencer reach                           | **8%**  |

> **Note:** The weights sum to 100% and reflect brand-centric influencer evaluation rather than raw popularity.

---

## 🧹 Data Cleaning & Normalization

Instagram metrics often contain non-numeric suffixes:

* `K` → Thousands
* `M` → Millions

### Example

* `741K` → `741,000`
* `1.5M` → `1,500,000`

All such values are:

* Parsed
* Converted into numeric format
* Standardized for downstream calculations

---

## 🔧 Feature Engineering

### 1️⃣ Engagement Feature

A new feature **Engagement** is derived by combining:

```
Engagement = Number of Likes + Number of Comments


### 2️⃣ Audience Quality (LLM-based)

Audience quality is assessed using **Gemini (LLM)** by analyzing comment intent.

#### LLM Role Definition

Gemini is instructed to classify each comment as:

**Relevant Comments**

* Purchase intent
* Product feedback
* Brand-related discussion
* Product authenticity or quality discussion

**Irrelevant Comments**

* Emojis only
* Generic phrases ("Nice", "Cool")
* Spam or bot-like content
* Self-promotion
* Unrelated discussion

#### Audience Quality Formula

```
Audience Quality (%) = (Relevant Comments / Total Comments) × 100
```

---

### 3️⃣ Engagement Rate

```
Engagement (%) = (Q2 Engagement / Number of Followers) × 100
```

---

### 4️⃣ View Rate

```
Views (%) = (Q2 Views / Number of Followers) × 100
```

---

## 🧮 Social Score Calculation

Each component is multiplied by its predefined weight and summed to produce the final score.

```
Social Score =
(0.50 × Engagement %) +
(0.25 × Audience Quality %) +
(0.17 × Views %) +
(0.08 × Followers Score)
```

The result is a **single normalized score** representing the influencer’s overall brand value.

---

## 📈 Key Highlights

* Uses **Q2 (median)** instead of mean to reduce outlier bias
* Incorporates **LLM-based semantic understanding** of audience behavior
* Moves beyond vanity metrics
* Brand-focused and scalable
* Modular and extensible scoring system

---

## 🛠️ Tech Stack

* **Python** (Data processing & scoring)
* **Pandas / NumPy** (Data manipulation)
* **Gemini API** (Audience intent classification)

---

## 📌 Conclusion

This project delivers a **production-grade influencer scoring framework** that aligns influencer evaluation with real business value. By integrating statistical rigor with LLM-based semantic analysis, the Social Score provides a reliable metric for influencer-brand alignment.

---

**Author:** Furqan
**Domain:** Data Science | Machine Learning 
