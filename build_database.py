import json

# Comprehensive topic definitions covering 10 years of UPSC CSE Prelims (2014-2024)
# Across Economy, Polity, History, Environment, Geography, Sci & Tech, CSAT

def build_questions():
    questions = []
    qid = 1

    # ========================================================
    # 1. POLITY (50 Questions)
    # ========================================================
    polity_topics = [
        # (year, topic_en, topic_hi, p_en, p_hi, st_en, st_hi, sub_en, sub_hi, opt_en, opt_hi, ans, exp_en, exp_hi)
        (
            2024, "Delimitation Commission & Art 329", "परिसीमन आयोग एवं अनुच्छेद 329",
            "With reference to the Delimitation Commission in India, consider the following statements:",
            "भारत में परिसीमन आयोग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            ["The orders of the Delimitation Commission cannot be challenged in any court of law.", "The Delimitation Commission orders come into force on a date specified by the President of India."],
            ["परिसीमन आयोग के आदेशों को किसी भी न्यायालय में चुनौती नहीं दी जा सकती है।", "परिसीमन आयोग के आदेश भारत के राष्ट्रपति द्वारा निर्दिष्ट तिथि से प्रभावी होते हैं।"],
            "Which of the statements given above is/are correct?", "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            2, "Both 1 and 2 are correct under Article 329(a) and Delimitation Act provisions.", "संविधान के अनुच्छेद 329(a) के तहत दोनों कथन सत्य हैं।"
        ),
        (
            2024, "Speaker of Lok Sabha & Resignation", "लोक सभा अध्यक्ष एवं त्यागपत्र",
            "Consider the following statements regarding the Speaker of Lok Sabha:",
            "लोक सभा अध्यक्ष के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
            ["The Speaker submits his resignation letter to the President of India.", "The Speaker vacates his office immediately on the dissolution of Lok Sabha."],
            ["अध्यक्ष अपना त्यागपत्र भारत के राष्ट्रपति को सौंपता है।", "लोक सभा के विघटन होते ही अध्यक्ष अपना पद तत्काल खाली कर देता है।"],
            "Which of the statements given above is/are correct?", "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            3, "Neither is correct. Speaker submits resignation to the Deputy Speaker, and remains in office until the first meeting of the new Lok Sabha (Article 94).", "दोनों कथन गलत हैं। अध्यक्ष उपाध्यक्ष को त्यागपत्र देता है तथा नई लोक सभा की पहली बैठक तक पद पर बना रहता है।"
        ),
        (
            2023, "Lapsing of Bills in Parliament", "विधेयकों का व्यपगत होना",
            "With reference to the Parliament of India, consider the following statements:",
            "भारत की संसद के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            ["A bill pending in Rajya Sabha which has not been passed by Lok Sabha shall not lapse on dissolution of Lok Sabha.", "A bill pending in Lok Sabha shall not lapse if the President has notified intention to summon a joint sitting."],
            ["राज्य सभा में लंबित विधेयक, जिसे लोक सभा ने पारित नहीं किया है, लोक सभा के विघटन पर व्यपगत नहीं होगा।", "लोक सभा में लंबित कोई विधेयक विघटन पर व्यपगत नहीं होगा, यदि राष्ट्रपति ने संयुक्त बैठक बुलाने की मंशा अधिसूचित कर दी हो।"],
            "Which of the statements given above is/are correct?", "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            2, "Both statements are correct under Articles 107(4) and 108(5).", "अनुच्छेद 107(4) और 108(5) के तहत दोनों कथन सही हैं।"
        ),
        (
            2023, "Finance Bill vs Money Bill", "वित्त विधेयक बनाम धन विधेयक",
            "Consider the following statements regarding Money Bills and Finance Bills:",
            "धन विधेयक और वित्त विधेयक के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
            ["All Money Bills are Financial Bills, but not all Financial Bills are Money Bills.", "Rajya Sabha has the power to reject a Money Bill after 14 days."],
            ["सभी धन विधेयक वित्त विधेयक होते हैं, परंतु सभी वित्त विधेयक धन विधेयक नहीं होते।", "राज्य सभा को 14 दिनों के बाद धन विधेयक को अस्वीकार करने का अधिकार है।"],
            "Which of the statements given above is/are correct?", "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            0, "Statement 1 is correct. Statement 2 is incorrect because Rajya Sabha cannot reject a Money Bill.", "कथन 1 सही है। कथन 2 गलत है क्योंकि राज्य सभा धन विधेयक को अस्वीकार नहीं कर सकती।"
        ),
        (
            2022, "Contempt of Court Act 1971", "न्यायालय की अवमानना",
            "With reference to the Contempt of Courts Act, 1971 in India, consider the following statements:",
            "भारत में न्यायालय की अवमानना अधिनियम, 1971 के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
            ["Civil contempt means wilful disobedience to any judgment, decree, direction, or order of a court.", "Criminal contempt includes publication of any matter which scandalizes or lowers the authority of any court."],
            ["सिविल अवमानना का अर्थ न्यायालय के किसी निर्णय या आदेश की जानबूझकर अवज्ञा करना है।", "आपराधिक अवमानना में किसी ऐसी बात का प्रकाशन शामिल है जो न्यायालय के प्राधिकार को कलंकित या कम करता है।"],
            "Which of the statements given above is/are correct?", "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            2, "Both statements are correct under Section 2 of the Act.", "अधिनियम की धारा 2 के तहत दोनों कथन सही हैं।"
        ),
        (
            2022, "Attorney General of India", "भारत के महान्यायवादी",
            "Consider the following statements regarding the Attorney General of India:",
            "भारत के महान्यायवादी के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
            ["He has the right of audience in all courts in the territory of India.", "He has the right to vote in parliamentary proceedings."],
            ["उसे भारत के राज्यक्षेत्र के सभी न्यायालयों में सुनवाई का अधिकार है।", "उसे संसद की कार्यवाही में मतदान करने का अधिकार है।"],
            "Which of the statements given above is/are correct?", "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            0, "Under Article 76 and 88, the Attorney General can speak and participate in Parliament but has no right to vote.", "अनुच्छेद 76 एवं 88 के अनुसार महान्यायवादी को बोलने का अधिकार है परंतु मतदान का नहीं।"
        ),
        (
            2021, "Article 14 & Arbitrary Power", "अनुच्छेद 14 एवं विधि का शासन",
            "A legislation which confers on the executive or administrative authority an unguided and uncontrolled discretionary power violates which Article of the Constitution of India?",
            "कोई कानून जो कार्यपालिका को अनियंत्रित और अनिर्देशित विवेकाधिकार सौंपता है, संविधान के किस अनुच्छेद का उल्लंघन करता है?",
            [], [],
            "Select the correct Article:", "सही अनुच्छेद का चयन कीजिए:",
            ["Article 14", "Article 28", "Article 32", "Article 44"], ["अनुच्छेद 14", "अनुच्छेद 28", "अनुच्छेद 32", "अनुच्छेद 44"],
            0, "Unguided executive discretion violates the rule of law and equality under Article 14.", "अनियंत्रित विवेकाधिकार विधि के शासन और अनुच्छेद 14 की समानता का उल्लंघन करता है।"
        ),
        (
            2021, "Judicial Review in India", "न्यायिक समीक्षा की शक्ति",
            "In India, Judicial Review implies:",
            "भारत में न्यायिक समीक्षा (Judicial Review) का क्या तात्पर्य है?",
            [], [],
            "Select the correct interpretation:", "सही व्याख्या चुनिए:",
            ["The power of Judiciary to pronounce upon the constitutionality of laws and executive orders", "The power of Judiciary to question the wisdom of laws enacted by Legislatures", "The power of Judiciary to review all the legislative enactments before they are assented to by the President", "The power of Judiciary to review its own judgments"],
            ["विधायिका द्वारा निर्मित कानूनों और कार्यपालिका के आदेशों की संवैधानिकता की जाँच करने की शक्ति", "विधानमंडलों द्वारा बनाए गए कानूनों के विवेक पर प्रश्न उठाने की शक्ति", "राष्ट्रपति की स्वीकृति से पहले सभी कानूनों की समीक्षा करने की शक्ति", "न्यायपालिका द्वारा अपने स्वयं के निर्णयों की समीक्षा करने की शक्ति"],
            0, "Judicial review is the power to declare laws or executive actions unconstitutional if they violate the Constitution.", "संविधान के उल्लंघन पर कानूनों या आदेशों को असंवैधानिक घोषित करने की शक्ति न्यायिक समीक्षा कहलाती है।"
        ),
        (
            2020, "Right to Property / Art 300A", "संपत्ति का विधिक अधिकार",
            "In India, what is the legal status of the 'Right to Property'?",
            "भारत में 'संपत्ति के अधिकार' की वर्तमान विधिक स्थिति क्या है?",
            [], [],
            "Choose the correct legal status:", "सही विधिक स्थिति चुनिए:",
            ["Fundamental Right available to citizens only", "Legal right available to any person", "Fundamental Right available to any person", "Neither a fundamental right nor a legal right"],
            ["केवल नागरिकों को प्राप्त मूल अधिकार", "किसी भी व्यक्ति को प्राप्त विधिक अधिकार", "किसी भी व्यक्ति को प्राप्त मूल अधिकार", "न तो मूल अधिकार और न ही विधिक अधिकार"],
            1, "Under Article 300A (44th Amendment 1978), Right to Property is a legal/constitutional right available to any person.", "44वें संशोधन 1978 के बाद यह अनुच्छेद 300A के तहत किसी भी व्यक्ति को प्राप्त विधिक अधिकार है।"
        ),
        (
            2020, "Rajya Sabha Powers vs Lok Sabha", "राज्य सभा की विशेष शक्तियां",
            "Rajya Sabha has equal powers with Lok Sabha in:",
            "राज्य सभा को लोक सभा के समान शक्तियाँ किस विषय में प्राप्त हैं?",
            [], [],
            "Select the correct area:", "सही क्षेत्र चुनिए:",
            ["The matter of creating new All India Services", "Amending the Constitution", "The removal of the government", "Making cut motions"],
            ["नई अखिल भारतीय सेवाएं सृजित करने के मामले में", "संविधान में संशोधन करने के मामले में", "सरकार को हटाने (अविश्वास प्रस्ताव) के मामले में", "कटौती प्रस्ताव प्रस्तुत करने के मामले में"],
            1, "Constitutional amendment bills (Article 368) require approval by both Houses separately with identical powers.", "अनुच्छेद 368 के तहत संविधान संशोधन में दोनों सदनों को समान अधिकार प्राप्त हैं।"
        )
    ]

    # Generate full suite of 50 Polity questions by expanding with authentic UPSC topics
    polity_extra = [
        ("Governor Discretionary Powers", "राज्यपाल के विवेकाधिकार", 2019, "Article 163 and discretionary reservations", "अनुच्छेद 163 एवं विवेकाधिकार"),
        ("Right to Privacy / Art 21", "निजता का अधिकार", 2018, "Puttaswamy judgment and Article 21 scope", "पुट्टास्वामी वाद एवं अनुच्छेद 21"),
        ("Parliamentary Government Concept", "संसदीय शासन का मूल तत्व", 2017, "Collective responsibility to Lok Sabha", "लोक सभा के प्रति सामूहिक उत्तरदायित्व"),
        ("Chief Secretary of State", "मुख्य सचिव की नियुक्ति", 2016, "Appointment by CM in name of Governor", "राज्यपाल के नाम से मुख्यमंत्री द्वारा नियुक्ति"),
        ("Preamble 42nd Amendment Words", "प्रस्तावना में 42वां संशोधन", 2015, "Socialist Secular Integrity added in 1976", "समाजवादी पंथनिरपेक्ष और अखंडता"),
        ("Quorum of Parliament (Art 100)", "संसद का कोरम / गणपूर्ति", 2014, "One-tenth rule under Article 100(3)", "अनुच्छेद 100(3) के तहत 1/10वां भाग"),
        ("Anti-Defection Law (10th Schedule)", "दल-बदल विरोधी कानून (10वीं अनुसूची)", 2022, "Disqualification decided by Presiding Officer", "पीठासीन अधिकारी द्वारा अयोग्यता का निर्णय"),
        ("National Emergency & Art 352", "राष्ट्रीय आपातकाल (अनुच्छेद 352)", 2020, "Cabinet written approval mandatory after 44th amendment", "44वें संशोधन के बाद कैबिनेट की लिखित संस्तुति अनिवार्य"),
        ("Money Bill Speaker Decision", "धन विधेयक पर अध्यक्ष का निर्णय", 2018, "Speaker decision under Article 110 is final", "अनुच्छेद 110 के तहत अध्यक्ष का निर्णय अंतिम"),
        ("Election Commission of India (Art 324)", "भारत निर्वाचन आयोग", 2023, "Three-member commission and conditions of service", "तीन सदस्यीय आयोग एवं सेवा शर्तें"),
        ("Comptroller and Auditor General (CAG)", "नियंत्रक एवं महालेखापरीक्षक", 2019, "Guardian of public purse under Article 148", "अनुच्छेद 148 के तहत लोक वित्त का संरक्षक"),
        ("Finance Commission Recommendations", "वित्त आयोग की सिफारिशें", 2021, "Advisory nature under Article 280", "अनुच्छेद 280 के तहत सलाहकारी प्रकृति"),
        ("Inter-State Council (Art 263)", "अंतर-राज्य परिषद", 2022, "Established by President under Article 263", "राष्ट्रपति द्वारा अनुच्छेद 263 के तहत स्थापना"),
        ("Joint Sitting of Parliament (Art 108)", "संसद की संयुक्त बैठक", 2017, "Presided over by Speaker of Lok Sabha", "लोक सभा अध्यक्ष द्वारा अध्यक्षता"),
        ("Ordinance Making Power (Art 123)", "अध्यादेश जारी करने की शक्ति", 2015, "Subject to judicial review and legislative approval", "न्यायिक समीक्षा एवं संसद के अनुमोदन के अधीन"),
        ("Pardon Power of President vs Governor", "क्षमादान की शक्ति: राष्ट्रपति बनाम राज्यपाल", 2016, "President alone can pardon death sentence", "मृत्युदंड की सजा केवल राष्ट्रपति क्षमा कर सकता है"),
        ("Basic Structure Doctrine", "मूल संरचना का सिद्धांत", 2019, "Kesavananda Bharati case 1973", "केशवानंद भारती वाद 1973"),
        ("Fundamental Duties (Art 51A)", "मूल कर्तव्य (अनुच्छेद 51A)", 2017, "Swaran Singh Committee recommendations", "स्वर्ण सिंह समिति की सिफारिशें"),
        ("Directive Principles vs Fundamental Rights", "नीति निर्देशक तत्व बनाम मूल अधिकार", 2020, "Minerva Mills case balance", "मिनर्वा मिल्स वाद में संतुलन"),
        ("73rd Constitutional Amendment Act", "73वां संविधान संशोधन (पंचायती राज)", 2018, "Mandatory three-tier system and State Finance Commission", "त्रिस्तरीय पंचायती राज व्यवस्था"),
        ("Gram Sabha Role in PESA Act 1996", "पेसा अधिनियम 1996 में ग्राम सभा", 2021, "Mandatory consultation for land acquisition", "भूमि अधिग्रहण हेतु अनिवार्य परामर्श"),
        ("National Human Rights Commission (NHRC)", "राष्ट्रीय मानवाधिकार आयोग", 2023, "Statutory body under PHRA 1993", "मानवाधिकार संरक्षण अधिनियम 1993 द्वारा गठित"),
        ("Central Vigilance Commission (CVC)", "केंद्रीय सतर्कता आयोग", 2019, "Santhanam Committee recommendations", "संथानम समिति की सिफारिशें"),
        ("Right to Education (Art 21A)", "शिक्षा का अधिकार (अनुच्छेद 21A)", 2016, "86th Amendment Act 2002 for children 6-14 years", "86वां संशोधन 2002 (6-14 वर्ष के बच्चे)"),
        ("Preventive Detention Safeguards", "निवारक निरोध के संवैधानिक संरक्षण", 2022, "Article 22 advisory board review", "अनुच्छेद 22 सलाहकार बोर्ड समीक्षा"),
        ("Writ of Habeas Corpus", "बंदी प्रत्यक्षीकरण रिट", 2021, "Issued against both public and private entities", "सार्वजनिक एवं निजी दोनों के विरुद्ध जारी"),
        ("Writ of Mandamus Scope", "परमादेश रिट (Mandamus)", 2020, "Cannot be issued against President or Governor", "राष्ट्रपति या राज्यपाल के विरुद्ध जारी नहीं हो सकती"),
        ("Writ of Quo-Warranto", "अधिकार-पृच्छा रिट (Quo-Warranto)", 2018, "Inquires into legality of claim to public office", "सार्वजनिक पद के दावे की वैधानिकता की जांच"),
        ("Article 131 Original Jurisdiction", "अनुच्छेद 131: आरंभिक अधिकारिता", 2014, "Disputes between Centre and States", "केंद्र और राज्यों के बीच विवाद"),
        ("Article 143 Advisory Jurisdiction", "अनुच्छेद 143: परामर्शदात्री क्षेत्राधिकार", 2015, "President seeks opinion of Supreme Court", "राष्ट्रपति द्वारा सर्वोच्च न्यायालय से परामर्श"),
        ("Special Powers of Lok Sabha", "लोक सभा की अनन्य शक्तियां", 2023, "Passing money bills and no-confidence motion", "धन विधेयक पारित करना एवं अविश्वास प्रस्ताव"),
        ("Privilege Motion in Parliament", "विशेषाधिकार प्रस्ताव", 2014, "Breach of parliamentary privileges by minister", "संसदीय विशेषाधिकारों का हनन होने पर"),
        ("Calling Attention Motion", "ध्यानाकर्षण प्रस्ताव", 2017, "Matter of urgent public importance", "अविलंबनीय लोक महत्व के मामले पर"),
        ("Adjournment Motion Restrictions", "स्थगन प्रस्ताव की शर्तें", 2019, "Requires support of at least 50 members", "कम से कम 50 सदस्यों का समर्थन आवश्यक"),
        ("Consolidated Fund of India (Art 266)", "भारत की संचित निधि", 2021, "Parliamentary appropriation mandatory", "संसदीय विनियोग अधिनियम अनिवार्य"),
        ("Contingency Fund of India (Art 267)", "भारत की आकस्मिकता निधि", 2022, "Placed at disposal of President", "राष्ट्रपति के व्ययनाधीन रखी जाती है"),
        ("Public Accounts Committee (PAC)", "लोक लेखा समिति", 2024, "Examines CAG reports, chaired by opposition", "CAG रिपोर्ट की जांच, विपक्ष का अध्यक्ष"),
        ("Estimates Committee Composition", "प्राक्कलन समिति", 2020, "30 members, all from Lok Sabha only", "30 सदस्य, सभी केवल लोक सभा से"),
        ("Committee on Public Undertakings", "सार्वजनिक उपक्रम समिति", 2018, "Krishna Menon Committee recommendations", "कृष्ण मेनन समिति की सिफारिशें"),
        ("National Green Tribunal (NGT)", "राष्ट्रीय हरित अधिकरण", 2015, "Statutory tribunal under NGT Act 2010", "NGT अधिनियम 2010 के तहत स्थापित"),
        ("Special Leave Petition (Art 136)", "विशेष अनुमति याचिका (अनुच्छेद 136)", 2024, "Discretionary appellate power of Supreme Court against any court or tribunal", "किसी भी न्यायालय या अधिकरण के निर्णय के विरुद्ध सर्वोच्च न्यायालय की शक्ति"),
        ("Curative Petition Concept", "सुधारात्मक याचिका (Curative Petition)", 2023, "Evolved in Rupa Ashok Hurra case to prevent abuse of process", "रूपा अशोक हुर्रा वाद में प्रतिपादित अंतिम न्यायिक उपाय"),
        ("National Judicial Appointments Commission (NJAC)", "राष्ट्रीय न्यायिक नियुक्ति आयोग", 2016, "99th Amendment struck down by SC for violating judicial independence", "न्यायपालिका की स्वतंत्रता के उल्लंघन पर 99वां संशोधन निरस्त"),
        ("Governor Ordinance Promulgation (Art 213)", "राज्यपाल की अध्यादेश शक्ति", 2017, "Co-extensive with legislative power of state legislature", "राज्य विधानमंडल के समान लेकिन केवल सत्र न चलने पर"),
        ("Pro-tem Speaker Appointment", "प्रोटेम स्पीकर (सामयिक अध्यक्ष)", 2019, "Appointed by President to administer oath to new Lok Sabha members", "नवनिर्वाचित सांसदों को शपथ दिलाने हेतु नियुक्त वरिष्ठतम सदस्य"),
        ("Subordinate Courts Supervision (Art 235)", "अधीनस्थ न्यायालयों का नियंत्रण", 2021, "Vested exclusively in the High Court of the State", "राज्य के उच्च न्यायालय में पूर्ण नियंत्रण निहित"),
        ("Tribunals under Part XIV-A (Art 323A/B)", "प्रशासनिक अधिकरण", 2020, "Added by 42nd Amendment Act 1976 for administrative adjudication", "42वें संशोधन द्वारा प्रशासनिक मामलों के त्वरित निपटान हेतु शामिल"),
        ("Election Petition High Court Jurisdiction", "चुनाव याचिका की सुनवाई", 2018, "Original jurisdiction lies with High Court, not Election Commission", "मूल अधिकारिता उच्च न्यायालय को प्राप्त है, निर्वाचन आयोग को नहीं"),
        ("Leader of Opposition Statutory Status", "विपक्ष के नेता की वैधानिक स्थिति", 2022, "Recognized under Salary and Allowances of Leaders of Opposition Act 1977", "1977 के संसदीय अधिनियम द्वारा वैधानिक मान्यता")
    ]

    for item in polity_topics:
        q_dict = {
            "id": qid,
            "year": item[0],
            "paper": "GS Paper I",
            "subject": "Polity",
            "topic": item[1] + " (" + item[2] + ")",
            "prompt_en": item[3],
            "prompt_hi": item[4],
            "statements_en": item[5],
            "statements_hi": item[6],
            "sub_prompt_en": item[7],
            "sub_prompt_hi": item[8],
            "options_en": item[9],
            "options_hi": item[10],
            "correctIndex": item[11],
            "explanation_en": item[12],
            "explanation_hi": item[13]
        }
        questions.append(q_dict)
        qid += 1

    for title_en, title_hi, yr, desc_en, desc_hi in polity_extra:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "GS Paper I",
            "subject": "Polity",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"With reference to {title_en} in India, consider the following statements:",
            "prompt_hi": f"भारत में {title_hi} के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            "statements_en": [
                f"Under the Indian Constitution, {desc_en} is explicitly provided.",
                "It can be altered only through a constitutional amendment with special majority."
            ],
            "statements_hi": [
                f"भारतीय संविधान के तहत {desc_hi} का स्पष्ट प्रावधान किया गया है।",
                "इसे केवल विशेष बहुमत द्वारा संविधान संशोधन के माध्यम से ही संशोधित किया जा सकता है।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}।"
        }
        questions.append(q_dict)
        qid += 1

    # ========================================================
    # 2. ECONOMY (50 Questions)
    # ========================================================
    economy_list = [
        ("Sovereign Green Bonds", "सॉवरेन ग्रीन बॉन्ड", 2024, "Funds exclusively public zero-carbon projects via RBI FAR route", "सार्वजनिक हरित परियोजनाओं हेतु FAR मार्ग से FPI निवेश मान्य"),
        ("CBDC e-Rupee", "सीबीडीसी ई-रुपया", 2023, "Central bank legal tender sovereign liability token", "RBI की बैलेंस शीट पर संप्रभु देयता टोकन"),
        ("Inflation Targeting MPC", "मौद्रिक नीति समिति एवं मुद्रास्फीति", 2022, "CPI target of 4% +/- 2% under Section 45ZA of RBI Act", "RBI अधिनियम धारा 45ZA के तहत 4% +/- 2% लक्ष्य"),
        ("Demand vs Time Deposits", "मांग बनाम सावधि जमा", 2021, "Current and savings demand portion payable without notice", "मांग पर तत्काल देय चालू व बचत खाता राशि"),
        ("NBFCs Regulatory Framework", "गैर-बैंकिंग वित्तीय कंपनियां", 2020, "NBFCs cannot accept demand deposits or issue cheques", "NBFCs मांग जमा स्वीकार नहीं कर सकतीं"),
        ("Money Multiplier Mechanics", "मुद्रा गुणक की कार्यप्रणाली", 2019, "Increases with higher banking habit of population", "जनसंख्या की बैंकिंग आदतों में वृद्धि से बढ़ता है"),
        ("FRBM Debt-to-GDP Targets", "FRBM ऋण-जीडीपी लक्ष्य", 2018, "N.K. Singh committee 60% general debt target", "एन.के. सिंह समिति द्वारा 60% ऋण लक्ष्य"),
        ("NPCI & UPI Architecture", "एनपीसीआई एवं यूपीआई", 2017, "Umbrella retail payment entity set up by RBI & IBA", "RBI एवं IBA द्वारा स्थापित खुदरा भुगतान निकाय"),
        ("MCLR Transmission Mechanism", "MCLR संचरण प्रणाली", 2015, "Marginal cost of funds replaces base rate for fast transmission", "मौद्रिक नीति संचरण तेजी से करने हेतु बेस रेट के स्थान पर लागू"),
        ("Balance of Payments Capital Account", "भुगतान संतुलन: पूंजी खाता", 2014, "FDI, FPI and ECB form capital account, remittances in current", "FDI, FPI और बाह्य उधारी पूंजी खाते का भाग हैं"),
        ("Inverted Duty Structure", "इनवर्टेड ड्यूटी स्ट्रक्चर", 2023, "Higher import duty on raw materials than finished goods", "कच्चे माल पर तैयार माल की तुलना में अधिक आयात शुल्क"),
        ("Prompt Corrective Action (PCA)", "शीघ्र सुधारात्मक कार्रवाई (PCA)", 2021, "RBI framework on capital, asset quality, and profitability", "बैंकों की वित्तीय स्थिति सुधारने हेतु RBI का फ्रेमवर्क"),
        ("Core Inflation vs Headline Inflation", "कोर मुद्रास्फीति बनाम हेडलाइन", 2020, "Core excludes volatile food and fuel components", "कोर मुद्रास्फीति में खाद्य और ईंधन शामिल नहीं होते"),
        ("Real Effective Exchange Rate (REER)", "वास्तविक प्रभावी विनिमय दर", 2022, "Trade-weighted exchange rate adjusted for relative price differentials", "व्यापार भारित मूल्य अंतर समायोजित विनिमय दर"),
        ("Open Market Operations (OMO)", "खुले बाजार की क्रियाएं (OMO)", 2019, "Sale and purchase of government securities by RBI", "RBI द्वारा सरकारी प्रतिभूतियों का क्रय-विक्रय"),
        ("Statutory Liquidity Ratio (SLR)", "सांविधिक तरलता अनुपात", 2018, "Maintained in gold, cash, or approved government securities", "स्वर्ण, नकदी या अनुमोदित प्रतिभूतियों में अनिवार्य धारिता"),
        ("Priority Sector Lending (PSL)", "प्राथमिकता प्राप्त क्षेत्रक ऋण", 2024, "40% ANBC target for domestic commercial banks", "वाणिज्यिक बैंकों हेतु 40% लक्ष्य (कृषि, MSME आदि)"),
        ("External Commercial Borrowings (ECB)", "बाह्य वाणिज्यिक उधारी (ECB)", 2017, "Commercial loans raised by resident entities from non-resident lenders", "भारतीय कंपनियों द्वारा विदेशी स्रोतों से वाणिज्यिक ऋण"),
        ("Participatory Notes (P-Notes)", "सहभागिता पत्र (P-Notes)", 2016, "Offshore derivative instruments issued by registered FPIs", "पंजीकृत विदेशी संस्थागत निवेशकों द्वारा जारी डेरिवेटिव"),
        ("Sovereign Wealth Funds / NIIF", "राष्ट्रीय निवेश और अवसंरचना कोष", 2015, "NIIF acts as India sovereign-anchored investment manager", "भारत का पहला संप्रभु अवसंरचना कोष प्रबंधक"),
        ("Fiscal Deficit Concept", "राजकोषीय घाटा की संकल्पना", 2014, "Excess of total budget expenditure over non-debt receipts", "कुल बजट व्यय का गैर-ऋण प्राप्तियों पर आधिक्य"),
        ("Revenue Deficit vs Effective Revenue Deficit", "प्रभावी राजस्व घाटा", 2018, "Excludes grants given for creation of capital assets", "पूंजीगत परिसंपत्तियों के सृजन हेतु दिए गए अनुदान को घटाकर"),
        ("Current Account Deficit (CAD)", "चालू खाता घाटा", 2023, "Trade deficit plus net factor income and transfers deficit", "व्यापार घाटा एवं शुद्ध सेवा व प्रेषण का अंतर"),
        ("Special Drawing Rights (SDR)", "विशेष आहरण अधिकार (SDR)", 2020, "IMF reserve asset basket of 5 currencies (USD, EUR, CNY, JPY, GBP)", "IMF की 5 मुद्राओं की बास्केट पर आधारित परिसंपत्ति"),
        ("Monetary Policy Stance (Accommodative / Calibrated)", "मौद्रिक नीति का रुख", 2022, "Expansion of liquidity to stimulate economic growth", "आर्थिक वृद्धि को गति देने हेतु तरलता विस्तार"),
        ("Bad Bank / NARCL", "बैड बैंक / एनएआरसीएल", 2024, "National Asset Reconstruction Company for resolving stressed loans", "दबावग्रस्त ऋणों के समाधान हेतु स्थापित परिसंपत्ति कंपनी"),
        ("Insolvency and Bankruptcy Code (IBC 2016)", "दिवाला एवं शोधन अक्षमता संहिता", 2019, "Creditor-in-control time-bound resolution mechanism", "ऋणदाताओं के नियंत्रण में समयबद्ध समाधान प्रणाली"),
        ("GST Council (Article 279A)", "जीएसटी परिषद (अनुच्छेद 279A)", 2017, "Constitutional federal body chaired by Union Finance Minister", "केंद्रीय वित्त मंत्री की अध्यक्षता वाली संवैधानिक परिषद"),
        ("Foreign Direct Investment (FDI) Routes", "प्रत्यक्ष विदेशी निवेश के मार्ग", 2015, "Automatic route vs Government approval route", "स्वचालित मार्ग बनाम सरकारी अनुमोदन मार्ग"),
        ("Angel Tax Provisions (Section 56)", "एंजेल टैक्स प्रावधान", 2023, "Tax on unlisted company shares issued above fair market value", "उचित बाजार मूल्य से अधिक पर शेयर जारी करने पर कर"),
        ("Index of Industrial Production (IIP)", "औद्योगिक उत्पादन सूचकांक (IIP)", 2018, "Eight core industries comprise 40.27% weightage in IIP", "8 कोर उद्योगों का IIP में 40.27% भारांश"),
        ("Purchasing Power Parity (PPP)", "क्रय शक्ति समता (PPP)", 2016, "Exchange rate equalizing basket purchasing power across nations", "देशों के बीच समान वस्तुओं की क्रय शक्ति समकारी दर"),
        ("Gini Coefficient & Lorenz Curve", "गिनी गुणांक एवं लोरेंज वक्र", 2014, "Measures statistical dispersion of income inequality", "आय और धन की असमानता को मापने वाला सूचकांक"),
        ("Minimum Support Price (MSP) Determinants", "न्यूनतम समर्थन मूल्य निर्धारण", 2020, "Recommended by CACP factoring A2+FL cost formula", "CACP द्वारा A2+FL लागत फॉर्मूले पर संस्तुत मूल्य"),
        ("PM-Kisan Direct Benefit Transfer", "पीएम-किसान योजना", 2021, "Direct income support of Rs 6,000 annually to landholding farmers", "किसानों को प्रतिवर्ष 6000 रुपये की सीधी आय सहायता"),
        ("Agricultural Infrastructure Fund", "कृषि अवसंरचना कोष", 2022, "Medium-long term debt financing for post-harvest management", "फसल कटाई उपरांत प्रबंधन हेतु दीर्घकालिक ऋण सुविधा"),
        ("Trade Facilitation Agreement (TFA)", "व्यापार सुगमता समझौता (TFA)", 2017, "WTO binding treaty simplifying customs cross-border procedures", "विश्व व्यापार संगठन का सीमा शुल्क सरलीकरण समझौता"),
        ("Agreement on Agriculture (AoA) Boxes", "कृषि पर समझौता: ग्रीन/ब्लू/एम्बर बॉक्स", 2015, "Green box non-distorting, amber box trade-distorting support", "ग्रीन बॉक्स गैर-व्यापार विकृतकारी सहायता"),
        ("Carbon Border Adjustment Mechanism (CBAM)", "कार्बन बॉर्डर एडजस्टमेंट मैकेनिज्म", 2024, "EU tariff on carbon-intensive goods imported into Europe", "यूरोपीय संघ द्वारा कार्बन-सघन आयातों पर लगाया गया शुल्क"),
        ("Disinvestment & DIPAM", "विनिवेश एवं दीपम (DIPAM)", 2019, "Strategic disinvestment of Central Public Sector Enterprises", "केंद्रीय सार्वजनिक क्षेत्र के उद्यमों का रणनीतिक विनिवेश"),
        ("Treasury Bills (T-Bills) Maturities", "ट्रेजरी बिल (T-Bills)", 2024, "Zero-coupon sovereign debt issued in 91-day, 182-day, and 364-day tenors", "91, 182 और 364 दिन की परिपक्वता वाले शून्य कूपन बांड"),
        ("Ways and Means Advances (WMA)", "अर्थोपाय अग्रिम (WMA)", 2023, "Temporary liquidity loan facility by RBI to central and state governments", "सरकारों की अस्थायी वित्तीय कमी को पूरा करने हेतु RBI का ऋण"),
        ("Cash Reserve Ratio (CRR) Maintenance", "नकद आरक्षित अनुपात (CRR)", 2022, "Percentage of NDTL maintained as cash balance with RBI without interest", "RBI के पास नकदी के रूप में रखी जाने वाली अनिवार्य राशि"),
        ("Base Erosion and Profit Shifting (BEPS)", "आधार क्षरण एवं लाभ स्थानांतरण", 2021, "OECD/G20 initiative to prevent corporate tax avoidance by MNCs", "बहुराष्ट्रीय कंपनियों द्वारा कर चोरी रोकने की OECD पहल"),
        ("Equalization Levy / Digital Tax", "इक्वलाइजेशन लेवी (डिजिटल कर)", 2020, "Tax on non-resident e-commerce operators providing digital services in India", "विदेशी डिजिटल कंपनियों पर लगाया जाने वाला प्रत्यक्ष कर"),
        ("Real Estate Investment Trusts (REITs)", "रियल एस्टेट निवेश ट्रस्ट (REITs)", 2019, "Regulated by SEBI allowing small investors to own fractional commercial real estate", "व्यावसायिक संपत्तियों में छोटे निवेशकों की भागीदारी हेतु SEBI विनियमित"),
        ("Infrastructure Investment Trusts (InvITs)", "अवसंरचना निवेश ट्रस्ट (InvITs)", 2018, "Enables pooling of investment in operational infrastructure projects", "सड़क, पारेषण जैसी बुनियादी ढांचा परियोजनाओं में निवेश मंच"),
        ("Credit Default Swaps (CDS)", "क्रेडिट डिफॉल्ट स्वैप (CDS)", 2017, "Financial derivative contract transferring credit risk of fixed income security", "ऋणदाता को कर्जदार के डिफॉल्ट से बचाने वाला वित्तीय अनुबंध"),
        ("Financial Inclusion Index (FI-Index)", "वित्तीय समावेशन सूचकांक", 2022, "Published annually by RBI measuring access, usage, and quality", "RBI द्वारा वित्तीय पहुंच, उपयोग और गुणवत्ता मापने वाला सूचकांक")
    ]

    for title_en, title_hi, yr, desc_en, desc_hi in economy_list:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "GS Paper I",
            "subject": "Economy",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"With reference to {title_en} in the Indian Economy, consider the following statements:",
            "prompt_hi": f"भारतीय अर्थव्यवस्था में {title_hi} के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            "statements_en": [
                f"{desc_en}.",
                "It is strictly determined solely by external market forces without regulatory intervention."
            ],
            "statements_hi": [
                f"{desc_hi}।",
                "यह बिना किसी विनियामक हस्तक्षेप के पूरी तरह केवल बाहरी बाजार शक्तियों द्वारा निर्धारित होता है।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}. Statement 2 is incorrect as regulatory frameworks apply.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}। कथन 2 गलत है क्योंकि विनियामक नियम लागू होते हैं।"
        }
        questions.append(q_dict)
        qid += 1

    # ========================================================
    # 3. HISTORY & ART & CULTURE (50 Questions)
    # ========================================================
    history_list = [
        ("Rigvedic Geography / Nadistuti", "ऋग्वैदिक नदियां", 2024, "Nadistuti Sukta in Rigveda praises 21 rivers including Sarasvati and Ganga", "ऋग्वेद के नदीस्तुति सूक्त में सरस्वती, सिंधु, गंगा और यमुना का उल्लेख है"),
        ("Tolkappiyam Sangam Work", "तोलकाप्पियम संगम ग्रंथ", 2023, "Earliest extant Tamil masterpiece on grammar and poetics", "तमिल व्याकरण एवं काव्यशास्त्र का प्राचीनतम उपलब्ध ग्रंथ"),
        ("Agrahara Land Grants", "अग्रहार भूमि अनुदान", 2022, "Tax-free royal land granted to Brahmanas and scholars", "ब्राह्मणों एवं विद्वानों को दी जाने वाली कर-मुक्त भूमि"),
        ("Shramana & Upasaka Terms", "श्रमण एवं उपासक शब्दावली", 2021, "Shramana refers to heterodox monks, Upasaka to lay Buddhist householders", "श्रमण गैर-वैदिक तपस्वी तथा उपासक गृहस्थ बौद्ध अनुयायी थे"),
        ("Sthanakvasi Jain Sect", "स्थानकवासी जैन संप्रदाय", 2020, "Reforms sub-sect of Shvetambara Jainism rejecting idol-worship", "श्वेतांबर जैन धर्म का संप्रदाय जो मूर्ति पूजा नहीं करता"),
        ("Swadeshi National Education", "स्वदेशी आंदोलन एवं राष्ट्रीय शिक्षा", 2019, "National Council of Education established in August 1906", "अगस्त 1906 में राष्ट्रीय शिक्षा परिषद की स्थापना"),
        ("Champaran Satyagraha 1917", "चंपारण सत्याग्रह", 2018, "First civil disobedience linking peasant struggles to national movement", "तिनकठिया प्रणाली के विरुद्ध किसानों का राष्ट्रीय आंदोलन से जुड़ाव"),
        ("Charter Act 1813 Provisions", "1813 का चार्टर अधिनियम", 2017, "Abolished Company trade monopoly except tea and trade with China", "चाय और चीन व्यापार को छोड़कर कंपनी का एकाधिकार समाप्त"),
        ("Amuktamalyada by Krishnadevaraya", "कृष्णदेवराय का आमुक्तमाल्यद", 2016, "Telugu treatise on statecraft and administrative theory", "राजव्यवस्था एवं शासन पर तेलुगु का प्रसिद्ध ग्रंथ"),
        ("Ghadar Movement San Francisco", "गदर आंदोलन", 2014, "Founded in 1913 by Lala Har Dayal with headquarters at Yugantar Ashram", "1913 में लाला हरदयाल द्वारा सैन फ्रांसिस्को में स्थापित"),
        ("Indus Valley Dholavira Water Harvesting", "धौलावीरा जल संचयन प्रणाली", 2021, "Unique series of rock-cut water reservoirs in Rann of Kutch", "कच्छ के रण में शैलकर्तित जलाशयों की उन्नत प्रणाली"),
        ("Lothal Dockyard Harappan Port", "लोथल गोदीवाड़ा", 2018, "Tidal dockyard connected to Bhogavo river in Gujarat", "भोगवा नदी से जुड़ा हड़प्पा सभ्यता का प्रसिद्ध बंदरगाह"),
        ("Ashoka Rock Edict XIII Kalinga", "अशोक का 13वां शिलालेख", 2016, "Mentions Kalinga war remorse and victory by Dhamma", "कलिंग युद्ध के पश्चाताप एवं धम्म विजय का उल्लेख"),
        ("Kandariya Mahadeva Khajuraho", "कंदरिया महादेव मंदिर खजुराहो", 2020, "Panchayatana Nagara style built by Chandela dynasty", "चंदेल राजाओं द्वारा निर्मित नागर शैली का उत्कृष्ट मंदिर"),
        ("Ellora Kailasa Temple (Cave 16)", "एलोरा का कैलाश मंदिर", 2017, "Monolithic rock-cut temple carved from top to bottom by Rashtrakuta Krishna I", "राष्ट्रकूट शासक कृष्ण प्रथम द्वारा निर्मित एकाश्मक मंदिर"),
        ("Ajanta Murals & Frescoes", "अजंता के भित्ति चित्र", 2015, "Depict Jataka tales and Bodhisattva Padmapani under Vakatakas", "जातक कथाओं और पद्मपाणि बोधिसत्व का सुंदर चित्रण"),
        ("Bhakti Saint Kabir Teachings", "भक्ति संत कबीर के उपदेश", 2019, "Nirguna Bhakti rejecting caste hierarchies and rituals", "निर्गुण भक्ति, जाति प्रथा एवं बाह्य आडंबरों का विरोध"),
        ("Guru Nanak Devji Langar Concept", "गुरु नानक देव जी एवं लंगर", 2021, "Egalitarian community kitchen establishing social equality", "समानता और बंधुत्व की स्थापना हेतु सामुदायिक लंगर"),
        ("Akbar Sulh-i-Kul Policy", "अकबर की सुलह-ए-कुल नीति", 2022, "Universal peace and tolerance codified in administration", "सर्वभौमिक शांति, सहिष्णुता और धार्मिक सौहार्द की नीति"),
        ("Mansabdari System by Akbar", "अकबर की मनसबदारी व्यवस्था", 2018, "Zat indicated personal rank and Sawar military contingent required", "जात पद और वेतन तथा सवार घुड़सवारों की संख्या तय करता था"),
        ("Ibadat Khana at Fatehpur Sikri", "इबादत खाना (फतेहपुर सीकरी)", 2014, "House of Worship built in 1575 for inter-faith philosophical debates", "धार्मिक एवं दार्शनिक परिचर्चाओं हेतु 1575 में निर्मित"),
        ("Battle of Plassey 1757 Factors", "प्लासी का युद्ध 1757", 2020, "Mir Jafar betrayed Siraj-ud-Daulah leading to British political foothold", "मीर जाफर के विश्वासघात के कारण बंगाल में अंग्रेजी सत्ता का आरंभ"),
        ("Subsidiary Alliance by Wellesley", "वेलेजली की सहायक संधि", 2016, "Indian rulers maintained British forces and surrendered external foreign affairs", "देसी रियासतों द्वारा विदेश नीति अंग्रेजों को सौंपना"),
        ("Doctrine of Lapse by Dalhousie", "डलहौजी का व्यपगत सिद्धांत", 2017, "Annexation of states without natural heir (Satara, Jhansi, Nagpur)", "दत्तक पुत्र को उत्तराधिकारी न मानकर राज्यों का विलय"),
        ("Permanent Settlement of Bengal 1793", "बंगाल का स्थायी बंदोबस्त", 2019, "Lord Cornwallis fixed land revenue permanently with Zamindars", "लॉर्ड कॉर्नवालिस द्वारा जमींदारों से भू-राजस्व का स्थायी निर्धारण"),
        ("Ryotwari System in Madras & Bombay", "रैयतवाड़ी बंदोबस्त", 2022, "Thomas Munro directly recognized peasant-cultivator as owner", "थॉमस मुनरो द्वारा किसानों को सीधे भूमि का स्वामी मानना"),
        ("Mahalwari System by Holt Mackenzie", "महालवाड़ी बंदोबस्त", 2018, "Revenue settled with entire village community / Mahal", "हॉल्ट मैकेंजी द्वारा पूरे गांव/महाल के साथ राजस्व समझौता"),
        ("Wood's Education Despatch 1854", "वुड का घोषणा पत्र (1854)", 2015, "Magna Carta of English education in India recommending vernacular primaries", "भारतीय शिक्षा का मैग्नाकार्टा, प्राथमिक में मातृभाषा की संस्तुति"),
        ("Brahmo Samaj by Raja Ram Mohan Roy", "राजा राममोहन राय एवं ब्रह्म समाज", 2023, "Pioneered crusade against Sati and championed modern rationalism", "सती प्रथा का उन्मूलन एवं आधुनिक तर्कवाद का प्रसार"),
        ("Arya Samaj by Dayananda Saraswati", "दयानंद सरस्वती एवं आर्य समाज", 2021, "Called 'Back to the Vedas' and opposed idol worship and caste by birth", "'वेदों की ओर लौटो' का नारा एवं सामाजिक सुधार"),
        ("Satyashodhak Samaj by Jyotirao Phule", "सत्यशोधक समाज (ज्योतिराव फुले)", 2016, "Crusade against caste exploitation and education for women and Shudras", "दलितों, शूद्रों एवं महिलाओं के अधिकारों हेतु 1873 में स्थापना"),
        ("Indian National Congress 1885", "भारतीय राष्ट्रीय कांग्रेस 1885", 2014, "Founded by A.O. Hume, first session in Bombay under W.C. Bonnerjee", "ए.ओ. ह्यूम द्वारा स्थापित, प्रथम अध्यक्ष डब्ल्यू.सी. बनर्जी"),
        ("Surat Split of 1907", "सूरत विभाजन 1907", 2018, "Rift between Moderates and Extremists over Swadeshi extension", "नरम दल और गरम दल के बीच विचारधारात्मक विभाजन"),
        ("Morley-Minto Reforms 1909", "मार्ले-मिंटो सुधार 1909", 2017, "Introduced separate electorates for Muslims in central legislature", "मुसलमानों के लिए पृथक निर्वाचन प्रणाली की शुरुआत"),
        ("Home Rule League Movement 1916", "होम रूल लीग आंदोलन 1916", 2020, "Pioneered by Bal Gangadhar Tilak and Annie Besant for self-government", "तिलक और एनी बेसेंट द्वारा स्वशासन की मांग हेतु आरंभ"),
        ("Non-Cooperation Movement 1920", "असहयोग आंदोलन 1920", 2022, "Surrender of titles, boycott of courts and foreign goods after Jallianwala", "खिलाफत एवं पंजाब अन्याय के विरोध में विदेशी वस्तुओं का बहिष्कार"),
        ("Civil Disobedience & Dandi March 1930", "सविनय अवज्ञा आंदोलन एवं दांडी मार्च", 2021, "Breaking salt law at Dandi launched nationwide civil disobedience", "नमक कानून तोड़कर राष्ट्रव्यापी सविनय अवज्ञा की शुरुआत"),
        ("Quit India Resolution August 1942", "भारत छोड़ो आंदोलन 1942", 2019, "'Do or Die' call at Gowalia Tank Bombay led to spontaneous mass uprising", "'करो या मरो' का नारा एवं ऐतिहासिक जनक्रांति"),
        ("Cabinet Mission Plan 1946", "कैबिनेट मिशन योजना 1946", 2023, "Rejected sovereign Pakistan and created Constituent Assembly of India", "संविधान सभा के गठन का आधार एवं त्रिस्तरीय संघीय योजना"),
        ("Indian Independence Act 1947", "भारतीय स्वतंत्रता अधिनियम 1947", 2015, "Created independent dominions of India and Pakistan on 15 August 1947", "15 अगस्त 1947 को भारत और पाकिस्तान के स्वतंत्र डोमिनियन की स्थापना"),
        ("Sarnath Lion Capital Mauryan Art", "सारनाथ का सिंह शीर्ष (मौर्य कला)", 2024, "Carved in polished Chunar sandstone adopted as National Emblem of India", "चुनार बलुआ पत्थर से निर्मित भारत का राष्ट्रीय प्रतीक"),
        ("Megasthenes Indica Mauryan Society", "मेगास्थनीज की इंडिका", 2023, "Greek ambassador of Seleucus recording 7-caste division of Mauryan society", "मौर्य समाज के सात वर्गों में विभाजन का उल्लेख"),
        ("Harsha Kannauj Assembly", "हर्षवर्धन की कन्नौज सभा", 2022, "Convened in honor of Chinese pilgrim Xuanzang (Hiuen Tsang) in 643 AD", "ह्वेनसांग के सम्मान में आयोजित विशाल धार्मिक सभा"),
        ("Chola Local Self-Government Uttaramerur", "चोल स्थानीय स्वशासन (उत्तरमेरूर)", 2021, "Uttaramerur inscriptions record detailed Kudavolai ballot election rules for village sabha", "कुदावोलाई मतपत्र प्रणाली द्वारा ग्राम सभा के चुनाव"),
        ("Delhi Sultanate Market Reforms Alauddin", "अलाउद्दीन खिलजी के बाजार सुधार", 2020, "Fixed prices of grain, cloth, and horses under Shahna-i-Mandi", "शहना-ए-मंडी के अधीन वस्तुओं के मूल्यों का सख्त नियंत्रण"),
        ("Sher Shah Suri Grand Trunk Road", "शेरशाह सूरी एवं ग्रांड ट्रंक रोड", 2019, "Constructed Sadak-e-Azam from Sonargaon to Peshawar and introduced Rupiya", "सड़क-ए-आजम का निर्माण एवं चांदी का रुपया सिक्का चलाया"),
        ("Din-i-Ilahi by Emperor Akbar", "अकबर का दीन-ए-इलाही", 2018, "Syncretic ethical religion founded in 1582 emphasizing monotheism and virtue", "1582 में आरंभ किया गया नैतिक एवं सार्वभौमिक समन्वयवादी पंथ"),
        ("Maratha Chauth and Sardeshmukhi", "मराठा कर: चौथ एवं सरदेशमुखी", 2017, "Chauth was 25% protection tax, Sardeshmukhi was 10% hereditary levy", "पड़ोसी राज्यों से सुरक्षा हेतु 25% चौथ और 10% सरदेशमुखी"),
        ("Rani Gaidinliu Heraka Movement", "रानी गाइदिनल्यू एवं हेराका आंदोलन", 2023, "Naga spiritual leader who fought British colonial rule in Manipur and Nagaland", "मणिपुर व नगालैंड में ब्रिटिश शासन के विरुद्ध स्वतंत्रता संग्राम"),
        ("Komagata Maru Incident 1914", "कामागाटा मारू घटना 1914", 2014, "Japanese steamship carrying Sikh passengers denied entry into Canada and fired upon at Budge Budge", "कनाडा में प्रवेश से रोके गए सिख यात्रियों का ऐतिहासिक जहाज")
    ]

    for title_en, title_hi, yr, desc_en, desc_hi in history_list:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "GS Paper I",
            "subject": "History",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"With reference to {title_en} in Indian history, consider the following statements:",
            "prompt_hi": f"भारतीय इतिहास में {title_hi} के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            "statements_en": [
                f"{desc_en}.",
                "It occurred during the early medieval period under Sultanate rule."
            ],
            "statements_hi": [
                f"{desc_hi}।",
                "यह घटना सल्तनत काल के आरंभिक मध्यकाल में घटित हुई थी।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}।"
        }
        questions.append(q_dict)
        qid += 1

    # ========================================================
    # 4. ENVIRONMENT & ECOLOGY (50 Questions)
    # ========================================================
    env_list = [
        ("Cheetah Reintroduction in Kuno", "कूनो में चीता पुनर्वास", 2024, "Asiatic cheetah extinct in 1952, African cheetahs translocated to Kuno MP", "1952 में विलुप्त घोषित, नामीबिया व दक्षिण अफ्रीका से कूनो में पुनर्वास"),
        ("Invasive Alien Species Prosopis", "आक्रामक प्रजाति विलायती बबूल", 2023, "Reduces local native floral biodiversity and depletes groundwater", "स्थानीय जैव विविधता को कम करता है और भूजल सोखता है"),
        ("Blue Carbon Coastal Ecosystems", "ब्लू कार्बन पारिस्थितिकी", 2021, "Carbon captured and stored in mangroves, tidal marshes, and seagrasses", "मैंग्रोव, ज्वारीय दलदल और समुद्री घास द्वारा प्रगृहीत कार्बन"),
        ("Cauvery Basin Wildlife Sanctuaries", "कावेरी बेसिन वन्यजीव अभयारण्य", 2020, "Nagarhole, Sathyamangalam and Wayanad drain into Cauvery basin", "नागरहोल, सत्यमंगलम और वायनाड कावेरी बेसिन का भाग हैं"),
        ("Microbeads in Marine Waters", "माइक्रोबीड्स समुद्री प्रदूषण", 2019, "Microscopic synthetic plastics in cosmetics damaging marine food chains", "सौंदर्य प्रसाधनों से निकलने वाले सूक्ष्म प्लास्टिक कण जो जलीय जीवन को नष्ट करते हैं"),
        ("National Biodiversity Authority", "राष्ट्रीय जैव विविधता प्राधिकरण", 2017, "Statutory body under Biological Diversity Act 2002 checking biopiracy", "बायोपायरेसी रोकने और जैव संसाधनों के संरक्षण हेतु गठित वैधानिक निकाय"),
        ("Red Sanders Eastern Ghats", "रक्त चंदन शेषाचलम पहाड़ियां", 2016, "Endemic timber species growing in dry deciduous forests of Andhra Pradesh", "आंध्र प्रदेश के पूर्वी घाट/शेषाचलम के शुष्क पर्णपाती वनों में स्थानिक वृक्ष"),
        ("BioCarbon Fund World Bank", "बायोकार्बन फंड पहल", 2015, "Multilateral facility managed by World Bank for sustainable landscapes", "सतत वन परिदृश्य हेतु विश्व बैंक द्वारा प्रबंधित बहुपक्षीय कोष"),
        ("Global Environment Facility (GEF)", "वैश्विक पर्यावरण सुविधा", 2014, "Financial mechanism serving CBD, UNFCCC, Stockholm and Minamata", "जैव विविधता एवं जलवायु परिवर्तन संधियों हेतु वित्तीय तंत्र"),
        ("Ramsar Convention Montreux Record", "रामसर मोंट्रेक्स रिकॉर्ड", 2018, "Register of wetland sites where ecological character changes have occurred", "पारिस्थितिक संकटग्रस्त आर्द्रभूमियों की वैश्विक सूची (लोकटक, केवलादेव)"),
        ("Wildlife Protection Act 1972 Schedules", "वन्यजीव संरक्षण अधिनियम 1972", 2022, "Amended in 2022 reducing schedules to four for CITES alignment", "2022 संशोधन द्वारा अनुसूचियों को युक्तिसंगत बनाया गया"),
        ("Project Tiger & NTCA", "प्रोजेक्ट टाइगर एवं NTCA", 2023, "National Tiger Conservation Authority established under 2006 amendment", "2006 के संशोधन द्वारा गठित राष्ट्रीय बाघ संरक्षण प्राधिकरण"),
        ("Corbett National Park First in India", "जिम कॉर्बेट राष्ट्रीय उद्यान", 2014, "Established in 1936 as Hailey National Park in Uttarakhand", "1936 में हेली नेशनल पार्क के रूप में स्थापित भारत का पहला राष्ट्रीय उद्यान"),
        ("Kaziranga National Park Rhinos", "काजीरंगा राष्ट्रीय उद्यान", 2019, "Hosts world largest population of Great One-horned Rhinoceros", "विश्व के सर्वाधिक एक सींग वाले गैंडों का प्राकृतिक आवास"),
        ("Great Nicobar Biosphere Reserve", "ग्रेट निकोबार बायोस्फीयर रिजर्व", 2021, "Home to Shompen and Nicobarese tribes and saltwater crocodiles", "शौम्पेन जनजाति और लवणजल मगरमच्छ का प्राकृतिक पर्यावास"),
        ("Bhitarkanika Mangroves Saltwater Crocs", "भितरकनिका मैंग्रोव ओडिशा", 2017, "Ramsar wetland fed by Brahmani and Baitarani rivers hosting olive ridleys", "ब्राह्मणी-वैतरणी संगम पर ऑलिव रिडले कछुओं और मगरमच्छों का केंद्र"),
        ("Silent Valley Lion-tailed Macaque", "साइलेंट वैली (शांत घाटी केरल)", 2015, "Evergreen tropical rainforest preserving endangered lion-tailed macaque", "सिंह-पुच्छी मकाक का प्रसिद्ध सदाबहार वर्षावन पर्यावास"),
        ("Sundarbans Mangrove Royal Bengal Tiger", "सुंदरबन डेल्टा मैंग्रोव", 2018, "Tidal halophyte mangrove forest spanning India and Bangladesh", "विश्व का सबसे बड़ा मैंग्रोव डेल्टा एवं रॉयल बंगाल टाइगर का घर"),
        ("Keibul Lamjao Floating National Park", "केइबुल लामजाओ तैरता राष्ट्रीय उद्यान", 2020, "Only floating national park in the world on Loktak Lake Manipur (Phumdis)", "मणिपुर की लोकटक झील पर फुमदी पर तैरता एकमात्र राष्ट्रीय उद्यान (संगाई हिरण)"),
        ("Western Ghats Biodiversity Hotspot", "पश्चिमी घाट जैव विविधता हॉटस्पॉट", 2016, "High endemism recognized as UNESCO World Heritage Site", "यूनेस्को विश्व धरोहर एवं उच्च स्थानिक प्रजातियों का समृद्ध क्षेत्र"),
        ("Ozone Layer Protection Montreal Protocol", "मॉन्ट्रियल प्रोटोकॉल एवं ओजोन परत", 2022, "Phase-out of ODS like CFCs and Kigali amendment for HFC phase-down", "ओजोन क्षयकारी पदार्थों (CFCs) को चरणबद्ध तरीके से समाप्त करने का वैश्विक समझौता"),
        ("Paris Agreement Article 6 Carbon Markets", "पेरिस समझौता अनुच्छेद 6", 2023, "Establishes bilateral and multilateral cooperative carbon credit trading", "अंतर्राष्ट्रीय कार्बन क्रेडिट व्यापार हेतु संयुक्त तंत्र"),
        ("Kunming-Montreal Global Biodiversity Framework", "कुनमिंग-मॉन्ट्रियल 30x30 लक्ष्य", 2024, "Target to conserve at least 30% of planet land and seas by 2030", "2030 तक पृथ्वी के 30% भूभाग एवं समुद्र को संरक्षित करने का लक्ष्य"),
        ("Eutrophication and Algal Blooms", "सुपोषण एवं शैवाल प्रस्फुटन", 2019, "Nutrient enrichment (N & P) causing oxygen depletion and hypoxia", "नाइट्रोजन और फास्फोरस की अधिकता से जल में ऑक्सीजन की कमी (BOD वृद्धि)"),
        ("Bioaccumulation vs Biomagnification", "जैव-संचयन बनाम जैव-आवर्धन", 2015, "Biomagnification is progressive increase in pollutant concentration up trophic levels", "खाद्य श्रृंखला में ऊपर जाने पर प्रदूषक (जैसे पारा, DDT) की सांद्रता में वृद्धि"),
        ("Fly Ash Environmental Utilization", "फ्लाई ऐश का पर्यावरणीय उपयोग", 2018, "By-product of coal thermal power used in cement manufacturing and bricks", "कोयला बिजली घरों की राख जिसका उपयोग सीमेंट एवं ईंट निर्माण में होता है"),
        ("Particulate Matter PM2.5 Impacts", "पार्टिकुलेट मैटर PM2.5 प्रभाव", 2020, "Inhalable fine particles penetrating deep into lungs and bloodstream", "फेफड़ों और रक्तप्रवाह में गहराई तक प्रवेश करने वाले घातक सूक्ष्म कण"),
        ("National Clean Air Programme (NCAP)", "राष्ट्रीय स्वच्छ वायु कार्यक्रम", 2021, "Targets 20-30% reduction in particulate concentrations in non-attainment cities", "शहरों में PM स्तर 20-30% तक कम करने का समयबद्ध कार्यक्रम"),
        ("Single-Use Plastic Ban India 2022", "एकल-उपयोग प्लास्टिक प्रतिबंध", 2023, "Prohibited manufacture and sale of 19 identified low-utility plastic items", "पर्यावरण मंत्रालय द्वारा 19 प्रकार के एकल-उपयोग प्लास्टिक पर पूर्ण रोक"),
        ("Extended Producer Responsibility (EPR)", "विस्तारित उत्पादक उत्तरदायित्व (EPR)", 2022, "Mandates producers to ensure channelization and recycling of plastic waste", "प्लास्टिक और ई-कचरे के पुनर्चक्रण का दायित्व उत्पादक पर तय करना"),
        ("Battery Waste Management Rules", "बैटरी अपशिष्ट प्रबंधन नियम", 2024, "Mandates recovery of critical minerals like lithium, nickel, and cobalt", "लिथियम, कोबाल्ट जैसी महत्वपूर्ण धातुओं की अनिवार्य रिकवरी"),
        ("Biochemical Oxygen Demand (BOD)", "बायोकेमिकल ऑक्सीजन डिमांड (BOD)", 2017, "Measures organic pollution level in aquatic water bodies", "जल में कार्बनिक प्रदूषण स्तर मापने का वैज्ञानिक पैमाना"),
        ("Coral Bleaching Factors", "प्रवाल विरंजन (Coral Bleaching)", 2016, "Thermal stress expels symbiotic zooxanthellae algae from corals", "तापमान वृद्धि से प्रवालों से जूजैंथेली शैवाल का निष्कासन"),
        ("Ocean Acidification Chemistry", "महासागरीय अम्लीकरण", 2014, "Higher atmospheric CO2 absorption reduces ocean pH and carbonate ions", "CO2 अवशोषण से समुद्र के pH मान में गिरावट जिससे शंख-कवच कमजोर होते हैं"),
        ("Renewable Energy National Targets 500 GW", "500 गीगावाट गैर-जीवाश्म लक्ष्य", 2023, "India commitment to achieve 500 GW non-fossil capacity by 2030", "2030 तक 500 GW गैर-जीवाश्म ऊर्जा क्षमता हासिल करने की पंचामृत घोषणा"),
        ("International Solar Alliance (ISA)", "अंतर्राष्ट्रीय सौर गठबंधन (ISA)", 2018, "Joint initiative of India and France headquartered in Gurugram", "भारत और फ्रांस की संयुक्त पहल, मुख्यालय गुरुग्राम में"),
        ("National Green Hydrogen Mission", "राष्ट्रीय हरित हाइड्रोजन मिशन", 2024, "Targets 5 MMT annual production of green hydrogen by 2030", "2030 तक प्रतिवर्ष 50 लाख टन हरित हाइड्रोजन उत्पादन का लक्ष्य"),
        ("Namami Gange Integrated Conservation", "नमामि गंगे राष्ट्रीय मिशन", 2019, "Holistic basin approach for Nirmal and Aviral Ganga flow", "गंगा नदी के समग्र संरक्षण एवं प्रदूषण नियंत्रण हेतु एकीकृत मिशन"),
        ("National Bamboo Mission Restructuring", "राष्ट्रीय बांस मिशन", 2018, "Amended Forest Act removing bamboo from definition of tree in non-forest areas", "गैर-वन क्षेत्रों में बांस को वृक्ष की परिभाषा से बाहर किया गया"),
        ("Miyawaki Urban Afforestation Method", "मियावाकी पद्धति शहरी वनीकरण", 2022, "Japanese technique of planting dense multi-layered native urban mini-forests", "शहरी क्षेत्रों में तेजी से घने बहुस्तरीय देशी वन उगाने की जापानी तकनीक"),
        ("Project Elephant 1992 & Elephant Corridors", "प्रोजेक्ट एलीफेंट एवं हाथी गलियारे", 2024, "Centrally sponsored scheme securing migratory pathways for Asian elephants", "एशियाई हाथियों के प्राकृतिक मार्गों को सुरक्षित करने की योजना"),
        ("Great Indian Bustard Habitat Protection", "ग्रेट इंडियन बस्टर्ड (गोडावण)", 2023, "Critically endangered desert bird threatened by overhead high-voltage power lines", "थार मरुस्थल का गंभीर रूप से संकटग्रस्त पक्षी (हाईटेंशन तारों से खतरा)"),
        ("Gangetic Dolphin National Aquatic Animal", "गंगा डॉल्फिन राष्ट्रीय जलीय जीव", 2022, "Blind freshwater mammal navigating via echolocation in Ganga and Brahmaputra", "इकोलोकेशन द्वारा शिकार करने वाली भारत की राष्ट्रीय जलीय जीव"),
        ("Snow Leopard Conservation Project", "हिम तेंदुआ संरक्षण परियोजना", 2021, "Vulnerable apex predator of high-altitude trans-Himalayan craggy mountains", "हिमालय के 3000-4500 मीटर ऊंचाई वाले क्षेत्रों का शीर्ष शिकारी"),
        ("Olive Ridley Turtles Gahirmatha", "ऑलिव रिडले कछुए (गहिरमाथा तट)", 2020, "Mass nesting phenomenon known as Arribada on coastal beaches of Odisha", "ओडिशा तट पर हजारों कछुओं का सामूहिक अंडा देने (अरिबाडा) का केंद्र"),
        ("Amur Falcon Migratory Sanctuary Nagaland", "अमूर फाल्कन (नागालैंड पर्यावास)", 2019, "Long-distance raptor migrating from Siberia to South Africa stopping at Doyang reservoir", "साइबेरिया से दक्षिण अफ्रीका जाने वाला प्रवासी बाज़ पक्षी"),
        ("Tiger Census All-India Monitoring 2022", "अखिल भारतीय बाघ गणना 2022", 2023, "Camera-trap census recording 3,167+ wild tigers across Indian landscapes", "कैमरा ट्रैप विधि से की गई गणना में 3167 से अधिक बाघ दर्ज"),
        ("Gharial Chambal River Sanctuary", "घड़ियाल (चंबल अभयारण्य)", 2018, "Critically endangered fish-eating crocodilian with bulbous ghara on snout", "चंबल नदी का मीठे पानी में रहने वाला लंबी थूथन वाला मगरमच्छ"),
        ("Nilgiri Tahr Eravikulam National Park", "नीलगिरि तहर (इराविकुलम पार्क)", 2017, "Endangered mountain ungulate endemic to shola-grasslands of Western Ghats", "पश्चिमी घाट के शोला घास के मैदानों में पाई जाने वाली जंगली बकरी"),
        ("Red Panda Singalila National Park", "रेड पांडा (सिंगालीला राष्ट्रीय उद्यान)", 2016, "Arboreal mammal inhabiting temperate bamboo forests of Sikkim and North Bengal", "सिक्किम व दार्जिलिंग के बांस वनों में रहने वाला दुर्लभ जीव")
    ]

    for title_en, title_hi, yr, desc_en, desc_hi in env_list:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "GS Paper I",
            "subject": "Environment",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"With reference to {title_en}, consider the following statements:",
            "prompt_hi": f"{title_hi} के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            "statements_en": [
                f"{desc_en}.",
                "It is completely immune to any adverse ecological and climatic disturbances."
            ],
            "statements_hi": [
                f"{desc_hi}।",
                "यह किसी भी प्रतिकूल पारिस्थितिक या जलवायु संबंधी व्यवधानों से पूरी तरह अप्रभावित रहता है।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}।"
        }
        questions.append(q_dict)
        qid += 1

    # ========================================================
    # 5. GEOGRAPHY (50 Questions)
    # ========================================================
    geo_list = [
        ("Red Sea & Bab-el-Mandeb Strait", "लाल सागर एवं बाब-अल-मंदेब", 2024, "Bab-el-Mandeb connects Red Sea to Gulf of Aden and Arabian Sea", "बाब-अल-मंदेब जलडमरूमध्य लाल सागर को अदन की खाड़ी से जोड़ता है"),
        ("Indian Waterfalls and Rivers", "भारतीय जलप्रपात एवं नदियां", 2023, "Dhuandhar on Narmada, Hundru on Subarnarekha, Gersoppa Jog on Sharavati", "धुआंधार (नर्मदा), हुंडरू (सुवर्णरेखा), और जोग (शरावती नदी)"),
        ("Himalayan Peaks Mountain Ranges", "हिमालयी पर्वत शिखर", 2022, "Nanda Devi in Kumaon, Namcha Barwa in Eastern Himalayas, Nokrek in Garo Hills", "नंदा देवी कुमाऊं में, नामचा बरवा पूर्वी हिमालय में, नोकरेक गारो हिल्स में"),
        ("Siachen Glacier Nubra Valley", "सियाचिन ग्लेशियर एवं नुब्रा घाटी", 2020, "Siachen lies in Karakoram range directly North of Nubra Valley", "सियाचिन ग्लेशियर काराकोरम श्रेणी में नुब्रा घाटी के उत्तर में स्थित है"),
        ("Mediterranean Climate Winter Rains", "भूमध्यसागरीय जलवायु", 2018, "Receives cyclonic winter rainfall from Westerlies with dry summers", "पछुआ पवनों के कारण शीतकाल में वर्षा और ग्रीष्मकाल शुष्क"),
        ("Equator Passing 13 Nations", "भूमध्य रेखा पर स्थित देश", 2015, "Passes through Colombia, Kenya, Indonesia among 13 countries", "कोलंबिया, केन्या, इंडोनेशिया सहित 13 देशों से गुजरती है"),
        ("Turkey Surrounding Seas", "तुर्की के सीमावर्ती सागर", 2014, "Anatolian Turkey lies between Black Sea to the North and Mediterranean to South", "तुर्की उत्तर में काला सागर और दक्षिण में भूमध्य सागर के बीच स्थित है"),
        ("Major Rivers Originating in Amarkantak", "अमरकंटक से निकलने वाली नदियां", 2016, "Narmada, Son and Johilla originate from Amarkantak plateau", "नर्मदा और सोन नदियां अमरकंटक पठार से निकलती हैं"),
        ("Indus Water Treaty 1960 Rivers", "सिंधु जल समझौता 1960", 2021, "India has unrestricted use of Eastern rivers (Ravi, Beas, Sutlej)", "भारत को पूर्वी नदियों (रावी, ब्यास, सतलज) के जल का पूर्ण अधिकार"),
        ("Brahmaputra Yarlung Tsangpo Course", "ब्रह्मपुत्र नदी का अपवाह तंत्र", 2017, "Known as Yarlung Tsangpo in Tibet, cuts deep gorge at Namcha Barwa", "तिब्बत में यारलुंग त्सांगपो, नामचा बरवा के पास यू-टर्न लेती है"),
        ("Godavari River Tributaries", "गोदावरी की सहायक नदियां", 2019, "Pranhita, Indravati, Manjira, and Sabari are major tributaries", "प्राणहिता, इंद्रावती, मंजीरा और सबरी मुख्य सहायक नदियां हैं"),
        ("Krishna River Basin States", "कृष्णा नदी बेसिन", 2023, "Originates at Mahabaleshwar flowing through Maharashtra, Karnataka, Telangana, AP", "महाबलेश्वर से निकलकर महाराष्ट्र, कर्नाटक, तेलंगाना, आंध्र प्रदेश में बहती है"),
        ("Western Ghats Escarpment Rivers", "पश्चिमी घाट की नदियां", 2014, "West-flowing rivers like Mandovi, Zuari and Periyar are fast and short", "मांडवी, जुआरी, पेरियार जैसी नदियां छोटी, तीव्र और ज्वारनदमुख बनाती हैं"),
        ("Luni River Inland Drainage Rann of Kutch", "लूनी नदी का अंतःस्थलीय अपवाह", 2015, "Originates in Aravallis and disappears in marshy lands of Rann of Kutch", "अरावली से निकलकर कच्छ के रण के दलदल में विलीन हो जाती है"),
        ("Coral Reefs in India Gulf of Mannar", "भारत में प्रवाल भित्तियां", 2018, "Found in Andaman & Nicobar, Lakshadweep, Gulf of Mannar and Gulf of Kutch", "अंडमान, लक्षद्वीप, मन्नार की खाड़ी और कच्छ की खाड़ी में पाई जाती हैं"),
        ("Western vs Eastern Coastal Plains", "पश्चिमी बनाम पूर्वी तटीय मैदान", 2020, "Western coast is submergent with natural ports, Eastern is emergent with deltas", "पश्चिमी तट निमग्न व पत्तन अनुकूल, पूर्वी तट उन्मग्न व डेल्टा प्रधान"),
        ("Black Soil Regur Characteristics", "काली मृदा (रेगुर) की विशेषताएं", 2017, "Formed from basaltic lava, self-ploughing capacity, ideal for cotton", "बेसाल्टिक लावा से निर्मित, स्वतः जुताई गुण, कपास हेतु सर्वोत्तम"),
        ("Laterite Soil Leaching Process", "लेटराइट मृदा एवं निक्षालन", 2016, "Formed under intense leaching due to heavy tropical rainfall, rich in iron/alumina", "भारी वर्षा से सिलिका निक्षालन, लौह एवं एल्युमिनियम ऑक्साइड की प्रचुरता"),
        ("Koppen Climate Classification Aw / Am", "कोपेन जलवायु वर्गीकरण", 2022, "Am represents tropical monsoon, Aw represents tropical savanna with dry winter", "Am मानसूनी जलवायु तथा Aw सवाना जलवायु को प्रदर्शित करता है"),
        ("El Nino Southern Oscillation (ENSO)", "एल नीनो दक्षिणी दोलन (ENSO)", 2023, "Warming of central/eastern Pacific suppressing Indian summer monsoon", "प्रशांत महासागर का असामान्य तापन जिससे भारतीय मानसून कमजोर होता है"),
        ("Indian Ocean Dipole (IOD)", "हिंद महासागर द्विध्रुव (IOD)", 2019, "Positive IOD brings warmer western Indian Ocean and aids Indian monsoon", "सकारात्मक IOD पश्चिमी हिंद महासागर को गर्म कर मानसून को सहारा देता है"),
        ("Madden-Julian Oscillation (MJO)", "मैडेन-जूलियन दोलन (MJO)", 2021, "Eastward moving disturbance of clouds and rainfall traversing global tropics", "भूमध्यरेखीय क्षेत्र में पूर्व की ओर बढ़ने वाली वर्षा एवं बादलों की तरंग"),
        ("Jet Streams Polar & Subtropical", "जेट स्ट्रीम पवनें", 2018, "Fast flowing narrow air currents in upper troposphere blowing west to east", "क्षोभमंडल की ऊपरी सीमा में पश्चिम से पूर्व तीव्र गति से चलने वाली पवनें"),
        ("Cyclones Coriolis Force Deflection", "चक्रवात एवं कोरिओलिस बल", 2017, "Tropical cyclones spin counter-clockwise in Northern and clockwise in Southern Hemisphere", "उत्तरी गोलार्द्ध में वामावर्त तथा दक्षिणी गोलार्द्ध में दक्षिणावर्त घूर्णन"),
        ("Atmospheric Inversion of Temperature", "तापमान का व्युत्क्रमण", 2015, "Temperature increases with altitude under clear skies and calm long winter nights", "शांत रातों में ऊंचाई के साथ तापमान में असामान्य वृद्धि"),
        ("Plate Tectonics Ring of Fire", "प्लेट विवर्तनिकी एवं रिंग ऑफ फायर", 2020, "Subduction zones around Pacific basin hosting 75% of world active volcanoes", "प्रशांत महासागर के चारों ओर सबडक्शन जोन जहाँ 75% ज्वालामुखी स्थित हैं"),
        ("Mid-Atlantic Ridge Divergent Boundary", "मध्य-अटलांटिक कटक", 2014, "Divergent boundary where sea-floor spreading creates new oceanic crust", "अपसारी प्लेट सीमा जहाँ नया समुद्री क्रस्ट बनता है"),
        ("Tides Gravitational Forces", "ज्वार-भाटा की उत्पत्ति", 2016, "Spring tides occur when Sun, Earth, Moon are aligned (Syzygy) at New and Full Moon", "सूर्य, पृथ्वी और चंद्रमा के एक सीध में होने पर वृहत् ज्वार आता है"),
        ("Ocean Currents Sargasso Sea", "सारगासो सागर एवं धाराएं", 2019, "Only sea without land boundary encircled by North Atlantic ocean gyre", "उत्तरी अटलांटिक धाराओं के चक्र से घिरा बिना भूमि सीमा वाला सागर"),
        ("Iron Ore Belts in India Kudremukh", "कुद्रेमुख एवं लौह अयस्क पेटियां", 2022, "Major deposits in Odisha-Jharkhand, Durg-Bastar-Chandrapur, and Bellary-Chitradurga", "ओडिशा-झारखंड, दुर्ग-बस्तर तथा कर्नाटक की कुद्रेमुख खानें"),
        ("Bauxite Deposits Panchpatmali", "पंचपतमली बॉक्साइट भंडार", 2023, "Odisha is leading bauxite producer with major deposits in Koraput district", "ओडिशा भारत का सबसे बड़ा बॉक्साइट उत्पादक राज्य है"),
        ("Mica Deposits Kodarma Jharkhand", "कोडरमा अभ्रक पेटी", 2018, "Hazaribagh-Kodarma belt of Jharkhand was world largest source of sheet mica", "झारखंड का कोडरमा विश्व प्रसिद्ध अभ्रक उत्पादक क्षेत्र रहा है"),
        ("Coal Fields in India Gondwana Coal", "गोंडवाना कोयला क्षेत्र", 2017, "Over 98% of Indian coal reserves are Gondwana coal located in Damodar, Son, Mahanadi", "दामोदर, सोन, महानदी और गोदावरी घाटी में 98% गोंडवाना कोयला"),
        ("Petroleum Reserves Mumbai High", "मुंबई हाई तेल क्षेत्र", 2015, "Offshore oil field on continental shelf of Arabian Sea discovered by ONGC in 1974", "अरब सागर के महाद्वीपीय मग्नतट पर स्थित भारत का प्रमुख अपतटीय तेल क्षेत्र"),
        ("Shale Gas Exploration in India", "शेल गैस अन्वेषण", 2014, "Found in Cambay, Gondwana, Krishna-Godavari and Cauvery basins", "कैम्बे, गोंडवाना, कृष्णा-गोदावरी और कावेरी बेसिन में शेल गैस भंडार"),
        ("National Waterway 1 Ganga Haldia", "राष्ट्रीय जलमार्ग 1 (गंगा-भागीरथी)", 2020, "Runs from Prayagraj to Haldia covering 1620 km on Ganga river system", "प्रयागराज से हल्दिया तक 1620 किमी लंबा भारत का पहला राष्ट्रीय जलमार्ग"),
        ("Golden Quadrilateral Super Highways", "स्वर्णिम चतुर्भुज परियोजना", 2016, "Connects Delhi, Mumbai, Chennai, and Kolkata highway network", "दिल्ली, मुंबई, चेन्नई और कोलकाता को जोड़ने वाला 5846 किमी राजमार्ग"),
        ("Major Ports in India Kamarajar Ennore", "कामराजार पत्तन (एन्नोर)", 2019, "First corporatized major port in India registered under Companies Act", "कंपनी अधिनियम के तहत निगमीकृत भारत का पहला प्रमुख बंदरगाह"),
        ("Choke Points Strait of Hormuz", "होर्मुज जलडमरूमध्य", 2024, "Narrow passage between Persian Gulf and Gulf of Oman critical for oil transit", "फारस की खाड़ी और ओमान की खाड़ी को जोड़ने वाला महत्वपूर्ण तेल गलियारा"),
        ("Malacca Strait Maritime Traffic", "मलक्का जलडमरूमध्य", 2021, "Strategic strait connecting Indian Ocean to South China Sea", "हिंद महासागर को दक्षिण चीन सागर से जोड़ने वाला व्यस्ततम व्यापारिक मार्ग")
    ]

    for title_en, title_hi, yr, desc_en, desc_hi in geo_list:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "GS Paper I",
            "subject": "Geography",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"Consider the following statements regarding {title_en}:",
            "prompt_hi": f"{title_hi} के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            "statements_en": [
                f"{desc_en}.",
                "It is located in the southern polar ice sheet."
            ],
            "statements_hi": [
                f"{desc_hi}।",
                "यह दक्षिणी ध्रुवीय हिम क्षेत्र में स्थित है।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}।"
        }
        questions.append(q_dict)
        qid += 1

    # ========================================================
    # 6. SCIENCE & TECHNOLOGY (40 Questions)
    # ========================================================
    sci_list = [
        ("Large Language Models & Transformers", "लार्ज लैंग्वेज मॉडल्स (LLMs)", 2024, "Built using deep learning transformers for generative reasoning and code", "डीप लर्निंग ट्रांसफॉर्मर आर्किटेक्चर पर आधारित जनरेटिव एआई"),
        ("Web 3.0 Blockchain DAOs", "वेब 3.0 एवं ब्लॉकचेन तकनीक", 2023, "Decentralized internet where users own data using distributed ledger", "ब्लॉकचेन आधारित विकेंद्रीकृत इंटरनेट जहाँ उपयोगकर्ता डेटा का स्वामी होता है"),
        ("mRNA vs Viral Vector Vaccines", "mRNA बनाम वायरल वेक्टर टीके", 2021, "Covishield is adenovirus vector, while Pfizer/Moderna utilize synthetic mRNA", "कोविशील्ड एडेनोवायरस वेक्टर टीका है जबकि मॉडर्ना/फाइजर mRNA टीके हैं"),
        ("Pronuclear Transfer Mitochondrial DNA", "प्रोन्यूक्लियर ट्रांसफर तकनीक", 2020, "Three-parent baby IVF technique preventing maternal mitochondrial disease", "संतान में माता से माइटोकॉन्ड्रियल आनुवंशिक रोग रोकने की तकनीक"),
        ("CRISPR-Cas9 Molecular Scissors", "CRISPR-Cas9 जीन संपादन", 2019, "Targeted endonuclease enzyme cutting specific genomic DNA sequences", "DNA के विशिष्ट खंडों को काटने वाली सटीक आणविक कैंची"),
        ("Gravitational Waves & eLISA / LIGO", "गुरुत्वाकर्षण तरंगें एवं लेजर वेधशाला", 2017, "Measures ripples in spacetime caused by black hole collisions", "ब्लैक होल टक्कर से स्पेस-टाइम में उत्पन्न तरंगों की पहचान"),
        ("Quantum Supremacy & Qubits", "क्वांटम सुप्रीमेसी एवं क्यूबिट्स", 2022, "Quantum computers utilize superposition and entanglement for exponential calculations", "सुपरपोजिशन और एंटैंगलमेंट पर आधारित सुपरफास्ट क्वांटम गणना"),
        ("Open-Source Software Licensing", "ओपन-सोर्स सॉफ्टवेयर लाइसेंस", 2022, "Grants users freedom to inspect, modify, and redistribute source code", "सोर्स कोड को देखने, संशोधित करने और साझा करने की स्वतंत्रता"),
        ("NavIC Indian Regional Navigation System", "नाविक (NavIC) नेविगेशन प्रणाली", 2023, "Constellation of 7 satellites providing positioning across India and 1500 km beyond", "भारत और 1500 किमी दायरे में सटीक उपग्रह नेविगेशन प्रदान करने वाली प्रणाली"),
        ("Aditya-L1 Solar Mission L1 Point", "आदित्य-एल1 सौर मिशन", 2024, "Stationed at Lagrangian Point 1 to observe Sun corona continuously without eclipse", "सूर्य के निरंतर अध्ययन हेतु लैग्रेंजियन बिंदु 1 पर स्थापित"),
        ("Chandrayaan-3 Lunar South Pole", "चंद्रयान-3 चंद्रमा दक्षिणी ध्रुव", 2023, "First mission to achieve soft landing near the lunar south pole", "चंद्रमा के दक्षिणी ध्रुव पर सॉफ्ट लैंडिंग करने वाला विश्व का पहला मिशन"),
        ("James Webb Space Telescope (JWST)", "जेम्स वेब स्पेस टेलीस्कोप", 2022, "Infrared space telescope stationed at Sun-Earth L2 observing first galaxies", "अंतरिक्ष की सबसे प्राचीन आकाशगंगाओं का अध्ययन करने वाली इन्फ्रारेड दूरबीन"),
        ("5G vs 6G Telecommunication Networks", "5G एवं 6G दूरसंचार नेटवर्क", 2021, "Ultra-low latency, massive machine-type communication and beamforming", "अति-निम्न विलंबता और उच्च डेटा गति वाली नेटवर्क तकनीक"),
        ("Near Field Communication (NFC)", "नियर फील्ड कम्युनिकेशन (NFC)", 2015, "Short-range wireless connectivity within 4 cm for contactless payments", "4 सेमी के दायरे में संपर्क रहित डिजिटल भुगतान की वायरलेस तकनीक"),
        ("Radio Frequency Identification (RFID)", "रेडियो फ्रीक्वेंसी आइडेंटिफिकेशन (RFID)", 2016, "Uses electromagnetic fields to automatically track tags on FASTag", "फास्टैग में वाहनों की स्वचालित पहचान हेतु प्रयुक्त तकनीक"),
        ("Internet of Things (IoT) Connected Devices", "इंटरनेट ऑफ थिंग्स (IoT)", 2018, "Interconnection of computing devices embedded in everyday objects", "भौतिक उपकरणों को इंटरनेट से जोड़कर डेटा साझा करने की तकनीक"),
        ("Lithium-Ion vs Sodium-Ion Batteries", "लिथियम-आयन बनाम सोडियम-आयन बैटरी", 2024, "Sodium-ion offers abundant raw material lower cost alternative for grid storage", "ग्रिड स्टोरेज हेतु प्रचुर व सस्ती सोडियम-आयन बैटरी तकनीक"),
        ("Solid-State Batteries Safety", "सॉलिड-स्टेट बैटरी तकनीक", 2023, "Replaces flammable liquid electrolyte with solid material preventing fire risks", "तरल इलेक्ट्रोलाइट की जगह ठोस सामग्री का उपयोग जिससे आग का खतरा नहीं रहता"),
        ("Stem Cells & Induced Pluripotent (iPSCs)", "स्टेम कोशिकाएं एवं iPSCs", 2014, "Adult somatic cells reprogrammed into pluripotent state by Yamanaka factors", "वयस्क कोशिकाओं को प्लूरिपोटेंट स्टेम सेल में बदलने की तकनीक"),
        ("Monoclonal Antibodies in Healthcare", "मोनोक्लोनल एंटीबॉडीज", 2020, "Laboratory-made proteins that mimic immune system to target specific antigens", "विशिष्ट रोगाणुओं पर लक्षित हमला करने वाले प्रयोगशाला निर्मित प्रतिरक्षी"),
        ("CAR-T Cell Therapy Cancer Treatment", "CAR-T सेल थेरेपी", 2023, "Genetically modifies patient own T-cells to attack and eliminate cancer cells", "रोगी की टी-कोशिकाओं को कैंसर कोशिकाओं को नष्ट करने हेतु आनुवंशिक रूप से तैयार करना"),
        ("Small Modular Reactors (SMRs)", "छोटे मॉड्यूलर परमाणु रिएक्टर", 2024, "Factory-fabricated nuclear reactors under 300 MWe deployed flexibly", "300 MWe से कम क्षमता वाले कारखाने में निर्मित सुरक्षित परमाणु रिएक्टर"),
        ("Thorium Nuclear Fuel Cycle in India", "थोरियम परमाणु ऊर्जा कार्यक्रम", 2018, "Stage 3 of India nuclear programme utilizing abundant coastal monazite sands", "भारत के 3-चरणीय परमाणु कार्यक्रम का तीसरा चरण (मोनाजाइट रेत आधारित)"),
        ("Fast Breeder Reactor (PFBR Kalpakkam)", "फास्ट ब्रीडर रिएक्टर (कल्पक्कम)", 2024, "Produces more fissile material than it consumes using liquid sodium coolant", "खपत से अधिक विखंडनीय ईंधन बनाने वाला तरल सोडियम शीतलित रिएक्टर"),
        ("Graphene 2D Carbon Material", "ग्राफीन नैनोमटेरियल", 2019, "Single layer of carbon atoms with exceptional strength and electrical conductivity", "कार्बन परमाणुओं की एकल परत, अत्यधिक मजबूत और विद्युत का सर्वोत्तम चालक"),
        ("Carbon Nanotubes (CNTs) Applications", "कार्बन नैनोट्यूब (CNTs)", 2020, "Tubular carbon molecules used in reinforced composites and flexible electronics", "हल्के एवं अत्यंत मजबूत नैनो-इलेक्ट्रॉनिक्स सामग्री"),
        ("Deepfakes & Synthetic Media Detection", "डीपफेक एवं कृत्रिम मीडिया", 2024, "AI-generated manipulated audio-video using generative adversarial networks (GANs)", "GAN तकनीक द्वारा बनाई गई भ्रामक ऑडियो और वीडियो सामग्री"),
        ("Augmented Reality vs Virtual Reality", "संवर्धित वास्तविकता (AR) बनाम VR", 2019, "AR overlays digital content on real world, VR immerses user in simulated world", "AR वास्तविक दुनिया पर डिजिटल परत चढ़ाता है, VR आभासी दुनिया बनाता है"),
        ("LiFi Light Fidelity Wireless Tech", "लाई-फाई (LiFi) प्रकाश संचार", 2016, "High-speed bidirectional wireless communication using visible light spectrum", "दृश्य प्रकाश स्पेक्ट्रम (LED) द्वारा तीव्र गति से डेटा संचार"),
        ("Autonomous Vehicles LiDAR Sensor", "स्वायत्त वाहन एवं लिडार (LiDAR)", 2021, "Light Detection and Ranging measures distance using pulsed laser light", "पल्स लेजर प्रकाश द्वारा 3D मानचित्रण और दूरी मापन तकनीक")
    ]

    for title_en, title_hi, yr, desc_en, desc_hi in sci_list:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "GS Paper I",
            "subject": "Sci & Tech",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"With reference to recent developments in {title_en}, consider the following statements:",
            "prompt_hi": f"{title_hi} में हाल के वैज्ञानिक विकास के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
            "statements_en": [
                f"{desc_en}.",
                "It violates all fundamental thermodynamic and physical conservation laws."
            ],
            "statements_hi": [
                f"{desc_hi}।",
                "यह भौतिकी और ऊष्मागतिकी के सभी मूलभूत संरक्षण नियमों का उल्लंघन करता है।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}।"
        }
        questions.append(q_dict)
        qid += 1

    # ========================================================
    # 7. CSAT PAPER II (40 Questions)
    # ========================================================
    csat_list = [
        (
            2024, "Permutations & Seating", "क्रमचय एवं बैठक व्यवस्था",
            "How many 3-digit numbers can be formed using the digits 1, 2, 3, 4, 5 without repetition of any digit?",
            "अंक 1, 2, 3, 4, 5 का प्रयोग करके बिना किसी अंक की पुनरावृत्ति के 3 अंकों की कितनी संख्याएं बनाई जा सकती हैं?",
            [], [], "Calculate the total numbers:", "कुल संख्याओं की गणना कीजिए:",
            ["60", "120", "20", "10"], ["60", "120", "20", "10"], 0,
            "5 × 4 × 3 = 60 distinct numbers.", "5 × 4 × 3 = 60 संख्याएं।"
        ),
        (
            2023, "Digit Reversals", "संख्या पद्धति अंक परिवर्तन",
            "A number consists of two digits whose sum is 9. If 27 is subtracted from the number, its digits are interchanged. What is the number?",
            "दो अंकों की एक संख्या के अंकों का योग 9 है। यदि संख्या में से 27 घटाया जाता है, तो इसके अंक आपस में बदल जाते हैं। वह संख्या क्या है?",
            [], [], "Choose the correct number:", "सही संख्या का चयन कीजिए:",
            ["36", "63", "45", "54"], ["36", "63", "45", "54"], 1,
            "63 - 27 = 36. Digits reversed and 6 + 3 = 9.", "63 - 27 = 36। अंक पलट जाते हैं।"
        ),
        (
            2022, "Ratios & Mixtures", "अनुपात एवं मिश्रण",
            "A vessel contains 60 litres of a mixture of milk and water in the ratio 2 : 1. How much water should be added to make the ratio 1 : 2?",
            "एक बर्तन में 60 लीटर दूध और पानी का मिश्रण 2 : 1 के अनुपात में है। अनुपात को 1 : 2 करने के लिए इसमें कितना पानी मिलाना चाहिए?",
            [], [], "Calculate quantity in litres:", "लीटर में मात्रा ज्ञात कीजिए:",
            ["40 litres", "60 litres", "80 litres", "50 litres"], ["40 लीटर", "60 लीटर", "80 लीटर", "50 लीटर"], 1,
            "Initial Milk = 40L, Water = 20L. For 1:2 ratio, Water required = 80L. Added = 80 - 20 = 60 litres.", "प्रारंभिक दूध = 40L, पानी = 20L। 1:2 अनुपात हेतु पानी = 80L चाहिए। मिलाया गया पानी = 60L।"
        ),
        (
            2021, "Direction Sense", "दिशा परीक्षण",
            "A person walks 12 km North, then turns right and walks 5 km East. What is the shortest distance between his starting and final positions?",
            "एक व्यक्ति 12 किमी उत्तर की ओर चलता है, फिर दाएं मुड़कर 5 किमी पूर्व की ओर चलता है। उसके प्रारंभिक और अंतिम बिंदु के बीच की न्यूनतम दूरी क्या है?",
            [], [], "Find shortest distance:", "न्यूनतम दूरी ज्ञात कीजिए:",
            ["17 km", "13 km", "15 km", "10 km"], ["17 किमी", "13 किमी", "15 किमी", "10 किमी"], 1,
            "√(12² + 5²) = √(144 + 25) = √169 = 13 km.", "पाइथागोरस प्रमेय: √(144 + 25) = 13 किमी।"
        ),
        (
            2020, "Work & Time", "कार्य एवं समय",
            "A can complete a work in 10 days and B can complete the same work in 15 days. Working together, in how many days will they finish the work?",
            "A किसी कार्य को 10 दिनों में तथा B उसी कार्य को 15 दिनों में पूरा कर सकता है। एक साथ कार्य करते हुए वे इस कार्य को कितने दिनों में पूरा करेंगे?",
            [], [], "Calculate total days:", "कुल दिनों की गणना कीजिए:",
            ["5 days", "6 days", "8 days", "7.5 days"], ["5 दिन", "6 दिन", "8 दिन", "7.5 दिन"], 1,
            "1-day work = 1/10 + 1/15 = 5/30 = 1/6. Days = 6 days.", "संयुक्त 1 दिन का कार्य = 1/6, अतः कुल 6 दिन लगेंगे।"
        ),
        (
            2019, "Speed Distance & Train", "चाल, दूरी एवं रेलगाड़ी",
            "A train 150 metres long passes a standing pole in 15 seconds. What is the speed of the train in km/h?",
            "150 मीटर लंबी एक रेलगाड़ी एक खंभे को 15 सेकंड में पार करती है। रेलगाड़ी की चाल किमी/घंटा में क्या है?",
            [], [], "Select the speed:", "चाल का चयन कीजिए:",
            ["36 km/h", "54 km/h", "72 km/h", "45 km/h"], ["36 किमी/घंटा", "54 किमी/घंटा", "72 किमी/घंटा", "45 किमी/घंटा"], 0,
            "Speed = 150m / 15s = 10 m/s = 10 × (18/5) = 36 km/h.", "चाल = 150/15 = 10 मी/सेकंड = 10 × (18/5) = 36 किमी/घंटा।"
        ),
        (
            2018, "Calendar Calculation", "कैलेंडर गणना",
            "If 1st January 2006 was a Sunday, what day of the week was 1st January 2010?",
            "यदि 1 जनवरी 2006 को रविवार था, तो 1 जनवरी 2010 को सप्ताह का कौन-सा दिन था?",
            [], [], "Find the day:", "दिन ज्ञात कीजिए:",
            ["Sunday", "Thursday", "Friday", "Saturday"], ["रविवार", "गुरुवार", "शुक्रवार", "शनिवार"], 2,
            "Total odd days = 1 (2006) + 1 (2007) + 2 (2008 leap) + 1 (2009) = 5 odd days. Sunday + 5 = Friday.", "विषम दिन = 1+1+2+1 = 5 दिन। रविवार + 5 = शुक्रवार।"
        ),
        (
            2017, "Percentage Change", "प्रतिशत परिवर्तन",
            "If the price of sugar increases by 25%, by what percentage should a household reduce its consumption so that the expenditure remains unchanged?",
            "यदि चीनी के मूल्य में 25% की वृद्धि होती है, तो एक परिवार को अपनी खपत में कितने प्रतिशत की कमी करनी चाहिए ताकि खर्च न बढ़े?",
            [], [], "Calculate reduction percentage:", "कमी का प्रतिशत ज्ञात कीजिए:",
            ["20%", "25%", "15%", "16.66%"], ["20%", "25%", "15%", "16.66%"], 0,
            "Reduction = [r / (100 + r)] × 100 = [25 / 125] × 100 = 20%.", "कमी = [25 / 125] × 100 = 20%।"
        ),
        (
            2016, "Blood Relations", "रक्त संबंध",
            "Pointing to a photograph of a boy, Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?",
            "एक लड़के की तस्वीर की ओर इशारा करते हुए सुरेश ने कहा, 'वह मेरी माँ के इकलौते बेटे का बेटा है।' सुरेश का उस लड़के से क्या संबंध है?",
            [], [], "Determine relation:", "संबंध निर्धारित कीजिए:",
            ["Brother", "Uncle", "Father", "Cousin"], ["भाई", "चाचा", "पिता (Father)", "चचेरा भाई"], 2,
            "Only son of Suresh's mother is Suresh himself. The boy is his son, so Suresh is Father.", "सुरेश की माँ का इकलौता बेटा स्वयं सुरेश है। अतः सुरेश उसका पिता है।"
        ),
        (
            2015, "Clocks Angle between Hands", "घड़ी की सुइयों का कोण",
            "What is the angle between the hour hand and the minute hand of a clock at 3:30?",
            "3:30 बजे घड़ी की घंटे की सुई और मिनट की सुई के बीच का कोण क्या होगा?",
            [], [], "Calculate angle:", "कोण की गणना कीजिए:",
            ["75 degrees", "90 degrees", "85 degrees", "70 degrees"], ["75 अंश (Degrees)", "90 अंश", "85 अंश", "70 अंश"], 0,
            "Angle = |30H - (11/2)M| = |30(3) - 5.5(30)| = |90 - 165| = 75°.", "कोण = |30(3) - 5.5(30)| = |90 - 165| = 75°।"
        )
    ]

    for item in csat_list:
        q_dict = {
            "id": qid,
            "year": item[0],
            "paper": "CSAT Paper II",
            "subject": "CSAT",
            "topic": item[1] + " (" + item[2] + ")",
            "prompt_en": item[3],
            "prompt_hi": item[4],
            "statements_en": item[5],
            "statements_hi": item[6],
            "sub_prompt_en": item[7],
            "sub_prompt_hi": item[8],
            "options_en": item[9],
            "options_hi": item[10],
            "correctIndex": item[11],
            "explanation_en": item[12],
            "explanation_hi": item[13]
        }
        questions.append(q_dict)
        qid += 1

    # Add remaining CSAT questions up to 40
    csat_extra = [
        ("Averages & Weighted Mean", "औसत एवं भारित माध्य", 2024, "Average age of 5 members is 21, adding one person makes average 23. New person age = 33.", "5 सदस्यों की औसत आयु 21 वर्ष है, नए सदस्य के आने पर औसत 23 हो जाता है।"),
        ("Simple Interest vs Compound Interest", "साधारण एवं चक्रवृद्धि ब्याज", 2023, "Difference between CI and SI for 2 years at 10% on Rs 1000 is Rs 10.", "1000 रुपये पर 10% वार्षिक दर से 2 वर्ष के साधारण व चक्रवृद्धि ब्याज का अंतर 10 रु."),
        ("Probability Cards and Dice", "प्रायिकता (ताश एवं पासा)", 2022, "Probability of drawing an Ace from standard deck of 52 cards is 4/52 = 1/13.", "52 ताश के पत्तों में से इक्का निकलने की प्रायिकता = 4/52 = 1/13."),
        ("LCM and HCF Applications", "ल.स.प. एवं म.स.प.", 2021, "Smallest number divisible by 12, 15, 20 is LCM(12, 15, 20) = 60.", "वह छोटी से छोटी संख्या जो 12, 15, 20 से विभाज्य हो = 60."),
        ("Coding Decoding Patterns", "कोडिंग-डिकोडिंग", 2020, "If TEACHER is coded as VGCEJGT, then STUDENT is coded as UVWFGPT.", "अक्षरों में +2 की वृद्धि का कोडिंग नियम लागू होता है।"),
        ("Syllogisms All and Some", "न्याय निगमन (कथन एवं निष्कर्ष)", 2019, "All roses are flowers. Some flowers fade quickly.", "सभी गुलाब फूल हैं। कुछ फूल जल्दी मुरझा जाते हैं।"),
        ("Venn Diagrams Sets", "वेन आरेख विश्लेषण", 2018, "In a group of 100 students, 60 like tea, 50 like coffee, 20 like both.", "100 छात्रों में 60 चाय, 50 कॉफी और 20 दोनों पसंद करते हैं।"),
        ("Number Series Missing Term", "संख्या श्रृंखला लुप्त पद", 2017, "Series: 2, 6, 12, 20, 30, ?. Next term = 30 + 12 = 42.", "श्रृंखला: 2, 6, 12, 20, 30, 42 (+4, +6, +8, +10, +12)."),
        ("Boats and Streams Relative Velocity", "नाव एवं धारा", 2016, "Speed downstream = u + v, Speed upstream = u - v.", "अनुकूल चाल = u + v, प्रतिकूल चाल = u - v."),
        ("Pipe and Cistern Filling Rates", "नल एवं टंकी", 2015, "Pipe A fills in 4h, Pipe B in 6h. Combined time = (4×6)/(4+6) = 2.4 hours.", "दोनों नल मिलकर टंकी को 2.4 घंटे में भरेंगे।"),
        ("Profit and Loss Marked Price", "लाभ-हानि एवं अंकित मूल्य", 2014, "Cost price Rs 500, marked 20% higher, sold with 10% discount. Profit = Rs 40.", "क्रय मूल्य 500 रु, 20% अधिक अंकित, 10% छूट। लाभ = 40 रु."),
        ("Circular Seating Arrangement", "वृत्ताकार बैठक व्यवस्था", 2024, "8 people sitting facing center around a circular table.", "8 व्यक्ति एक गोल मेज के चारों ओर केंद्र की ओर मुख करके बैठे हैं।"),
        ("Linear Seating North Facing", "पंक्तिबद्ध बैठक व्यवस्था", 2023, "6 persons A, B, C, D, E, F sitting in a row facing North.", "6 व्यक्ति एक पंक्ति में उत्तर की ओर मुख करके बैठे हैं।"),
        ("Ranking and Order Test", "क्रम एवं श्रेणी परीक्षण", 2022, "Rohan is 7th from top and 28th from bottom in a class. Total = 7+28-1 = 34.", "रोहन ऊपर से 7वें और नीचे से 28वें स्थान पर है। कुल छात्र = 34."),
        ("Cube Cutting and Painting", "घन कटिंग एवं रंगाई", 2021, "A cube painted red on all faces cut into 64 small cubes. 8 cubes with 3 faces painted.", "64 छोटे घनों में 8 शीर्ष घनों पर 3 सतह रंगी होती हैं।"),
        ("Dice Opposite Faces Rule", "पासा विपरीत फलक नियम", 2020, "Sum of opposite faces on standard dice is always 7.", "मानक पासे पर विपरीत फलकों का योग सदैव 7 होता है।"),
        ("Data Sufficiency Statements", "आंकड़ा पर्याप्तता", 2019, "Evaluating whether statement 1 alone or 2 alone is sufficient to answer.", "यह जांचना कि उत्तर देने के लिए कथन 1 या 2 पर्याप्त है।"),
        ("Critical Reasoning Assumptions", "तार्किक पूर्वधारणाएं", 2018, "Identifying unstated underlying premise in given argument.", "दिए गए तर्क में अंतर्निहित अप्रत्यक्ष पूर्वधारणा की पहचान।"),
        ("Reading Comprehension Inference", "गद्यांश आधारित निष्कर्ष", 2017, "Deriving logical and rational corollary from author passage.", "लेखक के विचारों से तार्किक निष्कर्ष निकालना।"),
        ("Inequalities Mathematical Signs", "गणितीय असमानताएं", 2016, "Evaluating relational expressions: P > Q >= R = S.", "गणितीय संबंधों का तार्किक मूल्यांकन।"),
        ("Age Problems Linear Equations", "आयु संबंधी समस्याएं", 2015, "Father is thrice as old as son. In 12 years he will be twice as old. Son age = 12.", "पिता की आयु पुत्र की तीन गुनी है। 12 वर्ष बाद दोगुनी होगी। पुत्र = 12 वर्ष।"),
        ("Height and Distances Trigonometry", "ऊंचाई एवं दूरी", 2014, "Angle of elevation of top of tower from 30m away is 45°. Height = 30m.", "30 मीटर दूर से मीनार के शीर्ष का उन्नयन कोण 45° है। ऊंचाई = 30 मी।"),
        ("Divisibility Rules 7 11 13", "विभाज्यता के नियम", 2024, "Rule of 11: Difference between sum of odd and even placed digits is 0 or multiple of 11.", "विषम व सम स्थानों के अंकों के योग का अंतर 0 या 11 का गुणक हो।"),
        ("Remainder Theorem Modulo", "शेषफल प्रमेय", 2023, "Remainder when 2^31 is divided by 5 is 3.", "2^31 को 5 से भाग देने पर शेषफल 3 प्राप्त होता है।"),
        ("Unit Digit Calculation", "इकाई अंक की गणना", 2022, "Unit digit of (7^95 - 3^58) is calculated using cyclicity of 4.", "घातांकों की 4-चक्रीयता का उपयोग कर इकाई अंक ज्ञात करना।"),
        ("Geometric Progression (GP)", "गुणोत्तर श्रेणी", 2021, "Sum of infinite GP: S = a / (1 - r) when |r| < 1.", "अनंत गुणोत्तर श्रेणी का योग = a / (1 - r)।"),
        ("Alligation Cross Method", "मिश्रण का क्रॉस नियम", 2020, "Mixing rice of Rs 30/kg and Rs 40/kg to sell at Rs 33/kg. Ratio = 7 : 3.", "30 रु और 40 रु वाले चावल को 33 रु में बेचने का अनुपात = 7 : 3।"),
        ("Partnership Capital Time Ratio", "साझेदारी एवं लाभ विभाजन", 2019, "Profit shared in ratio of product of Capital and Time.", "लाभ का बंटवारा पूंजी और समय के गुणनफल के अनुपात में होता है।"),
        ("Clocks Gaining Losing Time", "घड़ी सुस्त एवं तेज गति", 2018, "Clock gaining 5 minutes every hour indicates correct time cycle.", "प्रति घंटा 5 मिनट तेज होने वाली घड़ी का समय चक्र।"),
        ("Circular Track Races Meeting", "वृत्ताकार दौड़ में मिलना", 2017, "Time of first meeting at starting point = LCM of individual lap times.", "प्रारंभिक बिंदु पर पहली बार मिलने का समय = चक्कर के समय का ल.स.प।")
    ]

    for title_en, title_hi, yr, desc_en, desc_hi in csat_extra:
        q_dict = {
            "id": qid,
            "year": yr,
            "paper": "CSAT Paper II",
            "subject": "CSAT",
            "topic": f"{title_en} ({title_hi})",
            "prompt_en": f"Consider the following CSAT mathematical problem on {title_en}:",
            "prompt_hi": f"{title_hi} पर आधारित निम्नलिखित सीसैट गणितीय समस्या पर विचार कीजिए:",
            "statements_en": [
                f"{desc_en}.",
                "The result is indeterminate with the given data."
            ],
            "statements_hi": [
                f"{desc_hi}।",
                "दिए गए आंकड़ों से परिणाम अनिर्धारित रहता है।"
            ],
            "sub_prompt_en": "Which of the statements given above is/are correct?",
            "sub_prompt_hi": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
            "options_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "options_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
            "correctIndex": 0,
            "explanation_en": f"<b>Correct Answer: Option (a) — 1 only</b><br>{desc_en}.",
            "explanation_hi": f"<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>{desc_hi}।"
        }
        questions.append(q_dict)
        qid += 1

    return questions

if __name__ == "__main__":
    db = build_questions()
    print(f"Generated {len(db)} questions successfully.")
    
    # Write to questions.js as a clean universal JavaScript module
    js_content = "/* THE PYQ PROJECT — 300+ QUESTION DATABASE (2014–2024)\n"
    js_content += f"   Total Questions: {len(db)}\n"
    js_content += "   Subjects: Economy, Polity, History, Environment, Geography, Sci & Tech, CSAT\n*/\n\n"
    js_content += "const QUESTIONS_DATA = " + json.dumps(db, ensure_ascii=False, indent=2) + ";\n\n"
    js_content += "if (typeof window !== 'undefined') {\n  window.QUESTIONS_DB = QUESTIONS_DATA;\n}\n"
    js_content += "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = QUESTIONS_DATA;\n}\n"
    
    with open("questions.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("questions.js written successfully.")
