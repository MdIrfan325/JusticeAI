"""
Legal terms data for the JusticeAI application.
Contains definitions, examples, and Indian legal context for common legal terms.
"""

# Define categories for legal terms
TERM_CATEGORIES = [
    "Contract Law",
    "Property Law",
    "Criminal Law",
    "Consumer Law",
    "Employment Law",
    "Family Law",
    "Constitutional Law",
    "Intellectual Property"
]

# Dictionary of legal terms with definitions, examples, and Indian context
LEGAL_TERMS = {
    "Arbitration": {
        "category": "Contract Law",
        "definition": "A form of alternative dispute resolution where a neutral third party (arbitrator) reviews evidence, hears arguments, and makes a binding decision to resolve a dispute outside of court.",
        "example": "Any dispute arising out of or in connection with this contract, including any question regarding its existence, validity or termination, shall be referred to and finally resolved by arbitration under the rules of the Indian Arbitration Council, which rules are deemed to be incorporated by reference into this clause.",
        "indian_context": "In India, arbitration is governed by the Arbitration and Conciliation Act, 1996 (amended in 2015, 2019, and 2021). The amendments aim to make arbitration more efficient and reduce court intervention. Indian courts generally respect arbitration agreements and enforce arbitral awards. For domestic arbitrations, the award must be challenged within three months of receipt. India is also a signatory to the New York Convention, facilitating enforcement of foreign arbitral awards."
    },
    
    "Force Majeure": {
        "category": "Contract Law",
        "definition": "A clause that frees parties from obligation when an extraordinary event beyond their control (like natural disasters, war, riots) prevents them from fulfilling their contractual obligations.",
        "example": "Neither party shall be liable for any failure to perform its obligations under this Agreement if such failure results from circumstances beyond that party's reasonable control, including but not limited to acts of God, war, civil unrest, strike, fire, flood or other natural disaster.",
        "indian_context": "Indian courts interpret force majeure clauses strictly, requiring the event to be unforeseeable and unavoidable. The Indian Contract Act, 1872 (Section 56) recognizes the doctrine of frustration, which is related to but distinct from force majeure. During the COVID-19 pandemic, the Ministry of Finance issued an Office Memorandum clarifying that the pandemic could be considered a force majeure event for certain government contracts. For private contracts, courts assess each case based on specific contractual language and circumstances."
    },
    
    "Non-Disclosure Agreement (NDA)": {
        "category": "Contract Law",
        "definition": "A legal contract creating a confidential relationship between parties to protect sensitive information shared between them.",
        "example": "The Recipient agrees to maintain all Confidential Information in strict confidence and shall not disclose such information to any third party without prior written consent of the Disclosing Party. Recipient shall use Confidential Information solely for the purpose of evaluating a potential business relationship.",
        "indian_context": "NDAs in India are governed by the Indian Contract Act, 1872 and can be enforced through civil remedies for breach of contract. For trade secrets, there's no specific legislation in India, making NDAs crucial for protection. If violated, the affected party can seek injunctions and damages. Additionally, in certain circumstances, disclosure of confidential information may also attract criminal liability under the Indian Penal Code or Information Technology Act, 2000."
    },
    
    "Specific Performance": {
        "category": "Contract Law",
        "definition": "A court order requiring a party to perform the specific acts promised in a contract, typically used when monetary damages are inadequate compensation.",
        "example": "In the event of default, the non-defaulting party shall be entitled to specific performance of this Agreement in addition to any other remedies available at law or equity.",
        "indian_context": "Specific Performance in India is governed by the Specific Relief Act, 1963 (amended in 2018). The 2018 amendment made specific performance a general rule rather than an exception, allowing courts to more readily order specific performance instead of damages. Under Section 10, specific performance can be enforced for contracts related to immovable property, rare goods, and when monetary compensation is inadequate. However, it's not available for contracts of personal service or where constant court supervision would be required."
    },
    
    "Indemnity": {
        "category": "Contract Law",
        "definition": "A contractual obligation of one party to compensate another party for loss or damage that may occur in the future. It shifts liability from one party to another.",
        "example": "The Vendor shall indemnify, defend and hold harmless the Company from and against any and all claims, damages, liabilities, costs and expenses (including reasonable attorneys' fees) arising out of or related to any breach of this Agreement by the Vendor.",
        "indian_context": "Indemnity provisions in India are governed by Sections 124-125 of the Indian Contract Act, 1872. Indian courts generally enforce indemnity clauses, but they must be clear and unambiguous. Unlike some Western jurisdictions, Indian law doesn't recognize implied indemnities unless expressly stated. The indemnifying party's liability is limited to actual damages suffered, and courts may not enforce punitive indemnity clauses. Indemnity claims are subject to a three-year limitation period from when the right to claim arises."
    },
    
    "Caveat Emptor": {
        "category": "Consumer Law",
        "definition": "Latin for 'let the buyer beware', it's a principle that places the burden on the buyer to reasonably examine property before purchase and take responsibility for its condition.",
        "example": "The property is sold on an 'as is, where is' basis without any warranties as to its condition or fitness for purpose. The purchaser acknowledges that they have inspected the property and accept its current condition.",
        "indian_context": "In India, the principle of caveat emptor has been significantly restricted by the Consumer Protection Act, 2019, which replaced the 1986 Act. The new law expanded consumer rights and introduced concepts like product liability. Now, sellers and manufacturers can be held liable for defective products regardless of whether the buyer inspected them. For real estate, the Real Estate (Regulation and Development) Act, 2016 (RERA) further protects buyers by requiring developers to provide specific quality assurances and remedies for defects discovered within 5 years of possession."
    },
    
    "Writ Petition": {
        "category": "Constitutional Law",
        "definition": "A formal written application to a court requesting it to issue a specific writ or order directing a lower court, official, or authority to perform or refrain from performing a specific act.",
        "example": "The petitioner hereby files this writ of mandamus requesting the Honorable Court to direct the respondent Government Department to process the petitioner's license application, which has been pending for unreasonable time without any decision.",
        "indian_context": "In India, writ petitions are filed under Article 32 (Supreme Court) and Article 226 (High Courts) of the Constitution. The Indian courts recognize five types of writs: Habeas Corpus (to produce detained person), Mandamus (to compel performance of duty), Prohibition (to prevent lower court/tribunal from exceeding jurisdiction), Certiorari (to quash a decision), and Quo Warranto (to challenge a person's right to public office). Writ petitions are powerful tools for citizens to directly approach higher courts for protection of fundamental rights and ensure accountability of public officials."
    },
    
    "Public Interest Litigation (PIL)": {
        "category": "Constitutional Law",
        "definition": "A legal action initiated in a court of law for the protection of public interest, allowing any citizen or organization to approach the court seeking legal remedy in cases where public interest is at stake.",
        "example": "A PIL is filed to address the failure of municipal authorities to implement proper waste management systems, leading to health hazards and environmental degradation affecting the general public.",
        "indian_context": "PIL in India was developed by the Supreme Court in the 1980s as a procedural innovation to provide access to justice for the marginalized. Unlike traditional litigation requiring locus standi (direct interest in the matter), PILs can be filed by any public-spirited person on behalf of disadvantaged groups. Indian courts have used PILs to address issues like environmental protection, corruption, prison reforms, and human rights violations. While PILs have been transformative in Indian jurisprudence, courts have recently imposed stricter standards to prevent misuse and frivolous petitions."
    },
    
    "Anticipatory Bail": {
        "category": "Criminal Law",
        "definition": "A provision allowing a person to seek bail in anticipation of arrest on accusation of having committed a non-bailable offense.",
        "example": "The petitioner, fearing arrest in connection with FIR No. 123/2023 under Section 420 of the Indian Penal Code, hereby seeks anticipatory bail as the allegations are false and motivated by personal enmity.",
        "indian_context": "Anticipatory bail is unique to Indian legal system and is governed by Section 438 of the Criminal Procedure Code. It allows individuals to seek protection from arrest before it happens. The Supreme Court in Siddharam Satlingappa Mhetre v. State of Maharashtra (2011) held that anticipatory bail should not be limited by time and can continue until the trial ends. However, courts can impose conditions like cooperation with investigation, not leaving the country, etc. Recently, the Criminal Procedure (Identification) Act, 2022 has introduced provisions that may affect anticipatory bail applications."
    },
    
    "Maintenance": {
        "category": "Family Law",
        "definition": "Financial support that a person is legally obligated to provide for their spouse, ex-spouse, children, or other dependents after separation or divorce.",
        "example": "The respondent is directed to pay monthly maintenance of ₹15,000 to the petitioner and ₹10,000 for the minor child's education and upbringing, to be deposited in the petitioner's bank account by the 7th of each month.",
        "indian_context": "In India, maintenance laws vary by personal laws and secular provisions. Under Section 125 of Criminal Procedure Code (applicable to all religions), wives, minor children, and parents can claim maintenance. Under Hindu laws, the Hindu Adoption and Maintenance Act provides additional rights. For Muslims, maintenance (nafaqa) is governed by Muslim Women (Protection of Rights on Divorce) Act, 1986 and recent judicial interpretations. The Supreme Court in Rajnesh vs. Neha (2020) issued comprehensive guidelines for maintenance cases, including interim maintenance, criteria for determining amount, and enforcement mechanisms."
    },
    
    "Retrenchment": {
        "category": "Employment Law",
        "definition": "Termination of employment of a worker for any reason other than punishment imposed by disciplinary action. It generally refers to workforce reduction due to economic, technological or structural changes.",
        "example": "Due to the economic downturn and restructuring of operations, the Company regretfully announces retrenchment of 50 employees from the manufacturing division with effect from July 1, 2023, in accordance with applicable labor laws.",
        "indian_context": "In India, retrenchment is governed by the Industrial Disputes Act, 1947. For establishments with 100+ workers (50+ in some states after labor code amendments), employer must obtain government permission before retrenchment. The law requires: one month's notice or pay in lieu; severance compensation of 15 days' wages for each completed year of service; government notification; and following 'last come, first go' principle, where junior employees must be retrenched first. Retrenched workers also have preferential right to re-employment if the employer rehires. Non-compliance can result in reinstatement with back wages."
    },
    
    "Lok Adalat": {
        "category": "Constitutional Law",
        "definition": "A forum where disputes pending in court or at pre-litigation stage are settled amicably. Literally means 'People's Court' and is based on Gandhian principles of settlement of disputes through mediation.",
        "example": "The motor accident claim filed by the victim's family was resolved in the Lok Adalat where the insurance company agreed to pay ₹8 lakhs as compensation, avoiding years of litigation.",
        "indian_context": "Lok Adalats are established under the Legal Services Authorities Act, 1987 to provide free and competent legal services to weaker sections and to organize lok adalats for amicable settlement of disputes. They are presided over by a sitting or retired judicial officer and two other members with legal training. Lok Adalat decisions are binding and have the same status as court decrees, with no appeal possible. They handle various cases including motor accident claims, family disputes, bank recovery, and petty criminal cases. In 2021-22, over 1.27 crore cases were settled through Lok Adalats across India."
    },
    
    "Easement": {
        "category": "Property Law",
        "definition": "A right to use another person's land for a specific purpose, such as a pathway or to access utilities, without possessing it.",
        "example": "The owner of Plot A grants an easement to the owner of Plot B to use the driveway on Plot A to access the main road, as Plot B has no direct road access.",
        "indian_context": "Easements in India are governed by the Indian Easements Act, 1882. The law recognizes several types of easements: by grant (express or implied), by prescription (continuous use for 20 years), by necessity, and by custom. Easement by prescription is common in India, especially in older neighborhoods and rural areas where pathways have been used for generations. Recent Supreme Court judgments like Amrinder Singh v. Rajinder Kaur (2021) have clarified that easement rights must be specific and cannot be expanded beyond their original scope. Easements are particularly important in India due to high population density and joint family property divisions."
    },
    
    "Stamp Duty": {
        "category": "Property Law",
        "definition": "A tax imposed on legal documents to make them legally valid and admissible in court as evidence.",
        "example": "For a property valued at ₹50 lakhs in Mumbai, a stamp duty of 5% (₹2.5 lakhs) must be paid to the state government at the time of registration of the sale deed.",
        "indian_context": "Stamp duty in India is governed by the Indian Stamp Act, 1899, with rates determined by state-specific stamp acts. Rates vary significantly across states - from 3% to 8% for property transactions. In addition to property transfers, stamp duty applies to partnership deeds, loan agreements, power of attorney, and various commercial contracts. Inadequately stamped documents are inadmissible as evidence in court. Some states offer stamp duty concessions for women property buyers to promote women's property ownership. During COVID-19, several states temporarily reduced stamp duty rates to boost real estate transactions."
    },
    
    "Khata": {
        "category": "Property Law",
        "definition": "A record of property ownership and tax assessment maintained by municipal authorities. It contains details of the property, its size, location, and the person responsible for paying property tax.",
        "example": "Before purchasing the apartment, the buyer verified that the property had a clear Khata certificate showing no outstanding property tax dues and confirming the property dimensions matched with approved plans.",
        "indian_context": "Khata is particularly important in South Indian states like Karnataka, Tamil Nadu, and Andhra Pradesh. In Bangalore, it's issued by the Bruhat Bengaluru Mahanagara Palike (BBMP). While not a title document, Khata is essential for municipal services, obtaining utilities, and property tax payments. Two types exist: A Khata (for properties with approved building plans) and B Khata (for properties with plan violations or in unauthorized layouts). Recent digitization efforts have made Khata transfers and management more accessible online. A property without proper Khata faces difficulties in obtaining loans and may involve higher tax liabilities."
    },
    
    "Copyright": {
        "category": "Intellectual Property",
        "definition": "A legal right that grants the creator of an original work exclusive rights to determine whether and under what conditions their original work may be copied and used by others.",
        "example": "© 2023 Author Name. All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form without the prior written permission of the publisher.",
        "indian_context": "Copyright in India is governed by the Copyright Act, 1957 (amended several times, most significantly in 2012). Protection lasts for the author's lifetime plus 60 years after death. The 2012 amendment strengthened digital rights, introduced statutory licensing for cover versions, and improved rights of performers. India follows the principle of automatic protection - registration is not mandatory but provides evidentiary advantage. The Copyright Board handles licensing disputes and compulsory licensing. India is a signatory to major international copyright conventions including the Berne Convention, TRIPS Agreement, and WIPO Copyright Treaty, ensuring protection of Indian works internationally."
    },
    
    "Patent": {
        "category": "Intellectual Property",
        "definition": "A government-granted exclusive right to an inventor to prevent others from making, using, selling, or importing an invention for a limited period in exchange for detailed public disclosure of the invention.",
        "example": "The pharmaceutical company was granted a patent for its novel drug formulation, giving it exclusive rights to manufacture and sell the medication in India for 20 years from the date of filing the patent application.",
        "indian_context": "Patents in India are governed by the Patents Act, 1970 (amended in 2005 to comply with TRIPS). India grants 20-year patent protection from filing date. India's patent law includes Section 3(d), a unique provision preventing 'evergreening' by requiring enhanced efficacy for derivatives of known substances to be patentable. This provision was upheld in the landmark Novartis case (2013). India also has robust compulsory licensing provisions for public health emergencies, used in the Bayer-Natco case (2012). Pre-grant and post-grant opposition procedures allow third parties to challenge patents, making India's patent examination more rigorous than many other jurisdictions."
    },
    
    "Trademark": {
        "category": "Intellectual Property",
        "definition": "A recognizable sign, design, or expression that identifies products or services from a particular source and distinguishes them from others.",
        "example": "The beverage company has registered its distinctive logo and brand name as trademarks, allowing it to take legal action against any unauthorized use of similar marks that might confuse consumers.",
        "indian_context": "Trademarks in India are governed by the Trade Marks Act, 1999. Registration provides 10-year protection, renewable indefinitely. India follows a 'first to use' rather than 'first to file' system, meaning prior use can trump registration. The Well-Known Marks Registry provides special protection to famous brands. Recent amendments to trademark rules in 2017 streamlined the application process, reduced forms from 74 to 8, and introduced video conferencing for hearings. India uses the Nice Classification system with 45 classes. Criminal remedies are available for trademark counterfeiting under the Act, with penalties including imprisonment up to 3 years and fines."
    },
    
    "Bail": {
        "category": "Criminal Law",
        "definition": "Temporary release of an accused person awaiting trial, sometimes on the condition that a sum of money is lodged to guarantee their appearance in court.",
        "example": "The accused was granted bail on the condition of surrendering his passport, reporting to the police station weekly, and providing a personal bond of ₹50,000 with two sureties of like amount.",
        "indian_context": "Bail provisions in India are governed by Sections 436-450 of the Criminal Procedure Code. Indian courts classify offenses as bailable (where bail is a right) and non-bailable (where bail is discretionary). For non-bailable offenses, factors considered include nature of accusation, severity of punishment, evidence strength, and flight risk. The Supreme Court in Arnab Goswami v. State of Maharashtra (2020) emphasized that liberty should be the rule and detention the exception. The principle of 'bail not jail' has been reinforced in multiple judgments, though in practice, undertrial detention remains common. Recent amendments aim to streamline bail proceedings, particularly for economically disadvantaged defendants."
    },
    
    "Garnishee Order": {
        "category": "Contract Law",
        "definition": "A legal procedure where a creditor can collect what a debtor owes by directly accessing the debtor's property (often bank accounts or wages) that is held by a third party.",
        "example": "The court issued a garnishee order directing the employer to deduct 20% of the judgment debtor's monthly salary and remit it directly to the decree holder until the decreed amount is fully satisfied.",
        "indian_context": "In India, garnishee orders are governed by Order 21, Rules 46-46I of the Civil Procedure Code. They are a method of executing money decrees where the court directs a third party (garnishee) who owes money to the judgment debtor to pay directly to the decree holder. The procedure involves two stages: a garnishee notice (nisi order) and a final order after hearing the garnishee. Certain funds are exempt from garnishment, including provident fund, pension, and gratuity. Banks are common garnishees, and must disclose all accounts of the judgment debtor. Salary garnishment in India typically cannot exceed one-third of the employee's monthly wages."
    },
    
    "Gift Deed": {
        "category": "Property Law",
        "definition": "A legal document used to voluntarily transfer ownership of property from one person (donor) to another (donee) without any consideration or payment.",
        "example": "The mother executed a gift deed transferring her ancestral house to her daughter, specifying that the transfer is made out of natural love and affection, without any monetary consideration.",
        "indian_context": "Gift deeds in India are governed by the Transfer of Property Act, 1882 for non-Muslims and by personal laws for Muslims. For a valid gift, there must be a clear intention to give, acceptance by the donee, and transfer of possession. Gift deeds must be registered when involving immovable property valued above ₹100. They attract stamp duty (rates vary by state) and registration fees. Under Hindu law, ancestral property can be gifted with certain restrictions. Under Muslim law, gifts (Hiba) have specific rules regarding possession and quantum. Gift deeds are commonly used for tax planning and succession planning in India, though tax laws have been amended to limit tax avoidance through gifts."
    },
    
    "Doctrine of Laches": {
        "category": "Constitutional Law",
        "definition": "A legal principle that a legal right or claim will not be enforced or allowed if a long delay in asserting the right has prejudiced the adverse party. It's based on the maxim 'equity aids the vigilant, not those who slumber on their rights.'",
        "example": "The plaintiff's claim for specific performance of a 15-year-old agreement was dismissed by the court applying the doctrine of laches, as the plaintiff had inexplicably delayed enforcing their rights, causing prejudice to the defendant who had made alternative arrangements.",
        "indian_context": "In India, the doctrine of laches is an equitable principle applied by courts even when claims are filed within the statutory limitation period. The Supreme Court in Poysha Govindbhai Parshottambhai v. State of Gujarat (2021) held that delay and laches can be grounds for dismissing even constitutional remedies like writ petitions. However, in public interest matters, courts are more flexible. Factors considered include length of delay, reasons for delay, and prejudice caused. Indian courts distinguish between latches (delay in filing) and acquiescence (implied consent through inaction). This doctrine is particularly important in property disputes, specific performance cases, and administrative law where delays are common."
    },
    
    "Promissory Estoppel": {
        "category": "Contract Law",
        "definition": "A legal principle that prevents a party from acting in a certain way because they previously said they would not, and another party relied on that promise.",
        "example": "The government promised tax incentives to industries setting up in a backward area, based on which the company invested heavily. When the government later revoked the incentives, the court applied promissory estoppel to prevent the revocation for existing investors.",
        "indian_context": "Promissory estoppel in India has evolved significantly through judicial precedents, starting with the landmark case of Motilal Padampat Sugar Mills v. State of Uttar Pradesh (1979). Unlike some jurisdictions, Indian courts apply this doctrine even without consideration. It has been particularly significant in cases against the government, holding that the government cannot renege on its promises on which parties have relied, though courts recognize exceptions for public interest and legislative policy changes. The doctrine transcends traditional contract requirements, providing equitable relief even when formal contract elements are missing. Recent judgments have extended its application to commercial relationships, representations in tenders, and policy assurances."
    },
    
    "Liquidated Damages": {
        "category": "Contract Law",
        "definition": "A specific sum designated in a contract as the amount of damages to be paid in case of breach, agreed upon by the parties at the time of contract formation.",
        "example": "As per clause 15 of the construction contract, if the contractor fails to complete the project by the specified date, liquidated damages of ₹50,000 per day of delay shall be payable, not as a penalty but as a genuine pre-estimate of loss.",
        "indian_context": "In India, liquidated damages are governed by Section 74 of the Indian Contract Act, 1872. Unlike English law, Indian law makes no distinction between liquidated damages and penalty clauses - both are enforceable if reasonable. The Supreme Court in Kailash Nath Associates v. DDA (2015) clarified that actual loss must be proven even for liquidated damages claims, though the pre-estimated sum serves as the upper limit. Courts may reduce excessive liquidated damages, particularly in government contracts. In construction and infrastructure contracts, the standard liquidated damages rate is typically 0.5% to 1% of contract value per week of delay, usually capped at 5-10% of total contract value."
    },
    
    "Partition Deed": {
        "category": "Property Law",
        "definition": "A legal document that divides joint family property or co-owned property among the rightful owners/heirs, specifying each person's share.",
        "example": "Following the father's death, the three siblings executed a partition deed dividing the ancestral property, with the agricultural land divided equally, the main house going to the eldest son who paid equalization payment to others, and the commercial property divided in 40:30:30 ratio.",
        "indian_context": "Partition deeds in India are governed by personal laws and the Transfer of Property Act. For Hindus, the Hindu Succession Act governs rights in ancestral and joint family property. Family settlement/partition deeds must be registered when involving immovable property shares and attract stamp duty (rates vary by state). Notably, after the 2005 amendment to the Hindu Succession Act, daughters have equal coparcenary rights in ancestral property as sons. Income tax implications include capital gains tax exemption on transfers via partition of Hindu Undivided Family assets. Recent court rulings emphasize that oral partitions, though legally valid, are difficult to enforce without documentary evidence in case of disputes."
    },
    
    "Injunction": {
        "category": "Constitutional Law",
        "definition": "A court order requiring a person to do or cease doing a specific action.",
        "example": "The court granted a temporary injunction restraining the defendant from constructing any structure on the disputed property until the final disposal of the title suit.",
        "indian_context": "Injunctions in India are governed by Sections 36-42 of the Specific Relief Act, 1963 and Order 39 of the Civil Procedure Code. Indian courts recognize three types: temporary/interim (during proceedings), perpetual (final decision), and mandatory (requiring positive action). For granting an injunction, courts apply the three-pronged test: prima facie case, irreparable injury, and balance of convenience. In intellectual property cases, India has adopted the concept of 'dynamic injunctions' allowing blocking of mirror/redirect websites. In property disputes, which form the largest category of injunction cases in India, courts are increasingly requiring security deposits from plaintiffs to prevent frivolous injunction requests and compensate defendants for delays."
    },
    
    "Divorce by Mutual Consent": {
        "category": "Family Law",
        "definition": "A procedure where both spouses agree to dissolve their marriage amicably by mutual agreement without attributing fault to either party.",
        "example": "After living separately for over a year and determining that their marriage could not be salvaged, the couple filed a joint petition for divorce by mutual consent, agreeing on alimony, child custody, and property division terms.",
        "indian_context": "Divorce by mutual consent in India varies by personal law. Under the Hindu Marriage Act and Special Marriage Act, couples must show they've lived separately for at least one year, file a joint petition, and appear in court twice - once for filing and again after 6 months (but before 18 months) for the final decree. The 6-month waiting period can be waived by the Supreme Court as held in Amardeep Singh v. Harveen Kaur (2017). For Christians, the Indian Divorce Act requires one-year separation. For Muslims, mutual divorce is available through Khula or Mubarat. Courts prioritize mutual consent divorces, often concluding them in 6-8 months. Comprehensive settlement agreements covering maintenance, child custody, and property division typically accompany such divorces."
    },
    
    "Probate": {
        "category": "Family Law",
        "definition": "A legal process where a court validates a will and grants the right to the executor to administer the deceased person's estate according to the will's provisions.",
        "example": "After the testator's death, the executor named in the will applied for probate, submitting the original will and death certificate to the court, which then verified the will's authenticity before granting probate.",
        "indian_context": "In India, probate is governed by the Indian Succession Act, 1925. Probate is mandatory for wills in the presidency towns (Kolkata, Mumbai, Chennai) and for immovable property in these areas. In other regions, probate is optional but advisable for execution certainty. The process involves filing a petition with the High Court or District Court with jurisdiction, publishing a citation in a newspaper inviting objections, and court examination of the will's execution. Probate carries evidentiary value - it conclusively establishes the will's validity. Court fees for probate are value-based (percentage of estate) and can be substantial. The process typically takes 6-18 months, though contested probates can take years to resolve."
    },
    
    "Defamation": {
        "category": "Criminal Law",
        "definition": "Communication of a false statement that harms the reputation of an individual, business, product, group, government, or nation.",
        "example": "The newspaper published an article falsely claiming the businessman had engaged in tax fraud, leading him to file a defamation case seeking damages for harm to his personal and professional reputation.",
        "indian_context": "India has both civil and criminal defamation laws. Civil defamation is based on tort law, allowing victims to claim damages. Criminal defamation under Sections 499-502 of Indian Penal Code carries punishment up to 2 years imprisonment. In 2016, the Supreme Court upheld the constitutionality of criminal defamation in Subramanian Swamy v. Union of India, though it remains controversial. Truth is a defense only if publication was for public good. Special protection exists for statements about public conduct of public servants. Recent judgments have emphasized balancing reputation rights with free speech, particularly for journalists and public interest matters. For online defamation, both IT Act provisions and traditional defamation laws apply."
    },
    
    "Right to Information (RTI)": {
        "category": "Constitutional Law",
        "definition": "A legal right allowing citizens to request access to information held by public authorities, subject to certain exceptions.",
        "example": "The activist filed an RTI application requesting details of government spending on a public infrastructure project, including copies of contracts, payments made, and progress reports.",
        "indian_context": "The Right to Information Act, 2005 covers all constitutional authorities and substantially government-funded NGOs. Applications require minimal fee (usually ₹10) with responses mandated within 30 days. Information exempt from disclosure includes national security, commercial confidence, cabinet papers, and personal information with no public interest. The implementation structure includes Public Information Officers at organization level, first appeals within the organization, and second appeals to independent Information Commissions at state and central levels. Despite challenges including backlog of appeals and increasing denial rates, RTI has transformed governance by exposing corruption and improving transparency in public administration. Recent amendments in 2019 changed Information Commissioners' tenure and appointment terms, raising concerns about independence."
    },
    
    "Will": {
        "category": "Family Law",
        "definition": "A legal document expressing a person's wishes regarding the distribution of their property and the care of any minor children after death.",
        "example": "In her will, she bequeathed her residential property to her daughter, financial investments to her son, and established a trust for her grandchildren's education, while appointing her brother as the executor of the estate.",
        "indian_context": "Wills in India are governed by personal laws and the Indian Succession Act, 1925. For valid wills: the testator must be of sound mind and not a minor, the will must be signed by the testator and attested by two witnesses, and it should be made voluntarily without coercion. Registration of wills is optional but recommended. Under Hindu law (applicable to Buddhists, Jains, Sikhs), there are no restrictions on bequeathing property. Under Muslim law, testamentary freedom is limited to 1/3rd of the estate, with the remainder following Islamic inheritance laws. Courts scrutinize wills that disinherit natural heirs or contain unusual provisions. Recent judgments emphasize that handwritten, unregistered wills are valid if execution requirements are met, though they invite greater judicial scrutiny."
    }
}
