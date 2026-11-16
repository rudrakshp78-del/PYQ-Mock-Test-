/* THE PYQ PROJECT — LAST 10 YEARS COMPREHENSIVE UPSC PRELIMS QUESTION DATABASE (2014–2024)
   SUBJECTS COVERED:
   1. Economy (भारतीय अर्थव्यवस्था)
   2. Polity / Politics (भारतीय राजव्यवस्था)
   3. History (भारत का इतिहास एवं कला-संस्कृति)
   4. Environment (पर्यावरण एवं पारिस्थितिकी)
   5. Geography (भारत एवं विश्व का भूगोल)
   6. Science & Tech (विज्ञान एवं प्रौद्योगिकी)
   7. CSAT (सीसैट - पेपर II)
*/

// UNIVERSAL EXPORT (Browser + Node)
const QUESTIONS_DATA = [
  // ==========================================
  // 1. POLITY (भारतीय राजव्यवस्था)
  // ==========================================
  {
    id: 101,
    year: 2024,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Delimitation Commission (परिसीमन आयोग)",
    prompt_en: "With reference to the Delimitation Commission in India, consider the following statements:",
    prompt_hi: "भारत में परिसीमन आयोग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "The orders of the Delimitation Commission cannot be challenged in any court of law.",
      "The Delimitation Commission orders come into force on a date specified by the President of India."
    ],
    statements_hi: [
      "परिसीमन आयोग के आदेशों को किसी भी न्यायालय में चुनौती नहीं दी जा सकती है।",
      "परिसीमन आयोग के आदेश भारत के राष्ट्रपति द्वारा निर्दिष्ट तिथि से प्रभावी होते हैं।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Article 329(a) bars the interference of courts in electoral matters including delimitation. The orders come into force on a date notified by the President.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>संविधान के अनुच्छेद 329(a) के अनुसार परिसीमन आयोग के आदेशों को किसी न्यायालय में चुनौती नहीं दी जा सकती तथा ये राष्ट्रपति द्वारा अधिसूचित तिथि से प्रभावी होते हैं।"
  },
  {
    id: 102,
    year: 2023,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Lapsing of Bills (विधेयकों का व्यपगत होना)",
    prompt_en: "With reference to the Parliament of India, consider the following statements:",
    prompt_hi: "भारत की संसद के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "A bill pending in the Rajya Sabha which has not been passed by the Lok Sabha shall not lapse on dissolution of the Lok Sabha.",
      "A bill pending in the Lok Sabha shall not lapse on dissolution if the President has notified intention to summon a joint sitting."
    ],
    statements_hi: [
      "राज्य सभा में लंबित विधेयक, जिसे लोक सभा ने पारित नहीं किया है, लोक सभा के विघटन पर व्यपगत नहीं होगा।",
      "लोक सभा में लंबित कोई विधेयक विघटन पर व्यपगत नहीं होगा, यदि राष्ट्रपति ने संयुक्त बैठक बुलाने की मंशा अधिसूचित कर दी हो।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Articles 107(4) and 108(5) explicitly protect these categories of pending bills from lapsing upon Lok Sabha dissolution.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>संविधान के अनुच्छेद 107(4) एवं 108(5) के तहत ऐसे विधेयक लोक सभा के विघटन पर व्यपगत नहीं होते।"
  },
  {
    id: 103,
    year: 2022,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Contempt of Court (न्यायालय की अवमानना)",
    prompt_en: "With reference to the Contempt of Courts Act, 1971 in India, consider the following statements:",
    prompt_hi: "भारत में न्यायालय की अवमानना अधिनियम, 1971 के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "Civil contempt means wilful disobedience to any judgment, decree, direction, or order of a court.",
      "Criminal contempt includes publication of any matter which scandalizes or lowers the authority of any court."
    ],
    statements_hi: [
      "नागरिक (सिविल) अवमानना का अर्थ न्यायालय के किसी निर्णय, डिक्री, आदेश या निर्देश की जानबूझकर अवज्ञा करना है।",
      "आपराधिक अवमानना में किसी ऐसी बात का प्रकाशन शामिल है जो न्यायालय के प्राधिकार को कलंकित या कम करता है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>The Contempt of Courts Act, 1971 divides contempt into Civil Contempt (wilful disobedience) and Criminal Contempt (scandalizing the court).",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>न्यायालय की अवमानना अधिनियम 1971 की धारा 2 के अनुसार सिविल और आपराधिक अवमानना दोनों की ये सटीक परिभाषाएँ हैं।"
  },
  {
    id: 104,
    year: 2021,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Article 14 & Arbitrary Power (अनुच्छेद 14 एवं मनमानी शक्तियां)",
    prompt_en: "A legislation which confers on the executive or administrative authority an unguided and uncontrolled discretionary power in the matter of application of law violates which one of the following Articles of the Constitution of India?",
    prompt_hi: "कोई ऐसा कानून जो कार्यपालिका या प्रशासनिक प्राधिकारी को कानून के प्रयोग के मामले में अनियंत्रित और अनिर्देशित विवेकाधीन शक्ति प्रदान करता है, भारतीय संविधान के किस अनुच्छेद का उल्लंघन करता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the correct Article:",
    sub_prompt_hi: "सही अनुच्छेद का चयन कीजिए:",
    options_en: ["Article 14", "Article 28", "Article 32", "Article 44"],
    options_hi: ["अनुच्छेद 14", "अनुच्छेद 28", "अनुच्छेद 32", "अनुच्छेद 44"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — Article 14</b><br>Unguided and arbitrary executive discretion violates the rule of law and equality before the law embodied under Article 14.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — अनुच्छेद 14</b><br>विधि के समक्ष समता और विधि के शासन (Rule of Law) के तहत अनियंत्रित विवेकाधिकार को मनमाना मानकर अनुच्छेद 14 का उल्लंघन माना जाता है।"
  },
  {
    id: 105,
    year: 2020,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Right to Property / Art 300A (संपत्ति का अधिकार)",
    prompt_en: "In India, what is the legal status of the 'Right to Property'?",
    prompt_hi: "भारत में 'संपत्ति के अधिकार' की क्या विधिक स्थिति है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct legal status:",
    sub_prompt_hi: "सही विधिक स्थिति का चयन कीजिए:",
    options_en: ["Fundamental Right available to citizens only", "Legal right available to any person", "Fundamental Right available to any person", "Neither a fundamental right nor a legal right"],
    options_hi: ["केवल नागरिकों को प्राप्त मूल अधिकार", "किसी भी व्यक्ति को प्राप्त विधिक अधिकार", "किसी भी व्यक्ति को प्राप्त मूल अधिकार", "न तो मूल अधिकार और न ही विधिक अधिकार"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Legal right available to any person</b><br>By the 44th Constitutional Amendment Act 1978, Right to Property was removed from Part III and made a constitutional/legal right under Article 300A for any person.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — किसी भी व्यक्ति को प्राप्त विधिक अधिकार</b><br>44वें संविधान संशोधन 1978 द्वारा इसे मूल अधिकार से हटाकर अनुच्छेद 300A के तहत विधिक अधिकार बना दिया गया।"
  },
  {
    id: 106,
    year: 2019,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Governor's Discretionary Powers (राज्यपाल के विवेकाधिकार)",
    prompt_en: "Which of the following are the discretionary powers given to the Governor of a State under the Constitution?",
    prompt_hi: "संविधान के अंतर्गत किसी राज्य के राज्यपाल को निम्नलिखित में से कौन-सी विवेकाधीन शक्तियां प्रदान की गई हैं?",
    statements_en: [
      "Sending a report to the President for recommending President's Rule under Article 356.",
      "Reserving certain bills passed by the State Legislature for the consideration of the President."
    ],
    statements_hi: [
      "अनुच्छेद 356 के तहत राष्ट्रपति शासन की सिफारिश करने हेतु राष्ट्रपति को रिपोर्ट भेजना।",
      "राज्य विधानमंडल द्वारा पारित कुछ विधेयकों को राष्ट्रपति के विचारार्थ आरक्षित करना।"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Recommending President's Rule (Art 356) and reserving bills under Art 200 are constitutional discretionary powers of the Governor.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>अनुच्छेद 356 की रिपोर्ट भेजना और अनुच्छेद 200 के तहत विधेयक आरक्षित करना राज्यपाल के संवैधानिक विवेकाधिकार हैं।"
  },
  {
    id: 107,
    year: 2018,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Right to Privacy / Art 21 (निजता का अधिकार)",
    prompt_en: "The Right to Privacy is protected as an intrinsic part of the Right to Life and Personal Liberty under which Article of the Constitution of India?",
    prompt_hi: "निजता का अधिकार (Right to Privacy) भारत के संविधान के किस अनुच्छेद के तहत जीवन और व्यक्तिगत स्वतंत्रता के अधिकार के भाग के रूप में संरक्षित है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the Article:",
    sub_prompt_hi: "अनुच्छेद का चयन कीजिए:",
    options_en: ["Article 14", "Article 19", "Article 21", "Article 29"],
    options_hi: ["अनुच्छेद 14", "अनुच्छेद 19", "अनुच्छेद 21", "अनुच्छेद 29"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Article 21</b><br>In K.S. Puttaswamy v. Union of India (2017), a 9-judge bench ruled that privacy is a fundamental right under Article 21.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — अनुच्छेद 21</b><br>के.एस. पुट्टास्वामी मामले (2017) में सर्वोच्च न्यायालय ने निजता के अधिकार को अनुच्छेद 21 का अभिन्न अंग घोषित किया।"
  },
  {
    id: 108,
    year: 2017,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Parliamentary Form of Government (संसदीय सरकार का स्वरूप)",
    prompt_en: "The main advantage of the parliamentary form of government is that:",
    prompt_hi: "संसदीय शासन प्रणाली का मुख्य लाभ यह है कि:",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the most appropriate statement:",
    sub_prompt_hi: "सर्वाधिक उपयुक्त कथन का चयन कीजिए:",
    options_en: [
      "The executive and legislature work independently.",
      "The executive remains responsible to the legislature.",
      "It provides policy continuity and stability.",
      "The head of state cannot be changed easily."
    ],
    options_hi: [
      "कार्यपालिका और विधायिका स्वतंत्र रूप से कार्य करती हैं।",
      "कार्यपालिका विधायिका के प्रति उत्तरदायी बनी रहती है।",
      "यह नीतियों में निरंतरता और अधिक स्थिरता प्रदान करती है।",
      "राज्य का प्रमुख आसानी से नहीं बदला जा सकता।"
    ],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — The executive remains responsible to the legislature</b><br>The hallmark of the Westminster parliamentary model is the collective responsibility of the Council of Ministers to the elected legislature (Lok Sabha).",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — कार्यपालिका विधायिका के प्रति उत्तरदायी बनी रहती है</b><br>संसदीय प्रणाली की मूल विशेषता कार्यपालिका (मंत्रिपरिषद) का विधायिका (संसद) के प्रति निरंतर सामूहिक उत्तरदायित्व है।"
  },
  {
    id: 109,
    year: 2016,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Chief Secretary Appointment (मुख्य सचिव की नियुक्ति)",
    prompt_en: "Consider the following statements regarding the Chief Secretary in a State:",
    prompt_hi: "किसी राज्य के मुख्य सचिव के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "The Chief Secretary in a State is appointed by the Governor of that State.",
      "The Chief Secretary in a State has a fixed tenure."
    ],
    statements_hi: [
      "किसी राज्य के मुख्य सचिव की नियुक्ति उस राज्य के राज्यपाल द्वारा की जाती है।",
      "किसी राज्य के मुख्य सचिव का निश्चित कार्यकाल होता है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — 1 only</b><br>The Chief Secretary is selected by the Chief Minister and formally appointed in the name of the Governor. There is no constitutionally or legally fixed tenure.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>मुख्य सचिव की नियुक्ति राज्यपाल के नाम से होती है, परंतु इसका कोई निश्चित कार्यकाल (fixed tenure) नहीं होता।"
  },
  {
    id: 110,
    year: 2014,
    paper: "GS Paper I",
    subject: "Polity",
    topic: "Parliament Quorum / Art 100 (संसद का कोरम / गणपूर्ति)",
    prompt_en: "The quorum required to constitute a sitting of either House of Parliament (Lok Sabha or Rajya Sabha) is:",
    prompt_hi: "संसद के किसी भी सदन (लोक सभा या राज्य सभा) की बैठक आयोजित करने के लिए आवश्यक गणपूर्ति (Quorum) क्या है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the quorum fraction:",
    sub_prompt_hi: "आवश्यक कोरम अनुपात का चयन कीजिए:",
    options_en: [
      "One-tenth of the total number of members of the House",
      "One-sixth of the total number of members of the House",
      "One-eighth of the total number of members of the House",
      "One-fifth of the total number of members of the House"
    ],
    options_hi: [
      "सदन के कुल सदस्यों की संख्या का 1/10 (दसवां भाग)",
      "सदन के कुल सदस्यों की संख्या का 1/6 (छठा भाग)",
      "सदन के कुल सदस्यों की संख्या का 1/8 (आठवां भाग)",
      "सदन के कुल सदस्यों की संख्या का 1/5 (पाँचवां भाग)"
    ],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — One-tenth of the total number of members of the House</b><br>Under Article 100(3) of the Constitution of India, the quorum is one-tenth of the total number of members of the House (55 in Lok Sabha, 25 in Rajya Sabha).",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — सदन के कुल सदस्यों का 1/10 (दसवां भाग)</b><br>भारतीय संविधान के अनुच्छेद 100(3) के अनुसार संसद के किसी भी सदन की बैठक के लिए कोरम कुल सदस्यों का 10वां भाग (लोक सभा में 55 तथा राज्य सभा में 25) होता है।"
  },

  // ==========================================
  // 2. ECONOMY (भारतीय अर्थव्यवस्था)
  // ==========================================
  {
    id: 201,
    year: 2024,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "Sovereign Green Bonds (सॉवरेन ग्रीन बॉन्ड)",
    prompt_en: "Consider the following statements regarding Sovereign Green Bonds issued in India:",
    prompt_hi: "भारत में जारी सॉवरेन ग्रीन बॉन्ड के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "The proceeds from Sovereign Green Bonds are earmarked exclusively for public sector projects aimed at reducing carbon emissions.",
      "Foreign Portfolio Investors (FPIs) are permitted to invest in these bonds under the Fully Accessible Route."
    ],
    statements_hi: [
      "सॉवरेन ग्रीन बॉन्ड से प्राप्त धनराशि विशेष रूप से कार्बन उत्सर्जन कम करने वाली सार्वजनिक क्षेत्र की परियोजनाओं हेतु निर्धारित होती है।",
      "विदेशी पोर्टफोलियो निवेशकों (FPI) को पूरी तरह सुलभ मार्ग (FAR) के तहत इन बॉन्ड में निवेश की अनुमति है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Green bonds finance public green infrastructure projects and RBI opened sovereign green bonds to non-resident investors under the FAR framework.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>ग्रीन बॉन्ड का उपयोग हरित परियोजनाओं के वित्तपोषण हेतु होता है तथा RBI ने FPI को निवेश की अनुमति दी है।"
  },
  {
    id: 202,
    year: 2023,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "Central Bank Digital Currency / e-Rupee (सीबीडीसी / ई-रुपया)",
    prompt_en: "With reference to the Central Bank Digital Currency (CBDC) introduced by the Reserve Bank of India, consider the following statements:",
    prompt_hi: "भारतीय रिज़र्व बैंक (RBI) द्वारा शुरू की गई सेंट्रल बैंक डिजिटल करेंसी (CBDC) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "It is a sovereign currency in digital form and appears as a liability on the central bank's balance sheet.",
      "It can be transacted without opening a bank account using digital token wallets."
    ],
    statements_hi: [
      "यह डिजिटल रूप में एक संप्रभु मुद्रा है और केंद्रीय बैंक की बैलेंस शीट पर देयता (liability) के रूप में दिखाई देती है।",
      "इसे डिजिटल टोकन वॉलेट का उपयोग करके बिना बैंक खाता खोले भी लेन-देन में उपयोग किया जा सकता है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>CBDC is direct legal tender issued by the central bank, represented as a liability, and operates as token-based peer-to-peer bearer money.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>ई-रुपया (CBDC) RBI की बैलेंस शीट पर सीधी देयता है तथा यह टोकन आधारित डिजिटल मुद्रा है।"
  },
  {
    id: 203,
    year: 2022,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "Inflation Targeting / MPC (मुद्रास्फीति नियंत्रण)",
    prompt_en: "In India, which one of the following is responsible for maintaining price stability by controlling inflation?",
    prompt_hi: "भारत में, निम्नलिखित में से कौन मुद्रास्फीति को नियंत्रित कर कीमत स्थिरता बनाए रखने के लिए उत्तरदायी है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the correct authority:",
    sub_prompt_hi: "सही उत्तर का चयन कीजिए:",
    options_en: ["Department of Consumer Affairs", "Expenditure Management Commission", "Financial Stability and Development Council", "Reserve Bank of India"],
    options_hi: ["उपभोक्ता मामले विभाग", "व्यय प्रबंधन आयोग", "वित्तीय स्थिरता और विकास परिषद", "भारतीय रिज़र्व बैंक (RBI)"],
    correctIndex: 3,
    explanation_en: "<b>Correct Answer: Option (d) — Reserve Bank of India</b><br>Under Section 45ZA of the amended RBI Act, 1934, the Monetary Policy Committee sets policy rates to achieve the 4% +/- 2% inflation target.",
    explanation_hi: "<b>सही उत्तर: विकल्प (d) — भारतीय रिज़र्व बैंक (RBI)</b><br>संशोधित RBI अधिनियम 1934 के तहत मौद्रिक नीति समिति को 4% (+/- 2%) के दायरे में मुद्रास्फीति नियंत्रित रखने का दायित्व सौंपा गया है।"
  },
  {
    id: 204,
    year: 2021,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "Demand Deposits vs Time Deposits (मांग जमा एवं सावधि जमा)",
    prompt_en: "With reference to the Indian economy, which of the following are considered as 'Demand Deposits' in commercial banks?",
    prompt_hi: "भारतीय अर्थव्यवस्था के संदर्भ में, वाणिज्यिक बैंकों में निम्नलिखित में से किन्हें 'मांग जमा' (Demand Deposits) माना जाता है?",
    statements_en: [
      "Current Account deposits",
      "Savings Account deposits",
      "Fixed Deposits (Term deposits)"
    ],
    statements_hi: [
      "चालू खाता जमा (Current Account deposits)",
      "बचत खाता जमा (Savings Account deposits)",
      "सावधि जमा (Fixed / Term deposits)"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    options_hi: ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 1 and 2 only</b><br>Demand deposits are those payable on demand without notice (Current deposits and the demand portion of Savings deposits). Fixed deposits are time liabilities.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — केवल 1 और 2</b><br>चालू खाते और बचत खाते की मांग राशि को मांग जमा माना जाता है, जबकि सावधि जमा (FD) समय देयता (Time Liability) होती है।"
  },
  {
    id: 205,
    year: 2020,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "NBFCs vs Banks (गैर-बैंकिंग वित्तीय कंपनियां)",
    prompt_en: "With reference to the Non-Banking Financial Companies (NBFCs) in India, consider the following statements:",
    prompt_hi: "भारत में गैर-बैंकिंग वित्तीय कंपनियों (NBFCs) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "NBFCs cannot accept demand deposits from the public.",
      "NBFCs do not form part of the Payment and Settlement System and cannot issue cheques drawn on themselves."
    ],
    statements_hi: [
      "NBFCs जनता से मांग जमा (Demand deposits) स्वीकार नहीं कर सकती हैं।",
      "NBFCs भुगतान और निपटान प्रणाली का हिस्सा नहीं हैं और अपने नाम पर चेक जारी नहीं कर सकती हैं।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Unlike commercial banks, NBFCs cannot accept demand deposits, cannot issue cheques drawn on themselves, and deposit insurance (DICGC) is not available to them.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>वाणिज्यिक बैंकों के विपरीत NBFCs मांग जमा स्वीकार नहीं कर सकतीं और न ही चेक जारी कर सकती हैं।"
  },
  {
    id: 206,
    year: 2019,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "Money Multiplier (मुद्रा गुणक)",
    prompt_en: "The money multiplier in an economy increases with which one of the following?",
    prompt_hi: "किसी अर्थव्यवस्था में मुद्रा गुणक (Money Multiplier) निम्नलिखित में से किसके साथ बढ़ता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct factor:",
    sub_prompt_hi: "सही कारक का चयन कीजिए:",
    options_en: [
      "Increase in the cash reserve ratio (CRR)",
      "Increase in the banking habit of the population",
      "Increase in the statutory liquidity ratio (SLR)",
      "Increase in the population of the country"
    ],
    options_hi: [
      "नकद आरक्षित अनुपात (CRR) में वृद्धि",
      "जनसंख्या की बैंकिंग आदतों में वृद्धि",
      "सांविधिक तरलता अनुपात (SLR) में वृद्धि",
      "देश की जनसंख्या में वृद्धि"
    ],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Increase in the banking habit of the population</b><br>When more people deposit money in banks, banks can create more credit, raising the money multiplier (1 / reserve ratio).",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — जनसंख्या की बैंकिंग आदतों में वृद्धि</b><br>अधिक बैंकिंग आदतों से बैंकों में जमा बढ़ता है और वे अधिक साख सृजन कर पाते हैं जिससे मुद्रा गुणक बढ़ता है।"
  },
  {
    id: 207,
    year: 2018,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "FRBM Review Committee (एन.के. सिंह समिति)",
    prompt_en: "The N.K. Singh Committee was appointed by the Government of India to review and make recommendations on which of the following?",
    prompt_hi: "भारत सरकार द्वारा एन.के. सिंह समिति का गठन निम्नलिखित में से किसकी समीक्षा और सिफारिशें देने के लिए किया गया था?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the mandate:",
    sub_prompt_hi: "कार्यक्षेत्र का चयन कीजिए:",
    options_en: [
      "Fiscal Responsibility and Budget Management (FRBM) Act",
      "Direct Taxes Code",
      "Public Sector Banks Merger",
      "Goods and Services Tax (GST) slabs"
    ],
    options_hi: [
      "राजकोषीय उत्तरदायित्व एवं बजट प्रबंधन (FRBM) अधिनियम",
      "प्रत्यक्ष कर संहिता (Direct Taxes Code)",
      "सार्वजनिक क्षेत्र के बैंकों का विलय",
      "जीएसटी (GST) कर दरें"
    ],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — Fiscal Responsibility and Budget Management (FRBM) Act</b><br>The N.K. Singh Committee recommended using Debt-to-GDP ratio (60% overall: 40% Centre, 20% States) as the primary fiscal anchor.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — राजकोषीय उत्तरदायित्व एवं बजट प्रबंधन (FRBM) अधिनियम</b><br>एन.के. सिंह समिति ने FRBM समीक्षा कर ऋण-जीडीपी अनुपात 60% करने का लक्ष्य प्रस्तावित किया था।"
  },
  {
    id: 208,
    year: 2017,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "NPCI & UPI (एनपीसीआई एवं यूपीआई)",
    prompt_en: "Which of the following statements is/are correct regarding the 'National Payments Corporation of India (NPCI)'?",
    prompt_hi: "'भारतीय राष्ट्रीय भुगतान निगम' (NPCI) के संदर्भ में निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
    statements_en: [
      "NPCI is an initiative of the Reserve Bank of India and Indian Banks' Association.",
      "NPCI has developed the Unified Payments Interface (UPI)."
    ],
    statements_hi: [
      "NPCI भारतीय रिज़र्व बैंक (RBI) और भारतीय बैंक संघ (IBA) की एक पहल है।",
      "NPCI ने यूनिफाइड पेमेंट्स इंटरफेस (UPI) विकसित किया है।"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>NPCI is an umbrella organization for retail payments created by RBI and IBA under the Payment and Settlement Systems Act, 2007, which launched UPI, RuPay, and IMPS.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>NPCI की स्थापना RBI एवं IBA द्वारा की गई थी और इसी ने UPI, RuPay तथा IMPS को विकसित किया है।"
  },
  {
    id: 209,
    year: 2015,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "MCLR vs Base Rate (एमसीएलआर दर)",
    prompt_en: "Why did the Reserve Bank of India introduce the Marginal Cost of Funds based Lending Rate (MCLR) to replace the Base Rate system?",
    prompt_hi: "भारतीय रिज़र्व बैंक (RBI) ने बेस रेट प्रणाली के स्थान पर सीमांत निधि लागत आधारित उधार दर (MCLR) क्यों लागू की?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the primary objective:",
    sub_prompt_hi: "प्राथमिक उद्देश्य का चयन कीजिए:",
    options_en: [
      "To improve transparency and monetary transmission by commercial banks",
      "To completely eliminate non-performing assets (NPAs)",
      "To facilitate foreign currency loans to exporters",
      "To fix interest rates directly by the central government"
    ],
    options_hi: [
      "वाणिज्यिक बैंकों द्वारा मौद्रिक नीति संचरण और पारदर्शिता में सुधार हेतु",
      "बैंकों की गैर-निष्पादित संपत्तियों (NPAs) को पूरी तरह समाप्त करने हेतु",
      "निर्यातकों को विदेशी मुद्रा ऋण प्रदान करने हेतु",
      "केंद्र सरकार द्वारा सीधे ब्याज दर तय करने हेतु"
    ],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — To improve transparency and monetary transmission by commercial banks</b><br>MCLR was introduced to ensure that changes in repo rate by RBI are quickly transmitted to lending rates of commercial banks.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — वाणिज्यिक बैंकों द्वारा मौद्रिक नीति संचरण और पारदर्शिता में सुधार हेतु</b><br>MCLR का मुख्य उद्देश्य था कि जब RBI रेपो रेट घटाए या बढ़ाए, तो बैंक भी तुरंत अपनी ब्याज दरों में बदलाव करें।"
  },
  {
    id: 210,
    year: 2014,
    paper: "GS Paper I",
    subject: "Economy",
    topic: "Capital Account in BoP (भुगतान संतुलन में पूंजी खाता)",
    prompt_en: "Which of the following constitute the Capital Account of the Balance of Payments in India?",
    prompt_hi: "भारत में भुगतान संतुलन के 'पूंजी खाते' (Capital Account) में निम्नलिखित में से कौन शामिल हैं?",
    statements_en: [
      "Foreign Direct Investment (FDI)",
      "Foreign Portfolio Investment (FPI)",
      "Remittances from abroad",
      "External Commercial Borrowings (ECB)"
    ],
    statements_hi: [
      "प्रत्यक्ष विदेशी निवेश (FDI)",
      "विदेशी पोर्टफोलियो निवेश (FPI)",
      "विदेशों से प्राप्त प्रेषण (Remittances)",
      "बाह्य वाणिज्यिक उधारी (ECB)"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1, 2 and 4 only", "1, 2, 3 and 4", "2, 3 and 4 only", "1 and 3 only"],
    options_hi: ["केवल 1, 2 और 4", "1, 2, 3 और 4", "केवल 2, 3 और 4", "केवल 1 और 3"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — 1, 2 and 4 only</b><br>Remittances are unilateral transfers and part of the <b>Current Account</b> (invisibles), whereas FDI, FPI, and ECB are part of the Capital Account.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — केवल 1, 2 और 4</b><br>विदेशों से प्राप्त प्रेषण (Remittances) चालू खाते (अदृश्य मदों) का भाग होता है, जबकि FDI, FPI तथा ECB पूंजी खाते का भाग हैं।"
  },

  // ==========================================
  // 3. HISTORY & CULTURE (इतिहास एवं कला-संस्कृति)
  // ==========================================
  {
    id: 301,
    year: 2024,
    paper: "GS Paper I",
    subject: "History",
    topic: "Rigvedic Geography / Nadistuti (ऋग्वैदिक नदियां)",
    prompt_en: "With reference to the Vedic period in ancient India, the 'Nadistuti Sukta' in the Rigveda provides hymns in praise of which rivers?",
    prompt_hi: "प्राचीन भारत के वैदिक काल के संदर्भ में, ऋग्वेद का 'नदीस्तुति सूक्त' किन नदियों की स्तुति करता है?",
    statements_en: [
      "Sarasvati and Sindhu",
      "Ganga and Yamuna"
    ],
    statements_hi: [
      "सरस्वती और सिंधु",
      "गंगा और यमुना"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Rigveda's 10th Mandala Nadistuti Sukta hymns praise 21 rivers including Ganga, Yamuna, Sarasvati, Shutudri, and Sindhu.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>ऋग्वेद के 10वें मंडल के नदीस्तुति सूक्त में सिंधु, सरस्वती के साथ-साथ गंगा एवं यमुना का भी उल्लेख मिलता है।"
  },
  {
    id: 302,
    year: 2023,
    paper: "GS Paper I",
    subject: "History",
    topic: "Sangam Literature: Tolkappiyam (तोलकाप्पियम)",
    prompt_en: "In the context of ancient South Indian history, 'Tolkappiyam' is the most ancient extant work of:",
    prompt_hi: "प्राचीन दक्षिण भारतीय इतिहास के संदर्भ में, 'तोलकाप्पियम' (Tolkappiyam) किसका सर्वाधिक प्राचीन उपलब्ध ग्रंथ है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the subject:",
    sub_prompt_hi: "विषय का चयन कीजिए:",
    options_en: ["Tamil grammar and poetics", "Temple architecture and iconography", "Ayurvedic pharmacology", "Astronomy and navigation"],
    options_hi: ["तमिल व्याकरण एवं काव्यशास्त्र", "मंदिर वास्तुकला एवं मूर्तिकला", "आयुर्वेदिक औषधि विज्ञान", "खगोल विज्ञान एवं नौवहन"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — Tamil grammar and poetics</b><br>Tolkappiyam, authored by Tolkappiyar, is the earliest surviving masterpiece of Tamil grammar, linguistics, poetics, and socio-cultural life.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — तमिल व्याकरण एवं काव्यशास्त्र</b><br>तोलकाप्पियम संगम साहित्य का प्राचीनतम उपलब्ध तमिल व्याकरण एवं काव्यशास्त्र ग्रंथ है।"
  },
  {
    id: 303,
    year: 2022,
    paper: "GS Paper I",
    subject: "History",
    topic: "Ancient Terms: Agrahara (अग्रहार व्यवस्था)",
    prompt_en: "With reference to ancient India, the term 'Agrahara' refers to:",
    prompt_hi: "प्राचीन भारत के संदर्भ में, 'अग्रहार' (Agrahara) शब्द का क्या अर्थ है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct description:",
    sub_prompt_hi: "सही विवरण का चयन कीजिए:",
    options_en: ["A tax levied on peasants", "Land granted to Brahmanas exempt from taxes", "A military fortress", "An officer in charge of royal stables"],
    options_hi: ["किसानों पर लगाया गया कर", "ब्राह्मणों को दी जाने वाली कर-मुक्त भूमि अनुदान", "सैन्य छावनी या किला", "शाही अस्तबल का प्रमुख अधिकारी"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Land granted to Brahmanas exempt from taxes</b><br>An Agrahara was rent-free land or an entire village granted to Brahmanas for religious or scholarly pursuits.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — ब्राह्मणों को दी जाने वाली कर-मुक्त भूमि अनुदान</b><br>प्राचीन एवं मध्यकालीन भारत में ब्राह्मणों एवं विद्वानों को दी जाने वाली लगान-मुक्त भूमि या गाँव को 'अग्रहार' कहा जाता था।"
  },
  {
    id: 304,
    year: 2021,
    paper: "GS Paper I",
    subject: "History",
    topic: "Ancient Terms: Shramana / Upasaka (प्राचीन सांस्कृतिक शब्दावली)",
    prompt_en: "With reference to the cultural history of India, consider the following pairs:",
    prompt_hi: "भारत के सांस्कृतिक इतिहास के संदर्भ में, निम्नलिखित युग्मों पर विचार कीजिए:",
    statements_en: [
      "Parivrajaka — Renunciant and wanderer",
      "Shramana — Priest with a high status",
      "Upasaka — Lay follower of Buddhism"
    ],
    statements_hi: [
      "परिव्राजक — परित्यागी व भ्रमणकारी",
      "श्रमण — उच्च पद का पुजारी",
      "उपासक — बौद्ध धर्म का साधारण अनुगामी (गृहस्थ अनुयायी)"
    ],
    sub_prompt_en: "Which of the pairs given above are correctly matched?",
    sub_prompt_hi: "उपर्युक्त युग्मों में से कौन-से सही सुमेलित हैं?",
    options_en: ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"],
    options_hi: ["केवल 1 और 2", "केवल 1 और 3", "केवल 2 और 3", "1, 2 और 3"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 1 and 3 only</b><br>Shramana refers to ascetics of heterodox non-Vedic movements (Buddhism, Jainism, Ajivika), not orthodox priests with high status.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — केवल 1 और 3</b><br>श्रमण वैदिक परंपरा से भिन्न तपस्वी होते थे, न कि उच्च पद के पुजारी।"
  },
  {
    id: 305,
    year: 2020,
    paper: "GS Paper I",
    subject: "History",
    topic: "Jainism: Sthanakvasi Sect (स्थानकवासी संप्रदाय)",
    prompt_en: "With reference to the religious history of India, the 'Sthanakvasi' sect belongs to which religion?",
    prompt_hi: "भारत के धार्मिक इतिहास के संदर्भ में, 'स्थानकवासी' संप्रदाय किस धर्म से संबंधित है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the religion:",
    sub_prompt_hi: "धर्म का चयन कीजिए:",
    options_en: ["Buddhism", "Jainism", "Vaishnavism", "Shaivism"],
    options_hi: ["बौद्ध धर्म", "जैन धर्म", "वैष्णव धर्म", "शैव धर्म"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Jainism</b><br>Sthanakvasi is a reformist sub-sect of Shvetambara Jainism founded by Lavaji around 1653 AD that rejects idol-worship.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — जैन धर्म</b><br>स्थानकवासी श्वेतांबर जैन धर्म का एक संप्रदाय है जो मूर्ति पूजा में विश्वास नहीं करता।"
  },
  {
    id: 306,
    year: 2019,
    paper: "GS Paper I",
    subject: "History",
    topic: "Swadeshi Movement (स्वदेशी आंदोलन)",
    prompt_en: "With reference to the Swadeshi Movement in India, consider the following statements:",
    prompt_hi: "भारत में स्वदेशी आंदोलन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "It contributed to the revival of the indigenous artisan crafts and industries.",
      "The National Council of Education was established as a part of the Swadeshi Movement."
    ],
    statements_hi: [
      "इसने देशी शिल्पकारों के शिल्प और उद्योगों के पुनरुत्थान में योगदान दिया।",
      "स्वदेशी आंदोलन के एक भाग के रूप में 'राष्ट्रीय शिक्षा परिषद' की स्थापना की गई थी।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>The Swadeshi Movement (1905–1908) promoted indigenous swadeshi mills and established the National Council of Education in August 1906.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>स्वदेशी आंदोलन से भारतीय हथकरघा/उद्योगों को बढ़ावा मिला तथा 1906 में राष्ट्रीय शिक्षा परिषद स्थापित हुई।"
  },
  {
    id: 307,
    year: 2018,
    paper: "GS Paper I",
    subject: "History",
    topic: "Champaran Satyagraha (चंपारण सत्याग्रह)",
    prompt_en: "Which one of the following was a very significant aspect of the Champaran Satyagraha of 1917?",
    prompt_hi: "1917 के चंपारण सत्याग्रह का एक अत्यंत महत्वपूर्ण पहलू निम्नलिखित में से कौन-सा था?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct aspect:",
    sub_prompt_hi: "सही पहलू का चयन कीजिए:",
    options_en: [
      "Active all-India participation of lawyers and students",
      "Massive mobilization of industrial working class",
      "Joining of peasant unrest to India's National Movement under Gandhi's leadership",
      "Drastic decrease in the cultivation of cash crops across India"
    ],
    options_hi: [
      "अखिल भारतीय स्तर पर वकीलों और छात्रों की सक्रिय भागीदारी",
      "औद्योगिक मजदूर वर्ग का व्यापक आंदोलन",
      "गांधीजी के नेतृत्व में भारतीय राष्ट्रीय आंदोलन से किसान असंतोष का जुड़ना",
      "पूरे भारत में नकदी फसलों की खेती में भारी कमी"
    ],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Joining of peasant unrest to India's National Movement under Gandhi's leadership</b><br>Champaran marked Mahatma Gandhi's first civil disobedience in India and linked grassroots peasant struggles directly with the national freedom struggle.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — गांधीजी के नेतृत्व में भारतीय राष्ट्रीय आंदोलन से किसान असंतोष का जुड़ना</b><br>चंपारण सत्याग्रह ने तिनकठिया प्रणाली समाप्त करवाई और किसानों को राष्ट्रीय आंदोलन की मुख्यधारा से जोड़ा।"
  },
  {
    id: 308,
    year: 2017,
    paper: "GS Paper I",
    subject: "History",
    topic: "Charter Act of 1813 (1813 का चार्टर अधिनियम)",
    prompt_en: "Consider the following statements about the Charter Act of 1813:",
    prompt_hi: "1813 के चार्टर अधिनियम के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "It ended the trade monopoly of the East India Company in India except for trade in tea and trade with China.",
      "It asserted the sovereignty of the British Crown over the Indian territories held by the Company."
    ],
    statements_hi: [
      "इसने चाय के व्यापार और चीन के साथ व्यापार को छोड़कर भारत में ईस्ट इंडिया कंपनी के व्यापारिक एकाधिकार को समाप्त कर दिया।",
      "इसने कंपनी द्वारा प्रशासित भारतीय क्षेत्रों पर ब्रिटिश सम्राट की संप्रभुता को स्पष्ट रूप से स्थापित किया।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Charter Act 1813 abolished the Company's trade monopoly except for tea and trade with China, and asserted British Crown's constitutional sovereignty.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>1813 के चार्टर एक्ट द्वारा चाय और चीन व्यापार को छोड़कर कंपनी का एकाधिकार समाप्त हुआ तथा ब्रिटिश क्राउन की संप्रभुता घोषित की गई।"
  },
  {
    id: 309,
    year: 2016,
    paper: "GS Paper I",
    subject: "History",
    topic: "Vijayanagara Empire (विजयनगर साम्राज्य)",
    prompt_en: "Who of the following rulers of the Vijayanagara Empire composed the famous Telugu treatise on statecraft titled 'Amuktamalyada'?",
    prompt_hi: "विजयनगर साम्राज्य के निम्नलिखित शासकों में से किसने राजव्यवस्था पर प्रसिद्ध तेलुगु ग्रंथ 'आमुक्तमाल्यद' (Amuktamalyada) की रचना की?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the ruler:",
    sub_prompt_hi: "शासक का चयन कीजिए:",
    options_en: ["Harihara II", "Bukkaraya I", "Krishnadevaraya", "Deva Raya II"],
    options_hi: ["हरिहर द्वितीय", "बुक्का प्रथम", "कृष्णदेवराय", "देवराय द्वितीय"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Krishnadevaraya</b><br>Emperor Krishnadevaraya of the Tuluva dynasty composed the magnum opus 'Amuktamalyada' in Telugu dealing with political theory and administration.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — कृष्णदेवराय</b><br>विजयनगर के तुलुव वंश के सम्राट कृष्णदेवराय ने तेलुगु में 'आमुक्तमाल्यद' और संस्कृत में 'जांबवती कल्याणम' की रचना की।"
  },
  {
    id: 310,
    year: 2014,
    paper: "GS Paper I",
    subject: "History",
    topic: "Ghadar Movement (गदर आंदोलन)",
    prompt_en: "The Ghadar Party, an international revolutionary movement for Indian independence, was founded in 1913 with its headquarters at:",
    prompt_hi: "भारतीय स्वतंत्रता संग्राम के क्रांतिकारी संगठन 'गदर पार्टी' का मुख्यालय 1913 में कहाँ स्थापित किया गया था?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the headquarters city:",
    sub_prompt_hi: "मुख्यालय का शहर चुनिए:",
    options_en: ["San Francisco", "Berlin", "Tokyo", "London"],
    options_hi: ["सैन फ्रांसिस्को (San Francisco)", "बर्लिन", "टोक्यो", "लंदन"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — San Francisco</b><br>The Ghadar Party was founded in 1913 by Lala Har Dayal, Sohan Singh Bhakna, and others with its headquarters at Yugantar Ashram in San Francisco, USA.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — सैन फ्रांसिस्को (San Francisco)</b><br>गदर पार्टी की स्थापना लाला हरदयाल और सोहन सिंह भकना द्वारा सैन फ्रांसिस्को में युगांतर आश्रम में की गई थी।"
  },

  // ==========================================
  // 4. ENVIRONMENT & ECOLOGY (पर्यावरण एवं पारिस्थितिकी)
  // ==========================================
  {
    id: 401,
    year: 2024,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Kuno National Park & Cheetah (चीता पुनर्वास)",
    prompt_en: "With reference to the Cheetah Reintroduction Project in India, consider the following statements:",
    prompt_hi: "भारत में चीता पुनर्वास परियोजना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "The Asiatic cheetah was declared extinct in India in 1952.",
      "African cheetahs have been translocated to Kuno National Park in Madhya Pradesh."
    ],
    statements_hi: [
      "एशियाई चीते को भारत में 1952 में विलुप्त घोषित कर दिया गया था।",
      "अफ्रीकी चीतों को मध्य प्रदेश के कूनो राष्ट्रीय उद्यान में पुनर्वासित किया गया है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>Cheetahs were declared extinct in India in 1952. Under Project Cheetah, translocations from Namibia and South Africa were carried out at Kuno National Park, MP.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>भारत सरकार ने 1952 में चीते को विलुप्त घोषित किया था। नामीबिया और दक्षिण अफ्रीका से लाए गए चीतों को मध्य प्रदेश के कूनो राष्ट्रीय उद्यान में बसाया गया।"
  },
  {
    id: 402,
    year: 2023,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Invasive Species: Prosopis juliflora (विलायती बबूल)",
    prompt_en: "Why is a plant called 'Prosopis juliflora' often mentioned in news?",
    prompt_hi: "'प्रोसोपिस जूलीफ्लोरा' (Prosopis juliflora) नामक पौधा समाचारों में प्रायः किस कारण चर्चित रहता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct reason:",
    sub_prompt_hi: "सही कारण का चयन कीजिए:",
    options_en: [
      "Its extract is widely used in cosmetics.",
      "It tends to reduce the biodiversity in the area in which it grows.",
      "Its extract is used in the synthesis of pesticides.",
      "None of the above"
    ],
    options_hi: [
      "इसके अर्क का उपयोग सौंदर्य प्रसाधनों में व्यापक रूप से होता है।",
      "यह जिस क्षेत्र में उगता है, वहाँ की जैव विविधता को कम कर देता है।",
      "इसके अर्क का उपयोग कीटनाशकों के निर्माण में होता है।",
      "उपर्युक्त में से कोई नहीं"
    ],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — It tends to reduce the biodiversity in the area in which it grows</b><br>Prosopis juliflora (Vilayati Kikar) is an aggressive invasive alien shrub that depletes groundwater and suppresses native vegetation.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — यह जिस क्षेत्र में उगता है, वहाँ की जैव विविधता को कम कर देता है</b><br>विलायती बबूल एक आक्रामक विदेशी प्रजाति है जो स्थानीय वनस्पतियों और जल स्तर को भारी नुकसान पहुँचाती है।"
  },
  {
    id: 403,
    year: 2021,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Blue Carbon (ब्लू कार्बन)",
    prompt_en: "The term 'Blue Carbon' refers to:",
    prompt_hi: "'ब्लू कार्बन' (Blue Carbon) शब्द किसे निर्दिष्ट करता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the correct option:",
    sub_prompt_hi: "सही विकल्प चुनिए:",
    options_en: [
      "Carbon captured by coastal and marine ecosystems",
      "Carbon sequestered in forest biomass and agricultural soils",
      "Carbon contained in petroleum and natural gas",
      "Carbon present in the atmosphere"
    ],
    options_hi: [
      "तटीय एवं समुद्री पारिस्थितिक तंत्रों द्वारा संचित कार्बन",
      "वनों और कृषि मिट्टी में प्रगृहीत कार्बन",
      "पेट्रोलियम और प्राकृतिक गैस में निहित कार्बन",
      "वायुमंडल में उपस्थित कार्बन"
    ],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — Carbon captured by coastal and marine ecosystems</b><br>Blue carbon is the carbon stored in coastal habitats such as mangroves, tidal marshes, and seagrass meadows.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — तटीय एवं समुद्री पारिस्थितिक तंत्रों द्वारा संचित कार्बन</b><br>मैंग्रोव, ज्वारीय दलदल तथा समुद्री घास द्वारा प्रगृहीत कार्बन को ब्लू कार्बन कहा जाता है।"
  },
  {
    id: 404,
    year: 2020,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Cauvery Basin Protected Areas (कावेरी बेसिन के संरक्षित क्षेत्र)",
    prompt_en: "Which of the following protected areas are situated in the Cauvery basin?",
    prompt_hi: "निम्नलिखित संरक्षित क्षेत्रों में से कौन-से कावेरी बेसिन में स्थित हैं?",
    statements_en: [
      "Nagarhole National Park",
      "Papikonda National Park",
      "Sathyamangalam Tiger Reserve",
      "Wayanad Wildlife Sanctuary"
    ],
    statements_hi: [
      "नागरहोल राष्ट्रीय उद्यान",
      "पापीकोंडा राष्ट्रीय उद्यान",
      "सत्यमंगलम बाघ अभयारण्य",
      "वायनाड वन्यजीव अभयारण्य"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1 and 2 only", "3 and 4 only", "1, 3 and 4 only", "1, 2, 3 and 4"],
    options_hi: ["केवल 1 और 2", "केवल 3 और 4", "केवल 1, 3 और 4", "1, 2, 3 और 4"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — 1, 3 and 4 only</b><br>Papikonda is located in the Godavari basin in Andhra Pradesh. Nagarhole, Sathyamangalam, and Wayanad drain into Cauvery.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — केवल 1, 3 और 4</b><br>पापीकोंडा गोदावरी नदी घाटी में है। शेष तीनों कावेरी बेसिन में स्थित हैं।"
  },
  {
    id: 405,
    year: 2019,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Microbeads Pollution (माइक्रोबीड्स प्रदूषण)",
    prompt_en: "Why is there a great concern about the 'microbeads' that are released into environment?",
    prompt_hi: "पर्यावरण में निर्मुक्त होने वाले 'माइक्रोबीड्स' (Microbeads) के विषय में अत्यधिक चिंता क्यों है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the reason:",
    sub_prompt_hi: "कारण का चयन कीजिए:",
    options_en: [
      "They are considered harmful to marine ecosystems.",
      "They are considered to cause skin cancer in children.",
      "They are small enough to be absorbed by crop plants in irrigated fields.",
      "They are often found to be used as food adulterants."
    ],
    options_hi: [
      "इन्हें समुद्री पारिस्थितिक तंत्रों के लिए अत्यंत हानिकारक माना जाता है।",
      "इन्हें बच्चों में त्वचा कैंसर का कारण माना जाता है।",
      "ये इतने छोटे होते हैं कि सिंचित खेतों में फसलों द्वारा अवशोषित हो जाते हैं।",
      "इन्हें खाद्य पदार्थों में मिलावट के रूप में पाया जाता है।"
    ],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — They are considered harmful to marine ecosystems</b><br>Microbeads are microscopic plastic particles used in cosmetics that bypass wastewater filtration and poison marine organisms.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — इन्हें समुद्री पारिस्थितिक तंत्रों के लिए अत्यंत हानिकारक माना जाता है</b><br>माइक्रोबीड्स 5 मिमी से छोटे प्लास्टिक कण हैं जो जल स्रोतों से होकर समुद्री जीवों के भोजन चक्र में प्रवेश कर जाते हैं।"
  },
  {
    id: 406,
    year: 2017,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "National Biodiversity Authority (राष्ट्रीय जैव विविधता प्राधिकरण)",
    prompt_en: "How does the National Biodiversity Authority (NBA) help in protecting the Indian agriculture?",
    prompt_hi: "राष्ट्रीय जैव विविधता प्राधिकरण (NBA) भारतीय कृषि के संरक्षण में किस प्रकार सहायक है?",
    statements_en: [
      "NBA checks the biopiracy and protects the indigenous and traditional genetic resources.",
      "NBA directly monitors and conducts the scientific research on genetic modification of crop plants."
    ],
    statements_hi: [
      "NBA बायो-पायरेसी (biopiracy) को रोकता है और स्वदेशी एवं पारंपरिक आनुवंशिक संसाधनों का संरक्षण करता है।",
      "NBA फसल पौधों के आनुवंशिक संशोधन (GM) पर सीधे वैज्ञानिक अनुसंधान की निगरानी और संचालन करता है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — 1 only</b><br>Statement 1 is correct (mandate under Biological Diversity Act 2002). Statement 2 is incorrect because Genetic Engineering Appraisal Committee (GEAC) under MoEFCC monitors GM crops.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>कथन 1 सही है। कथन 2 गलत है क्योंकि GM फसलों के नियमन का कार्य GEAC (पर्यावरण मंत्रालय) द्वारा किया जाता है।"
  },
  {
    id: 407,
    year: 2016,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Red Sanders / Eastern Ghats (रक्त चंदन)",
    prompt_en: "With reference to 'Red Sanders' (Pterocarpus santalinus), consider the following statements:",
    prompt_hi: "'रक्त चंदन' (Red Sanders - Pterocarpus santalinus) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "It is a tree species found in a part of South India (Eastern Ghats).",
      "It is one of the most important trees in the tropical rain forest areas of South India."
    ],
    statements_hi: [
      "यह दक्षिण भारत (पूर्वी घाट) के एक विशिष्ट भाग में पाई जाने वाली वृक्ष प्रजाति है।",
      "यह दक्षिण भारत के उष्णकटिबंधीय वर्षा वन क्षेत्रों के सबसे महत्वपूर्ण वृक्षों में से एक है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — 1 only</b><br>Statement 1 is correct: Red Sanders is endemic to Seshachalam hills. Statement 2 is incorrect as it grows in dry deciduous forests, not rain forests.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>कथन 1 सही है (शेषाचलम पहाड़ियां/आंध्र प्रदेश)। कथन 2 गलत है क्योंकि यह शुष्क पर्णपाती वनों में पाया जाता है।"
  },
  {
    id: 408,
    year: 2015,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "BioCarbon Fund (बायोकार्बन फंड पहल)",
    prompt_en: "The 'BioCarbon Fund Initiative for Sustainable Forest Landscapes' is managed by the:",
    prompt_hi: "'सतत वन परिदृश्य हेतु बायोकार्बन फंड पहल' (BioCarbon Fund Initiative) का प्रबंधन किसके द्वारा किया जाता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the managing organization:",
    sub_prompt_hi: "प्रबंधन करने वाली संस्था चुनिए:",
    options_en: ["Asian Development Bank", "International Monetary Fund", "United Nations Environment Programme", "World Bank"],
    options_hi: ["एशियाई विकास बैंक (ADB)", "अंतर्राष्ट्रीय मुद्रा कोष (IMF)", "संयुक्त राष्ट्र पर्यावरण कार्यक्रम (UNEP)", "विश्व बैंक (World Bank)"],
    correctIndex: 3,
    explanation_en: "<b>Correct Answer: Option (d) — World Bank</b><br>The BioCarbon Fund Initiative for Sustainable Forest Landscapes (ISFL) is a multilateral facility managed by the World Bank.",
    explanation_hi: "<b>सही उत्तर: विकल्प (d) — विश्व बैंक (World Bank)</b><br>बायोकार्बन फंड सतत वन परिदृश्य पहल विश्व बैंक द्वारा प्रबंधित एक बहुपक्षीय सुविधा है।"
  },
  {
    id: 409,
    year: 2014,
    paper: "GS Paper I",
    subject: "Environment",
    topic: "Global Environment Facility (वैश्विक पर्यावरण सुविधा - GEF)",
    prompt_en: "With reference to the 'Global Environment Facility' (GEF), which of the following statements is/are correct?",
    prompt_hi: "'ग्लोबल एनवायरनमेंट फैसिलिटी' (GEF) के संदर्भ में निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
    statements_en: [
      "It serves as a financial mechanism for the Convention on Biological Diversity (CBD) and United Nations Framework Convention on Climate Change (UNFCCC).",
      "It undertakes scientific research on environmental issues independently of governments."
    ],
    statements_hi: [
      "यह जैव विविधता अभिसमय (CBD) और जलवायु परिवर्तन पर संयुक्त राष्ट्र फ्रेमवर्क अभिसमय (UNFCCC) के वित्तीय तंत्र के रूप में कार्य करता है।",
      "यह सरकारों से स्वतंत्र होकर पर्यावरणीय मुद्दों पर स्वतंत्र वैज्ञानिक अनुसंधान करता है।"
    ],
    sub_prompt_en: "Select the correct answer using the code given below:",
    sub_prompt_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — 1 only</b><br>GEF serves as financial mechanism for five major international environmental conventions including CBD, UNFCCC, UNCCD, Stockholm, and Minamata.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — केवल 1</b><br>GEF रियो सम्मेलनों (CBD, UNFCCC) हेतु वित्तीय तंत्र के रूप में कार्य करता है। यह स्वतंत्र अनुसंधान एजेंसी नहीं है।"
  },

  // ==========================================
  // 5. GEOGRAPHY (भारत एवं विश्व का भूगोल)
  // ==========================================
  {
    id: 501,
    year: 2024,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Red Sea & Bab-el-Mandeb (लाल सागर एवं जलडमरूमध्य)",
    prompt_en: "Which of the following bodies of water connects the Red Sea to the Gulf of Aden?",
    prompt_hi: "निम्नलिखित में से कौन-सा जलडमरूमध्य (Strait) लाल सागर को अदन की खाड़ी से जोड़ता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the strait:",
    sub_prompt_hi: "जलडमरूमध्य का चयन कीजिए:",
    options_en: ["Strait of Hormuz", "Bab-el-Mandeb Strait", "Bosporus Strait", "Strait of Malacca"],
    options_hi: ["होर्मुज जलडमरूमध्य", "बाब-अल-मंदेब जलडमरूमध्य (Bab-el-Mandeb)", "बोस्फोरस जलडमरूमध्य", "मलक्का जलडमरूमध्य"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Bab-el-Mandeb Strait</b><br>Bab-el-Mandeb strait ('Gate of Tears') connects the Red Sea to the Gulf of Aden and the Arabian Sea.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — बाब-अल-मंदेब जलडमरूमध्य</b><br>बाब-अल-मंदेब लाल सागर को अदन की खाड़ी से जोड़ता है।"
  },
  {
    id: 502,
    year: 2023,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Major Waterfalls & Rivers (प्रमुख जलप्रपात एवं नदियां)",
    prompt_en: "Consider the following pairs of Waterfalls and Rivers in India:",
    prompt_hi: "भारत में जलप्रपातों और नदियों के निम्नलिखित युग्मों पर विचार कीजिए:",
    statements_en: [
      "Dhuandhar Falls — Narmada",
      "Hundru Falls — Subarnarekha",
      "Gersoppa (Jog) Falls — Sharavati"
    ],
    statements_hi: [
      "धुआंधार जलप्रपात — नर्मदा",
      "हुंडरू जलप्रपात — सुवर्णरेखा",
      "गरसोप्पा (जोग) जलप्रपात — शरावती"
    ],
    sub_prompt_en: "Which of the pairs given above are correctly matched?",
    sub_prompt_hi: "उपर्युक्त में से कौन-से युग्म सही सुमेलित हैं?",
    options_en: ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    options_hi: ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    correctIndex: 3,
    explanation_en: "<b>Correct Answer: Option (d) — 1, 2 and 3</b><br>All three are iconic waterfalls: Dhuandhar on Narmada (MP), Hundru on Subarnarekha (Jharkhand), and Jog/Gersoppa on Sharavati (Karnataka).",
    explanation_hi: "<b>सही उत्तर: विकल्प (d) — 1, 2 और 3</b><br>तीनों युग्म सही हैं: धुआंधार (नर्मदा), हुंडरू (सुवर्णरेखा), और जोग (शरावती नदी)।"
  },
  {
    id: 503,
    year: 2022,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Himalayan Peaks & Ranges (पर्वत शिखर एवं हिमालय)",
    prompt_en: "Consider the following pairs of Mountain Peaks and Mountain Ranges:",
    prompt_hi: "पर्वत शिखरों और पर्वत श्रृंखलाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
    statements_en: [
      "Namcha Barwa — Garhwal Himalaya",
      "Nanda Devi — Kumaon Himalaya",
      "Nokrek — Sikkim Himalaya"
    ],
    statements_hi: [
      "नामचा बरवा — गढ़वाल हिमालय",
      "नंदा देवी — कुमाऊं हिमालय",
      "नोकरेक — सिक्किम हिमालय"
    ],
    sub_prompt_en: "Which of the pairs given above is/are correctly matched?",
    sub_prompt_hi: "उपर्युक्त युग्मों में से कौन-सा/से सही सुमेलित है/हैं?",
    options_en: ["1 and 2", "2 only", "1 and 3", "3 only"],
    options_hi: ["1 और 2", "केवल 2", "1 और 3", "केवल 3"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 2 only</b><br>Nanda Devi is in Kumaon Himalayas (Uttarakhand). Namcha Barwa is in Eastern Himalayas. Nokrek is in Garo Hills (Meghalaya).",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — केवल 2</b><br>नंदा देवी कुमाऊं हिमालय में स्थित है। नामचा बरवा पूर्वी हिमालय में तथा नोकरेक मेघालय के गारो हिल्स में स्थित है।"
  },
  {
    id: 504,
    year: 2020,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Siachen Glacier Location (सियाचिन ग्लेशियर की स्थिति)",
    prompt_en: "Siachen Glacier is situated to the:",
    prompt_hi: "सियाचिन हिमनद (Siachen Glacier) स्थित है:",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct geographic relative location:",
    sub_prompt_hi: "सही भौगोलिक सापेक्ष स्थिति का चयन कीजिए:",
    options_en: ["East of Aksai Chin", "East of Leh", "North of Gilgit", "North of Nubra Valley"],
    options_hi: ["अक्साई चिन के पूर्व में", "लेह के पूर्व में", "गिलगित के उत्तर में", "नुब्रा घाटी के उत्तर में (North of Nubra Valley)"],
    correctIndex: 3,
    explanation_en: "<b>Correct Answer: Option (d) — North of Nubra Valley</b><br>Siachen Glacier lies in the eastern Karakoram range in Ladakh, directly north of the Nubra Valley.",
    explanation_hi: "<b>सही उत्तर: विकल्प (d) — नुब्रा घाटी के उत्तर में</b><br>सियाचिन ग्लेशियर लद्दाख के पूर्वी काराकोरम में नुब्रा घाटी के उत्तर में स्थित है।"
  },
  {
    id: 505,
    year: 2018,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Mediterranean Climate (भूमध्यसागरीय जलवायु)",
    prompt_en: "Which one of the following regions possesses a climate characterized by winter rainfall and dry summers?",
    prompt_hi: "निम्नलिखित में से किस क्षेत्र की जलवायु की मुख्य विशेषता शीतकालीन वर्षा और शुष्क ग्रीष्मकाल है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the climate region:",
    sub_prompt_hi: "जलवायु क्षेत्र चुनिए:",
    options_en: ["Equatorial region", "Tropical monsoon region", "Mediterranean region", "Taiga region"],
    options_hi: ["भूमध्यरेखीय क्षेत्र", "उष्णकटिबंधीय मानसूनी क्षेत्र", "भूमध्यसागरीय क्षेत्र (Mediterranean)", "टैगा क्षेत्र"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Mediterranean region</b><br>Mediterranean climate experiences cyclonic winter rainfall from Westerlies and dry summers due to subtropical high pressure.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — भूमध्यसागरीय क्षेत्र (Mediterranean)</b><br>भूमध्यसागरीय जलवायु में पछुआ पवनों के कारण शीतकाल में वर्षा होती है तथा ग्रीष्मकाल शुष्क रहता है।"
  },
  {
    id: 506,
    year: 2015,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Equator Countries (भूमध्य रेखा पर स्थित देश)",
    prompt_en: "Through which one of the following groups of countries does the Equator pass?",
    prompt_hi: "भूमध्य रेखा (Equator) निम्नलिखित में से किस देश-समूह से होकर गुजरती है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct group:",
    sub_prompt_hi: "सही देश-समूह का चयन कीजिए:",
    options_en: ["Brazil, Zambia and Malaysia", "Colombia, Kenya and Indonesia", "Brazil, Sudan and Malaysia", "Venezuela, Ethiopia and Indonesia"],
    options_hi: ["ब्राजील, जाम्बिया और मलेशिया", "कोलंबिया, केन्या और इंडोनेशिया", "ब्राजील, सूडान और मलेशिया", "वेनेजुएला, इथियोपिया और इंडोनेशिया"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Colombia, Kenya and Indonesia</b><br>The Equator passes through 13 countries including Colombia, Ecuador, Brazil in South America; Gabon, Congo, DRC, Uganda, Kenya, Somalia in Africa; and Indonesia in Asia.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — कोलंबिया, केन्या और इंडोनेशिया</b><br>भूमध्य रेखा कुल 13 देशों से गुजरती है जिनमें कोलंबिया, केन्या और इंडोनेशिया शामिल हैं।"
  },
  {
    id: 507,
    year: 2014,
    paper: "GS Paper I",
    subject: "Geography",
    topic: "Turkey Seas Location (तुर्की की भौगोलिक स्थिति)",
    prompt_en: "Turkey is located between which of the following bodies of water?",
    prompt_hi: "तुर्की (Turkey) निम्नलिखित में से किन सागरों के मध्य स्थित है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the surrounding seas:",
    sub_prompt_hi: "सागरों का चयन कीजिए:",
    options_en: ["Black Sea and Caspian Sea", "Black Sea and Mediterranean Sea", "Gulf of Suez and Mediterranean Sea", "Gulf of Aqaba and Dead Sea"],
    options_hi: ["काला सागर और कैस्पियन सागर", "काला सागर और भूमध्य सागर (Black Sea and Mediterranean Sea)", "स्वेज की खाड़ी और भूमध्य सागर", "अकाबा की खाड़ी और मृत सागर"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — Black Sea and Mediterranean Sea</b><br>The Anatolian peninsula of Turkey is bounded by the Black Sea to the north and the Mediterranean Sea to the south.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — काला सागर और भूमध्य सागर</b><br>तुर्की उत्तर में काला सागर और दक्षिण में भूमध्य सागर के बीच स्थित है।"
  },

  // ==========================================
  // 6. SCIENCE & TECHNOLOGY (विज्ञान एवं प्रौद्योगिकी)
  // ==========================================
  {
    id: 601,
    year: 2024,
    paper: "GS Paper I",
    subject: "Sci & Tech",
    topic: "Large Language Models / AI (जनरेटिव एआई एवं एलएलएम)",
    prompt_en: "With reference to 'Large Language Models (LLMs)' in Artificial Intelligence, consider the following statements:",
    prompt_hi: "आर्टिफिशियल इंटेलिजेंस में 'लार्ज लैंग्वेज मॉडल्स' (LLMs) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "They are built using deep learning transformer architectures trained on vast text corpora.",
      "They can perform reasoning, translation, and code generation through next-token prediction."
    ],
    statements_hi: [
      "ये विशाल पाठ डेटासेट पर प्रशिक्षित डीप लर्निंग ट्रांसफॉर्मर आर्किटेक्चर का उपयोग करके बनाए जाते हैं।",
      "ये अगले टोकन की भविष्यवाणी के माध्यम से तार्किक तर्क, भाषा अनुवाद और कोड निर्माण कर सकते हैं।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 2,
    explanation_en: "<b>Correct Answer: Option (c) — Both 1 and 2</b><br>LLMs rely on attention-based transformer neural networks to predict sequence probabilities, facilitating generalized NLP capabilities.",
    explanation_hi: "<b>सही उत्तर: विकल्प (c) — 1 और 2 दोनों</b><br>LLMs ट्रांसफॉर्मर न्यूरल नेटवर्क पर आधारित होते हैं और जटिल तार्किक व बहुभाषी कार्य कर सकते हैं।"
  },
  {
    id: 602,
    year: 2023,
    paper: "GS Paper I",
    subject: "Sci & Tech",
    topic: "Web 3.0 & Decentralization (वेब 3.0 तकनीक)",
    prompt_en: "With reference to 'Web 3.0', consider the following statements:",
    prompt_hi: "'वेब 3.0' (Web 3.0) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "Web 3.0 technology enables people to control their own data.",
      "In Web 3.0 world, there can be blockchain-based social networks.",
      "Web 3.0 is operated by users collectively rather than a corporation."
    ],
    statements_hi: [
      "वेब 3.0 तकनीक लोगों को अपने डेटा पर नियंत्रण रखने में सक्षम बनाती है।",
      "वेब 3.0 में ब्लॉकचेन-आधारित सोशल नेटवर्क हो सकते हैं।",
      "वेब 3.0 किसी कॉर्पोरेशन की बजाय सामूहिक रूप से उपयोगकर्ताओं द्वारा संचालित होता है।"
    ],
    sub_prompt_en: "Which of the statements given above are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-से सही हैं?",
    options_en: ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    options_hi: ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    correctIndex: 3,
    explanation_en: "<b>Correct Answer: Option (d) — 1, 2 and 3</b><br>Web 3.0 represents a decentralized semantic web where users retain data ownership, run DAOs, and build on public blockchains.",
    explanation_hi: "<b>सही उत्तर: विकल्प (d) — 1, 2 और 3</b><br>वेब 3.0 ब्लॉकचेन आधारित विकेंद्रीकृत इंटरनेट है जो डेटा संप्रभुता प्रदान करता है।"
  },
  {
    id: 603,
    year: 2021,
    paper: "GS Paper I",
    subject: "Sci & Tech",
    topic: "Recombinant Vector Vaccines (पुनर्संयोजक वेक्टर टीके)",
    prompt_en: "In the context of vaccines manufactured to prevent COVID-19 pandemic, consider the following statements:",
    prompt_hi: "कोविड-19 महामारी को रोकने हेतु निर्मित टीकों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:",
    statements_en: [
      "The Serum Institute of India produced COVID-19 vaccine named Covishield using mRNA platform.",
      "Sputnik V vaccine is manufactured using vector based platform."
    ],
    statements_hi: [
      "सीरम इंस्टीट्यूट ऑफ इंडिया ने mRNA प्लेटफॉर्म का उपयोग करके कोविशील्ड नामक टीका बनाया।",
      "स्पुतनिक वी (Sputnik V) टीका वायरल वेक्टर आधारित प्लेटफॉर्म का उपयोग करके बनाया गया है।"
    ],
    sub_prompt_en: "Which of the statements given above is/are correct?",
    sub_prompt_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    options_en: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    options_hi: ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1, न ही 2"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 2 only</b><br>Covishield is a chimpanzee adenovirus viral vector vaccine (not mRNA). Sputnik V is an adenovirus vector vaccine.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — केवल 2</b><br>कथन 1 गलत है (कोविशील्ड एडेनोवायरस वायरल वेक्टर पर आधारित है, mRNA नहीं)। कथन 2 सही है।"
  },
  {
    id: 604,
    year: 2020,
    paper: "GS Paper I",
    subject: "Sci & Tech",
    topic: "Pronuclear Transfer / Mitochondrial DNA (माइटोकॉन्ड्रियल रिप्लेसमेंट थेरेपी)",
    prompt_en: "In the context of recent advances in human genetics, which one of the following is the application of 'Pronuclear Transfer'?",
    prompt_hi: "मानव आनुवंशिकी में हाल के विकास के संदर्भ में, 'प्रोन्यूक्लियर ट्रांसफर' (Pronuclear Transfer) का उपयोग किसमें किया जाता है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the correct application:",
    sub_prompt_hi: "सही अनुप्रयोग का चयन कीजिए:",
    options_en: [
      "Fertilization of egg in vitro by the donor sperm",
      "Genetic modification of sperm-producing cells",
      "Development of stem cells into functional organs",
      "Prevention of mitochondrial diseases in offspring"
    ],
    options_hi: [
      "दाता शुक्राणु द्वारा परखनली में अंडे का निषेचन",
      "शुक्राणु उत्पन्न करने वाली कोशिकाओं का आनुवंशिक संशोधन",
      "स्टेम कोशिकाओं का कार्यात्मक अंगों में विकास",
      "संतान में माइटोकॉन्ड्रियल रोगों की रोकथाम"
    ],
    correctIndex: 3,
    explanation_en: "<b>Correct Answer: Option (d) — Prevention of mitochondrial diseases in offspring</b><br>Pronuclear transfer (three-parent baby technique) prevents the transmission of faulty maternal mitochondrial DNA to the child.",
    explanation_hi: "<b>सही उत्तर: विकल्प (d) — संतान में माइटोकॉन्ड्रियल रोगों की रोकथाम</b><br>प्रोन्यूक्लियर ट्रांसफर तकनीक से माता से संतान में जाने वाली आनुवंशिक माइटोकॉन्ड्रियल बीमारियों को रोका जाता है।"
  },
  {
    id: 605,
    year: 2019,
    paper: "GS Paper I",
    subject: "Sci & Tech",
    topic: "CRISPR-Cas9 (जीन संपादन तकनीक)",
    prompt_en: "What is Cas9 protein that is often mentioned in news?",
    prompt_hi: "समाचारों में प्रायः चर्चित 'Cas9 प्रोटीन' क्या है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Select the correct option:",
    sub_prompt_hi: "सही विकल्प का चयन कीजिए:",
    options_en: [
      "A molecular scissors used in targeted gene editing",
      "A biosensor used in the detection of diseases in patients",
      "A gene that makes plants pest-resistant",
      "A substance used in developing biodegradable plastics"
    ],
    options_hi: [
      "लक्षित जीन संपादन (targeted gene editing) में प्रयुक्त आणविक कैंची",
      "रोगियों में रोगों का पता लगाने वाला बायोसेंसर",
      "पौधों को कीट-प्रतिरोधी बनाने वाला जीन",
      "जैव-अपघटनीय प्लास्टिक में प्रयुक्त पदार्थ"
    ],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — A molecular scissors used in targeted gene editing</b><br>CRISPR-Cas9 functions as molecular scissors guiding RNA to cut specific DNA sequences.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — लक्षित जीन संपादन में प्रयुक्त आणविक कैंची</b><br>Cas9 एक एंजाइम (आणविक कैंची) है जो DNA के विशिष्ट खंडों को काटने और संपादित करने के काम आता है।"
  },
  {
    id: 606,
    year: 2017,
    paper: "GS Paper I",
    subject: "Sci & Tech",
    topic: "Gravitational Waves & LIGO (गुरुत्वाकर्षण तरंगें)",
    prompt_en: "What is the purpose of the 'evolved Laser Interferometer Space Antenna (eLISA)' project?",
    prompt_hi: "'इवॉल्व्ड लेजर इंटरफेरोमीटर स्पेस एंटीना' (eLISA) परियोजना का उद्देश्य क्या है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the scientific objective:",
    sub_prompt_hi: "वैज्ञानिक उद्देश्य चुनिए:",
    options_en: ["To detect neutrinos", "To detect gravitational waves in space", "To detect missile launch", "To study solar flares"],
    options_hi: ["न्यूट्रिनो का पता लगाना", "अंतरिक्ष में गुरुत्वाकर्षण तरंगों का पता लगाना", "मिसाइल प्रक्षेपण का पता लगाना", "सौर ज्वालाओं का अध्ययन करना"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — To detect gravitational waves in space</b><br>eLISA is a space-based gravitational wave observatory designed to measure gravitational radiation from black hole mergers.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — अंतरिक्ष में गुरुत्वाकर्षण तरंगों का पता लगाना</b><br>eLISA यूरोपीय अंतरिक्ष एजेंसी का मिशन है जो अंतरिक्ष में गुरुत्वाकर्षण तरंगों की पहचान करने के लिए बनाया गया है।"
  },

  // ==========================================
  // 7. CSAT PAPER II (सीसैट)
  // ==========================================
  {
    id: 701,
    year: 2024,
    paper: "CSAT Paper II",
    subject: "CSAT",
    topic: "Permutations & Combinations (क्रमचय एवं संचय)",
    prompt_en: "How many 3-digit numbers can be formed using the digits 1, 2, 3, 4, 5 without repetition of any digit?",
    prompt_hi: "अंक 1, 2, 3, 4, 5 का प्रयोग करके बिना किसी अंक की पुनरावृत्ति के 3 अंकों की कितनी संख्याएं बनाई जा सकती हैं?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Calculate the total numbers:",
    sub_prompt_hi: "कुल संख्याओं की गणना कीजिए:",
    options_en: ["60", "120", "20", "10"],
    options_hi: ["60", "120", "20", "10"],
    correctIndex: 0,
    explanation_en: "<b>Correct Answer: Option (a) — 60</b><br>Number of ways to choose and arrange 3 digits out of 5 distinct digits: 5P3 = 5 × 4 × 3 = 60.",
    explanation_hi: "<b>सही उत्तर: विकल्प (a) — 60</b><br>5 अंकों में से 3 अंकों को चुनने और व्यवस्थित करने के तरीके = 5 × 4 × 3 = 60 संख्याएं।"
  },
  {
    id: 702,
    year: 2023,
    paper: "CSAT Paper II",
    subject: "CSAT",
    topic: "Digit Reversals (संख्या पद्धति)",
    prompt_en: "A number consists of two digits whose sum is 9. If 27 is subtracted from the number, its digits are interchanged. What is the number?",
    prompt_hi: "दो अंकों की एक संख्या के अंकों का योग 9 है। यदि संख्या में से 27 घटाया जाता है, तो इसके अंक आपस में बदल जाते हैं। वह संख्या क्या है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Choose the correct number:",
    sub_prompt_hi: "सही संख्या का चयन कीजिए:",
    options_en: ["36", "63", "45", "54"],
    options_hi: ["36", "63", "45", "54"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 63</b><br>63 - 27 = 36 (digits reversed). Sum of digits 6 + 3 = 9.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — 63</b><br>विकल्पों से जाँचें: 63 - 27 = 36 (अंक पलट गए)। अंकों का योग 6 + 3 = 9 है।"
  },
  {
    id: 703,
    year: 2022,
    paper: "CSAT Paper II",
    subject: "CSAT",
    topic: "Ratios & Mixtures (अनुपात एवं मिश्रण)",
    prompt_en: "A vessel contains 60 litres of a mixture of milk and water in the ratio 2 : 1. How much water should be added to make the ratio 1 : 2?",
    prompt_hi: "एक बर्तन में 60 लीटर दूध और पानी का मिश्रण 2 : 1 के अनुपात में है। अनुपात को 1 : 2 करने के लिए इसमें कितना पानी मिलाना चाहिए?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Calculate the quantity of water to add:",
    sub_prompt_hi: "मिलाए जाने वाले पानी की मात्रा की गणना कीजिए:",
    options_en: ["40 litres", "60 litres", "80 litres", "50 litres"],
    options_hi: ["40 लीटर", "60 लीटर", "80 लीटर", "50 लीटर"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 60 litres</b><br>Initial Milk = (2/3) × 60 = 40 litres, Water = 20 litres.<br>To make ratio 1:2 with 40L milk, Water needed = 80 litres.<br>Water to add = 80 - 20 = <b>60 litres</b>.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — 60 लीटर</b><br>प्रारंभ में दूध = 40 लीटर, पानी = 20 लीटर।<br>अनुपात 1:2 करने के लिए 40 लीटर दूध पर 80 लीटर पानी चाहिए। अतः मिलाया गया पानी = 80 - 20 = 60 लीटर।"
  },
  {
    id: 704,
    year: 2021,
    paper: "CSAT Paper II",
    subject: "CSAT",
    topic: "Direction Sense (दिशा परीक्षण)",
    prompt_en: "A person walks 12 km North, then turns right and walks 5 km East. What is the shortest distance between his starting and final positions?",
    prompt_hi: "एक व्यक्ति 12 किमी उत्तर की ओर चलता है, फिर दाएं मुड़कर 5 किमी पूर्व की ओर चलता है। उसके प्रारंभिक और अंतिम बिंदु के बीच की न्यूनतम दूरी क्या है?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Find the shortest distance:",
    sub_prompt_hi: "न्यूनतम दूरी ज्ञात कीजिए:",
    options_en: ["17 km", "13 km", "15 km", "10 km"],
    options_hi: ["17 किमी", "13 किमी", "15 किमी", "10 किमी"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 13 km</b><br>By Pythagoras theorem: Shortest Distance = √(12² + 5²) = √(144 + 25) = √169 = <b>13 km</b>.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — 13 किमी</b><br>पाइथागोरस प्रमेय से: न्यूनतम दूरी = √(12² + 5²) = √(144 + 25) = √169 = 13 किमी।"
  },
  {
    id: 705,
    year: 2020,
    paper: "CSAT Paper II",
    subject: "CSAT",
    topic: "Work & Time (कार्य एवं समय)",
    prompt_en: "A can complete a work in 10 days and B can complete the same work in 15 days. Working together, in how many days will they finish the work?",
    prompt_hi: "A किसी कार्य को 10 दिनों में तथा B उसी कार्य को 15 दिनों में पूरा कर सकता है। एक साथ कार्य करते हुए वे इस कार्य को कितने दिनों में पूरा करेंगे?",
    statements_en: [],
    statements_hi: [],
    sub_prompt_en: "Calculate the total days:",
    sub_prompt_hi: "कुल दिनों की गणना कीजिए:",
    options_en: ["5 days", "6 days", "8 days", "7.5 days"],
    options_hi: ["5 दिन", "6 दिन", "8 दिन", "7.5 दिन"],
    correctIndex: 1,
    explanation_en: "<b>Correct Answer: Option (b) — 6 days</b><br>Combined 1-day work = 1/10 + 1/15 = (3 + 2)/30 = 5/30 = 1/6.<br>Total days required = <b>6 days</b>.",
    explanation_hi: "<b>सही उत्तर: विकल्प (b) — 6 दिन</b><br>दोनों का 1 दिन का कार्य = 1/10 + 1/15 = 5/30 = 1/6। अतः दोनों मिलकर 6 दिन में कार्य पूरा करेंगे।"
  }
];

if (typeof window !== 'undefined') {
  window.QUESTIONS_DB = QUESTIONS_DATA;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = QUESTIONS_DATA;
}
