# 🏥 UAE Business Directory Scraper (Yellow Pages)

This project is a professional-grade web scraping solution built to extract high-quality business leads from the UAE's primary directories. It uses **Selenium** to handle dynamic web elements and **Python** for data structuring.

## 📊 What is being extracted?
The scraper is designed to capture every essential detail needed for lead generation and market analysis. For every business listing, the script extracts:

* **Business Name:** Full registered name of the hospital/company.
* **Phone Number:** Cleaned contact numbers (directly from the dialer links).
* **City & Location:** Specific area and city within the UAE.
* **Website URL:** Official business website for further research.
* **Products & Services:** Detailed tags and categories the business specializes in.

---

## 📂 Pre-Scraped Industry Categories
I have already utilized this scraper to build a massive database of businesses across the UAE. Below is a list of industries I have successfully extracted and cleaned:

### 🏗️ Construction & Engineering
* Builders & General Contractors
* Oilfield Services
* Maintenance Services
* Kitchen Equipment Suppliers

### 🏥 Healthcare & Science
* Hospitals & Clinics
* Pharmacies
* Diagnostic Centers

### 💼 Professional Services
* Accounting & Audit Firms
* Advertising & Marketing Agencies
* Institute of Chartered Accountants (CAs)

### 🍽️ Hospitality & Retail
* Restaurants & Cafes
* Food Importers
* Furniture & Interior Design
* Garments & Fashion Retail
* Jewelers

---

## 🛠️ How it Works
1.  **Navigation:** The script iterates through pagination (e.g., page 1 to 100).
2.  **Parsing:** It identifies each business card using specific CSS selectors.
3.  **Extraction:** Using XPATH, it pulls data even if some fields (like website or phone) are missing.
4.  **Storage:** The final output is saved in a structured `Hospitals_UAE.csv` file, ready for CRM import.
