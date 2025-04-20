"""
Legal FAQ data for the JusticeAI application.
Contains pre-defined questions and answers about Indian law.
"""

# FAQ categories organized by legal domains
LEGAL_FAQ_CATEGORIES = {
    "Property & Rental": {
        "What are my rights as a tenant in India?": 
            "In India, tenants have several rights including: 1) Protection from arbitrary eviction without proper notice, "
            "2) Right to peaceful possession of the property, 3) Right to essential services like water and electricity, "
            "4) Right to proper receipts for rent payments, and 5) Protection from unreasonable rent increases. "
            "These rights vary by state as rental laws in India are state-specific. In many states, tenants can only be "
            "evicted through court orders, not by force.",
        
        "What should I check before signing a rental agreement?": 
            "Before signing a rental agreement in India, check: 1) Proper details of landlord and tenant, "
            "2) Property description and condition, 3) Rent amount, security deposit and payment terms, "
            "4) Duration of tenancy and renewal terms, 5) Maintenance responsibilities, "
            "6) Notice period for termination, 7) List of fixtures and fittings, "
            "8) Whether the agreement needs registration (mandatory for agreements of 12+ months), "
            "9) Permitted usage and restrictions, and 10) Dispute resolution mechanism.",
        
        "How much security deposit can a landlord legally ask for?": 
            "In India, there's no uniform national law specifying maximum security deposit amounts. "
            "Practices vary by state and city. In Bangalore/Karnataka, the norm is 10 months' rent, while "
            "in Mumbai/Maharashtra, it's typically 2-3 months' rent. Delhi and other north Indian cities usually "
            "ask for 2-3 months' rent. Unless restricted by specific state laws, landlords can technically demand "
            "any amount, though excessive demands may be challenged in consumer courts as unfair trade practice.",
        
        "Can a landlord evict me without notice?": 
            "No, a landlord cannot legally evict you without proper notice in India. Eviction must follow legal procedures, "
            "which typically require: 1) A valid reason for eviction (e.g., non-payment of rent, property damage, illegal activities), "
            "2) Proper written notice as specified in your rental agreement (usually 1-3 months), and "
            "3) A court order if you refuse to vacate. Forceful eviction without court orders is illegal under Indian law "
            "and can result in penalties under the Indian Penal Code. If threatened with illegal eviction, you can file a police complaint.",
        
        "What is the difference between lease and rental agreement?": 
            "In India, the key differences between lease and rental agreements are: 1) Duration: Lease agreements are typically "
            "for longer periods (usually 12+ months) while rental agreements are for shorter terms (often 11 months). "
            "2) Registration: Leases exceeding 12 months must be legally registered with sub-registrar's office, while most rental "
            "agreements are unregistered. 3) Transferability: Lease rights can often be transferred to third parties if the lease "
            "permits, while rental agreements generally don't allow this. 4) Renewability: Lease terms are fixed for the duration "
            "while rental agreements are easier to modify upon renewal."
    },
    
    "Consumer Rights": {
        "How do I file a consumer complaint in India?": 
            "To file a consumer complaint in India: 1) First send a written complaint to the company/service provider, "
            "2) If unsatisfied with the response, file a complaint with the appropriate Consumer Disputes Redressal Commission "
            "(District/State/National level based on claim amount). Under the Consumer Protection Act 2019, you can file: "
            "a) Up to ₹1 crore at District Commission, b) ₹1-10 crore at State Commission, c) Above ₹10 crore at National Commission. "
            "You can file complaints online through the CONFONET portal or in person. No lawyer is required, and the fee is minimal.",
        
        "What is the cooling-off period for online purchases?": 
            "India doesn't have a universal statutory 'cooling-off period' for all online purchases. However, e-commerce platforms "
            "typically offer return/refund policies (usually 7-30 days) as per their terms. The Consumer Protection (E-Commerce) "
            "Rules, 2020 require sellers to clearly display return, refund, and exchange policies. For specific products, sectoral "
            "regulations may apply - for instance, IRDAI mandates a 15-day free-look period for insurance policies. If a product is "
            "defective, you can seek remedies under the Consumer Protection Act regardless of the seller's return policy.",
        
        "Can I return products purchased during sales?": 
            "Yes, you can return products purchased during sales in India, provided you comply with the seller's return policy that was "
            "disclosed at the time of purchase. Under the Consumer Protection Act, 2019, sellers must honor their advertised policies. "
            "However, many retailers have special 'no returns' or 'exchange only' policies for sale items, which are valid if clearly "
            "communicated before purchase. If the product is defective, you retain your right to return it regardless of sale status. "
            "Always check the sale-specific return policy and keep all receipts and tags intact when returning items.",
        
        "What rights do I have if a product is defective?": 
            "If a product is defective in India, you have the following rights under the Consumer Protection Act, 2019: "
            "1) Replacement with a non-defective product, 2) Refund of the purchase price, 3) Compensation for any damage or loss suffered, "
            "4) Repair of the defective product free of charge. To exercise these rights: Keep proof of purchase, report the defect to the "
            "seller immediately, document the issue with photos/videos if possible, and file a formal complaint with the seller. If not "
            "resolved satisfactorily, you can approach the Consumer Disputes Redressal Commission within 2 years from the date of cause of action.",
        
        "How long should a company take to process my refund?": 
            "Indian consumer protection laws don't specify exact timeframes for processing refunds, but under the Consumer Protection Act, "
            "refunds should be processed within a 'reasonable time'. Generally, e-commerce platforms typically process refunds within 5-14 business "
            "days after receiving the returned product, though credit card refunds may take additional time (7-14 days) to reflect in your account. "
            "Companies must adhere to their own stated refund policies. If a company takes unreasonably long to process your refund, you can file a "
            "complaint with the National Consumer Helpline (1800-11-4000) or the appropriate Consumer Disputes Redressal Commission."
    },
    
    "Employment Law": {
        "What should I check before signing an employment contract?": 
            "Before signing an employment contract in India, check: 1) Job title, role, responsibilities, and reporting structure, "
            "2) Compensation details including base salary, bonuses, and benefits, 3) Work hours, leave policy, and holidays, "
            "4) Probation period and terms, 5) Notice period for resignation/termination, 6) Non-compete and non-disclosure clauses, "
            "7) Intellectual property rights, 8) Performance evaluation criteria, 9) Grounds for termination, and "
            "10) Dispute resolution mechanism. Ensure the contract complies with relevant labor laws like the Minimum Wages Act, "
            "Payment of Gratuity Act, and state-specific shops and establishments acts.",
        
        "What is the legal notice period for resigning from a job?": 
            "In India, there is no universal statutory notice period for resignation. The notice period is governed by the terms "
            "specified in your employment contract, which typically ranges from 1-3 months. The Industrial Employment (Standing Orders) "
            "Act requires workmen to give notice as specified in their appointment terms or standing orders. For non-workmen, the "
            "contract terms prevail. If the contract doesn't specify a notice period, reasonable notice should be given based on "
            "industry practices. Some companies may waive the notice period or accept payment in lieu of notice at their discretion.",
        
        "Can my employer force me to work overtime?": 
            "In India, whether an employer can force overtime depends on the applicable labor laws and your employment contract. "
            "For factory workers, the Factories Act limits work to 9 hours daily and 48 hours weekly, with overtime requiring consent "
            "and double wages for excess hours (limited to 50 hours quarterly). For shop/commercial establishment employees, state-specific "
            "Shops and Establishments Acts apply with similar provisions. For other employees, the employment contract terms govern overtime. "
            "If your contract requires reasonable overtime, you may be obligated to comply. However, excessive or unpaid mandatory overtime "
            "can be challenged under various labor laws or as unfair labor practice.",
        
        "Is it legal to have a non-compete clause in my contract?": 
            "In India, non-compete clauses that operate during employment are generally valid and enforceable. However, non-compete "
            "clauses that extend beyond employment (restraining employees after they leave the company) are largely unenforceable "
            "under Section 27 of the Indian Contract Act, which considers agreements in restraint of trade void. Courts have consistently "
            "ruled that post-employment non-compete clauses are against public policy as they restrict an individual's right to livelihood. "
            "Limited exceptions exist for sale of business goodwill. While employers still include such clauses, they have little legal "
            "standing unless they involve protection of confidential information or trade secrets (which are protected under separate legal provisions).",
        
        "What are my maternity leave rights in India?": 
            "Under the Maternity Benefit (Amendment) Act, 2017, women employees in establishments with 10+ employees are entitled to: "
            "1) 26 weeks of paid maternity leave for the first two children (12 weeks for third child onward), 2) 12 weeks for adoptive and "
            "commissioning mothers, 3) Work from home option after the leave period (by mutual agreement), 4) Crèche facility in establishments "
            "with 50+ employees, and 5) No termination during pregnancy/maternity leave. To qualify, you must have worked at least 80 days in the "
            "12 months preceding your expected delivery date. These benefits apply to all women employees in the organized sector, including "
            "contractual and casual workers."
    },
    
    "Family Law": {
        "What are the grounds for divorce in India?": 
            "In India, divorce grounds vary based on personal laws. Under Hindu Marriage Act: 1) Adultery, 2) Cruelty (mental/physical), "
            "3) Desertion (2+ years), 4) Conversion to another religion, 5) Mental disorder, 6) Communicable disease, 7) Renunciation of "
            "the world, 8) Presumption of death (missing 7+ years), and 9) Mutual consent. Muslim Law allows different forms including "
            "Talaq, Khula, and Mubarat. Christian law (Divorce Act) and Parsi law (Parsi Marriage and Divorce Act) have similar grounds "
            "plus additional religion-specific provisions. The Special Marriage Act applies to inter-faith marriages with grounds similar "
            "to Hindu law. Mutual consent divorce requires 6-18 months of separation depending on applicable law.",
        
        "How is property divided after divorce in India?": 
            "India doesn't have a universal community property or equal division law for divorce. Property division follows these principles: "
            "1) Self-acquired property: Each spouse retains their individually owned property acquired before or during marriage, "
            "2) Inherited property: Typically remains with the inheriting spouse, 3) Joint property: Divided based on contribution, "
            "4) Streedhan/dowry: Remains the wife's property. Courts may award maintenance/alimony to financially dependent spouses. "
            "Recent Supreme Court judgments have recognized a wife's non-financial contributions to household, sometimes granting shares "
            "in husband's property. For mutual consent divorces, couples can create their own settlement agreements. The exact division "
            "varies by personal laws (Hindu, Muslim, Christian, Parsi) and individual case circumstances.",
        
        "What is the legal process for adoption in India?": 
            "Adoption in India is governed by the Central Adoption Resource Authority (CARA) under the Hindu Adoption and Maintenance Act "
            "(for Hindus) or the Juvenile Justice Act (for all religions). The process involves: 1) Registration on CARA's portal and home study "
            "by an authorized agency, 2) Waiting for child referral based on seniority, 3) Accepting/reserving a referred child, "
            "4) Pre-adoption foster care, 5) Court filing for adoption order, and 6) Post-adoption follow-ups. Eligibility criteria include: "
            "stable marriage for couples (2+ years), age requirements (minimum 25 years; maximum age difference with child shouldn't exceed 55 years), "
            "and adequate financial means. Single individuals can also adopt with specific gender restrictions (males cannot adopt female children).",
        
        "How is child custody determined in Indian divorce cases?": 
            "Child custody in Indian divorce cases is determined based on the 'welfare of the child' principle, not parental rights. "
            "Courts consider: 1) Child's age and gender (younger children often placed with mothers), 2) Child's preferences (if old enough), "
            "3) Parents' ability to provide care, education, and stability, 4) Parents' character and behavior, 5) Continuity in education "
            "and social relationships, and 6) Maintaining sibling relationships. Indian courts typically award: a) Physical custody to one parent "
            "with visitation rights to the other, or b) Joint custody where both parents share responsibilities. Courts increasingly favor "
            "arrangements that maintain relationships with both parents unless evidence shows potential harm to the child.",
        
        "What are the legal rights of a live-in relationship in India?": 
            "Live-in relationships in India, while not explicitly regulated by legislation, have been recognized by Supreme Court rulings as legal "
            "and valid relationships between consenting adults. Legal rights include: 1) Domestic violence protection under the Protection of Women "
            "from Domestic Violence Act, 2) Maintenance rights for the woman and children (Supreme Court has held that long-term live-in relationships "
            "are 'relationship in the nature of marriage'), 3) Children born have legitimate status with inheritance rights, 4) Woman can claim maintenance "
            "under Section 125 of CrPC if the relationship was sufficiently long-term, and 5) Property acquired during the relationship may be subject to "
            "division based on contribution. However, inheritance rights for partners and certain benefits available to married couples remain limited."
    },
    
    "Criminal Law": {
        "What should I do if I'm wrongfully arrested?": 
            "If wrongfully arrested in India: 1) Remain calm and don't resist physically, 2) Ask for the grounds of arrest and demand to see "
            "the arrest warrant (if applicable), 3) Exercise your right to inform a family member/friend about your arrest, 4) Request to speak "
            "with a lawyer immediately (you have a constitutional right to legal representation), 5) Don't sign any documents without legal advice, "
            "6) Note officer names and badge numbers, 7) Remember you must be produced before a magistrate within 24 hours of arrest, "
            "8) Apply for bail at the earliest opportunity, and 9) File for habeas corpus if detained illegally. Women can only be arrested "
            "between 6 AM and 6 PM and preferably by female officers.",
        
        "How do I file an FIR (First Information Report)?": 
            "To file an FIR in India: 1) Visit the police station with jurisdiction over the crime location, 2) Provide details of the incident "
            "including time, place, persons involved, and witnesses, 3) The officer must record your complaint in writing and read it back to you, "
            "4) After verification, sign the document (get a free copy - it's your right), 5) The officer must assign an FIR number and enter it in "
            "the station diary. If police refuse to register your FIR: a) Meet the Superintendent of Police with a written complaint, b) Send your "
            "complaint by registered post to the SP, c) File a private complaint before the Judicial Magistrate under CrPC Section 156(3), or "
            "d) File a complaint on the online portal of the state police.",
        
        "What is the difference between bailable and non-bailable offenses?": 
            "In India, the key differences between bailable and non-bailable offenses are: 1) Bail grant: For bailable offenses, bail is a matter "
            "of right and must be granted by police or court; for non-bailable offenses, bail is discretionary and only courts can grant it, "
            "2) Seriousness: Bailable offenses are generally less serious (punishment typically less than 3 years) while non-bailable offenses "
            "are more serious, 3) Process: For bailable offenses, accused can secure release by executing a personal bond with/without sureties; "
            "for non-bailable offenses, courts consider factors like flight risk, evidence tampering possibility, and case severity before granting bail. "
            "The classification is listed in the First Schedule of the Criminal Procedure Code with offenses marked as 'bailable' or 'non-bailable'.",
        
        "Can a criminal case be settled outside court?": 
            "In India, certain criminal cases can be settled outside court through: 1) Compounding of offenses under Section 320 of CrPC - "
            "specific offenses listed as 'compoundable' can be settled between parties with/without court permission (e.g., certain types of assault, "
            "criminal trespass, defamation), 2) Plea bargaining under Chapter XXIA of CrPC for offenses with punishment up to 7 years (excluding "
            "offenses affecting socio-economic conditions, against women/children), 3) Settlement through Lok Adalats for compoundable offenses, "
            "or 4) Mediation for cases with civil aspects. However, serious crimes like murder, rape, terrorism, and offenses against the state "
            "cannot be settled privately. For motor accident cases, settlement typically affects only compensation, not potential criminal liability.",
        
        "What is the punishment for cybercrime in India?": 
            "Cybercrime punishments in India under the Information Technology Act include: 1) Unauthorized access/hacking (Section 66): Up to 3 years "
            "imprisonment and/or fine up to ₹5 lakh, 2) Data theft (Section 66B): Up to 3 years and/or fine up to ₹1 lakh, 3) Identity theft (Section 66C): "
            "Up to 3 years and/or fine up to ₹1 lakh, 4) Cheating by personation using computer (Section 66D): Up to 3 years and/or fine up to ₹1 lakh, "
            "5) Privacy violation (Section 66E): Up to 3 years and/or fine up to ₹2 lakh, 6) Cyber terrorism (Section 66F): Life imprisonment, "
            "7) Publishing/transmitting obscene material (Section 67): First conviction - up to 3 years and fine up to ₹5 lakh; subsequent conviction - "
            "up to 5 years and fine up to ₹10 lakh, 8) Child pornography (Section 67B): Up to 5 years and fine up to ₹10 lakh for first conviction."
    },
    
    "Business Law": {
        "How do I register a private limited company in India?": 
            "To register a private limited company in India: 1) Obtain Digital Signature Certificate (DSC) for proposed directors, "
            "2) Apply for Director Identification Number (DIN) through SPICe+ form, 3) Apply for name approval via RUN service on MCA portal "
            "(provide 2-3 name options), 4) File SPICe+ form with documents including MOA, AOA, proof of registered office, declarations, etc., "
            "5) Pay registration fees and stamp duty (varies by state and capital), 6) Receive Certificate of Incorporation with CIN and PAN, "
            "7) Apply for TAN, GST registration, professional tax registration, and open a bank account. The entire process can be completed "
            "online through the MCA portal. Typically takes 7-15 days and costs ₹5,000-₹15,000 (excluding professional fees) depending on capital.",
        
        "What are the legal requirements for starting a small business?": 
            "Legal requirements for starting a small business in India include: 1) Business structure registration (Proprietorship/Partnership/LLP/Company), "
            "2) GST registration (mandatory if turnover exceeds ₹20 lakhs, or ₹10 lakhs in special category states), 3) PAN and TAN registration, "
            "4) Shops and Establishments Act registration (from municipal corporation), 5) Professional Tax registration (state-specific), "
            "6) Industry-specific licenses (e.g., FSSAI for food, pharmacy license for medicines), 7) MSME registration (optional but beneficial), "
            "8) Labor law compliances if hiring employees (PF, ESI, etc.), 9) Trademark registration (advisable for brand protection), and "
            "10) Fire and safety NOC for physical premises. For home-based small businesses, check zoning laws in your residential area as some "
            "municipalities restrict commercial activities in residential zones.",
        
        "What taxes does a small business need to pay in India?": 
            "Small businesses in India typically need to pay: 1) Income Tax: Based on business structure - proprietors/partners at individual rates, "
            "companies at flat 25% (reduced to 15% for new manufacturing companies) plus surcharge and cess, 2) GST: 5-28% depending on goods/services "
            "(businesses with turnover under ₹40 lakhs may be exempt; those under ₹1.5 crore can opt for composition scheme with flat 1-5% rates), "
            "3) Professional Tax: State-specific (typically ₹1,000-₹2,500 annually), 4) Property Tax: On business premises (rates vary by municipality), "
            "5) TDS (Tax Deducted at Source): When making specified payments, 6) Employer contributions: PF (12% of basic salary), ESI (3.25% of gross salary) "
            "for eligible employees. Tax filing deadlines: GST returns monthly/quarterly, TDS quarterly, income tax annually (July 31 for non-audit cases, "
            "October 31 for audit cases).",
        
        "What are the key points to include in a business contract?": 
            "Key points to include in an Indian business contract: 1) Clear identification of parties with complete details (name, address, registration numbers), "
            "2) Detailed description of goods/services with specifications, quantities, and quality standards, 3) Pricing, payment terms, and currency, "
            "4) Delivery schedules, logistics, and transfer of ownership/risk, 5) Contract duration and renewal terms, 6) Performance standards and metrics, "
            "7) Representations and warranties, 8) Confidentiality and data protection clauses, 9) Intellectual property rights, 10) Termination rights and "
            "notice periods, 11) Limitation of liability and indemnification, 12) Force majeure provisions, 13) Dispute resolution mechanism (arbitration "
            "preferred for commercial disputes), 14) Governing law and jurisdiction, and 15) Signatures of authorized representatives. For international "
            "contracts, consider currency fluctuations, international shipping terms (Incoterms), and compliance with foreign laws.",
        
        "How do I protect my business idea or invention in India?": 
            "To protect your business idea or invention in India: 1) Patents: File application with Indian Patent Office for technical inventions "
            "(20-year protection; costs ₹4,000-₹15,000 for filing plus examination fees; takes 3-5 years for grant), 2) Trademarks: Register business "
            "name, logo, and slogans with Trademark Registry (10-year protection, renewable; costs ₹4,500-₹9,000 per class; takes 1-2 years), "
            "3) Copyrights: Register original creative works with Copyright Office (protection for author's life + 60 years; costs ₹500-₹2,000; "
            "takes 6-12 months), 4) Trade Secrets: Use non-disclosure agreements and confidentiality clauses with employees/partners (no registration "
            "required; protection lasts as long as secrecy is maintained), 5) Industrial Designs: Register unique product appearances with Design Registry "
            "(15-year protection; costs ₹1,000-₹4,000; takes 6-12 months). For software/apps, use a combination of copyright (for code), patent "
            "(for technical methods), and trademark (for name/logo)."
    }
}
