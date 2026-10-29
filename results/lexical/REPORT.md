# Lexical track report

Generated 2026-10-29 by `tools/lexical.py`. Raw candidates are in `quran.json` and `hebrew-bible.json`.

Verses are counted, not tokens, so a word repeated within one verse counts once. Narrative labels come from `data/narratives/`.

## Benchmarks

| Expectation | Recovered |
|---|---|
| Quran: al-yamm is concentrated in the Moses narrative | yes |
| Quran al-yamm ↔ Hebrew yam (H3220) | yes |
| Quran tannūr ↔ Hebrew tannûr (H8574) | yes |
| Hebrew tēbâ (H8392) links Noah's ark and Moses' basket | yes |
| Quran kursī ↔ Hebrew kissēʾ (H3678); needs the Aramaic loan-chain layer (v2) | no (expected: known limitation) |

## Quran: concentration (34 candidates)

| Score | Lemma | Narrative | In narrative | Units | q | Flags |
|---|---|---|---|---|---|---|
| 16.19 | يَمّ *yamm* “sea” (root يمم) | Moses | 7/7 (100%; base 7%) | 4 | 1.5e-07 | synonym skew vs بَحْر (39, 28% here); Hebrew cognate יָם *yâm* H3220 |
| 15.31 | ساحِر *sāḥir* “magician” (root سحر) | Moses | 18/21 (86%; base 7%) | 7 | 1.8e-16 |  |
| 12.37 | غابِر *ghābir* “behind” (root غبر) | Lot | 5/7 (71%; base 1%) | 4 | 4.5e-08 | synonym skew vs خَلْف (22, 0% here), وَراء (24, 0% here) |
| 9.98 | يَهْبِطُ *yahbiṭu* “down” (root هبط) | Adam and Iblis | 5/8 (62%; base 1%) | 3 | 1.8e-07 | synonym skew vs نَزَّلَ (61, 0% here) |
| 9.33 | راغَ *rāgha* “turned” (root روغ) | Abraham | 3/3 (100%; base 3%) | 2 | 1.1e-04 | synonym skew vs قَلَّبُ (6, 0% here), أَدْبَرَ (4, 0% here) |
| 7.69 | حَوارِيّ *ḥawārī* “disciple” (root حور) | Jesus and Mary | 4/4 (100%; base 1%) | 3 | 3.1e-07 |  |
| 7.55 | عاقِر *ʿāqir* “barren” (root عقر) | Zechariah and John | 3/3 (100%; base 0%) | 2 | 4.1e-07 | Hebrew cognate עָקָר *ʻâqâr* H6135 |
| 6.93 | سَلْوَى *salwā* “quail” (root سلو) | Moses | 3/3 (100%; base 7%) | 3 | 1.1e-03 | Hebrew cognate שְׂלָו *sᵉlâv* H7958; **same narrative in Hebrew Bible** |
| 6.93 | تَلْقَفُ *talqafu* “swallow” (root لقف) | Moses | 3/3 (100%; base 7%) | 3 | 1.1e-03 | synonym skew vs خَسَفَ (8, 0% here) |
| 6.93 | أَيْمَن *ʾayman* “right” (root يمن) | Moses | 3/3 (100%; base 7%) | 3 | 1.1e-03 | synonym skew vs قَيِّم (5, 0% here); Hebrew cognate יְמָנִי *yᵉmânîy* H3233, יָמַן *yâman* H3231 |
| 6.67 | ناقَة *nāqa* “camel” (root نوق) | Salih and Thamud | 5/7 (71%; base 1%) | 4 | 1.2e-08 |  |
| 6.25 | عَقَرَ *ʿaqara* “hamstrung” (root عقر) | Salih and Thamud | 4/5 (80%; base 1%) | 4 | 2.4e-07 |  |
| 6.19 | أُمْطِرَتْ *ʾumṭirat* “rained” (root مطر) | Lot | 5/7 (71%; base 1%) | 5 | 4.5e-08 |  |
| 4.43 | أَصْنام *ʾaṣnām* “idol” (root صنم) | Abraham | 4/5 (80%; base 3%) | 4 | 2.5e-05 |  |
| 4.33 | آنَسَ *ʾānasa* “perceive” (root انس) | Moses | 3/4 (75%; base 7%) | 3 | 3.4e-03 | synonym skew vs يَشْعُرُ (25, 8% here) |
| 4.33 | اخْتارَ *akhtāra* “chose” (root خير) | Moses | 3/4 (75%; base 7%) | 3 | 3.4e-03 | synonym skew vs اجْتَبَى (10, 0% here) |
| 3.53 | مُغْرَق *mughraq* “drowned” (root غرق) | Noah | 3/4 (75%; base 2%) | 2 | 1.0e-04 |  |
| 3.46 | مَدائِن *madāʾin* “citie” (root مدن) | Moses | 3/3 (100%; base 7%) | 2 | 1.1e-03 |  |
| 3.46 | حاشِر *ḥāshir* “gatherer” (root حشر) | Moses | 3/3 (100%; base 7%) | 2 | 1.1e-03 |  |
| 3.46 | مُلْقي *mulqy* “throw” (root لقي) | Moses | 3/3 (100%; base 7%) | 3 | 1.1e-03 |  |
| 3.43 | يَبْخَسْ *yabkhas* “deprive” (root بخس) | Shuʿayb and Midian | 3/5 (60%; base 1%) | 3 | 1.8e-05 |  |
| 2.98 | مَطَر *maṭar* “rain” (root مطر) | Lot | 3/5 (60%; base 1%) | 3 | 6.2e-05 | Hebrew cognate מָטַר *mâṭar* H4306, מָטַר *mâṭar* H4305 |
| 2.98 | جَواب *jawāb* “answer” (root جوب) | Lot | 3/5 (60%; base 1%) | 3 | 6.2e-05 |  |
| 2.98 | ضَيْف *ḍayf* “guest” (root ضيف) | Lot | 3/5 (60%; base 1%) | 3 | 6.2e-05 |  |
| 2.86 | مَهْد *mahd* “cradle” (root مهد) | Jesus and Mary | 3/5 (60%; base 1%) | 3 | 9.5e-05 |  |
| 2.57 | يَسْتَحْىِۦ *yastaḥāi* “live” (root حيي) | Moses | 5/8 (62%; base 7%) | 4 | 3.3e-04 | Hebrew cognate חַי *chay* H2416, חָיָה *châyâh* H2421 |
| 2.57 | أَبْيَض *ʾabyaḍ* “white” (root بيض) | Moses | 5/8 (62%; base 7%) | 5 | 3.3e-04 | Hebrew cognate בּוּץ *bûwts* H948 |
| 2.21 | أَمْن *ʾamn* “security” (root امن) | Abraham | 3/5 (60%; base 3%) | 2 | 7.7e-04 |  |
| 2.16 | يَسُومُ *yasūmu* “afflicting” (root سوم) | Moses | 3/4 (75%; base 7%) | 2 | 3.4e-03 |  |
| 2.16 | واعَدْ *wāʿad* “appointed” (root وعد) | Moses | 3/4 (75%; base 7%) | 3 | 3.4e-03 |  |
| 2.16 | جاوَزَ *jāwaza* “across” (root جوز) | Moses | 3/4 (75%; base 7%) | 3 | 3.4e-03 |  |
| 2.16 | يُصَلَّبُ *yuṣallabu* “crucify” (root صلب) | Moses | 3/4 (75%; base 7%) | 3 | 3.4e-03 |  |
| 1.51 | ناظِر *nāẓir* “observer” (root نظر) | Moses | 3/5 (60%; base 7%) | 3 | 6.7e-03 |  |
| 1.51 | حُوت *ḥūt* “fish” (root حوت) | Moses | 3/5 (60%; base 7%) | 2 | 6.7e-03 |  |

## Quran: bridges (45 candidates)

| p | Lemma | Narratives | Verses |
|---|---|---|---|
| 7.3e-12 | راوَدُ *rāwadu* “seduce” (root رود) | Joseph (6) + Lot (1) | 7 |
| 8.1e-08 | ضَيْف *ḍayf* “guest” (root ضيف) | Abraham (2) + Lot (3) | 5 |
| 3.9e-07 | بَقَرَة *baqara* “cow” (root بقر) · Hebrew cognate בָּקָר *bâqâr* H1241 | Joseph (2) + Moses (4) | 6 |
| 2.0e-06 | حُوت *ḥūt* “fish” (root حوت) | Jonah (2) + Moses (3) | 5 |
| 2.4e-06 | رَهْط *rahṭ* “family” (root رهط) | Salih and Thamud (1) + Shuʿayb and Midian (2) | 3 |
| 6.3e-06 | فِتْيَة *fitya* “youth” (root فتي) | People of the Cave (2) + Joseph (1) | 3 |
| 6.8e-06 | طَفِقَ *ṭafiqa* “began” (root طفق) | Adam and Iblis (2) + Solomon (1) | 3 |
| 9.0e-06 | أَصْنام *ʾaṣnām* “idol” (root صنم) | Abraham (4) + Moses (1) | 5 |
| 2.5e-05 | جاوَزَ *jāwaza* “across” (root جوز) | Moses (3) + Saul (Talut) and Goliath (1) | 4 |
| 2.9e-05 | غَرَبَت *gharabat* “set” (root غرب) | People of the Cave (1) + Dhul-Qarnayn (1) | 2 |
| 2.9e-05 | طَلَعَت *ṭalaʿat* “rose” (root طلع) | People of the Cave (1) + Dhul-Qarnayn (1) | 2 |
| 5.8e-05 | مُغْرَق *mughraq* “drowned” (root غرق) | Moses (1) + Noah (3) | 4 |
| 6.0e-05 | بَصطَة *baṣṭa* “abundantly” (root بسط) | Hud and ʿAd (1) + Saul (Talut) and Goliath (1) | 2 |
| 8.3e-05 | سَمِين *samīn* “fat” (root سمن) · Hebrew cognate שֶׁמֶן *shemen* H8081 | Abraham (1) + Joseph (2) | 3 |
| 9.7e-05 | قِطْر *qiṭr* “molten” (root قطر) | Dhul-Qarnayn (1) + Solomon (1) | 2 |
| 1.8e-04 | مُسَحَّر *musaḥḥar* “bewitched” (root سحر) | Salih and Thamud (1) + Shuʿayb and Midian (1) | 2 |
| 2.3e-04 | صَبِيّ *ṣabī* “child” (root صبو) | Jesus and Mary (1) + Zechariah and John (1) | 2 |
| 3.3e-04 | مُبْتَلِي *mubtalī* “test” (root بلو) | Noah (1) + Saul (Talut) and Goliath (1) | 2 |
| 4.6e-04 | صَرْح *ṣarḥ* “palace” (root صرح) | Moses (2) + Solomon (1) | 3 |
| 5.6e-04 | يَكْفُلُ *yakfulu* “rear” (root كفل) | Jesus and Mary (1) + Moses (2) | 3 |
| 5.6e-04 | جِذْع *jidhʿ* “trunk” (root جذع) | Jesus and Mary (2) + Moses (1) | 3 |
| 6.1e-04 | مُجِيب *mujīb* “responsive” (root جوب) | Noah (1) + Salih and Thamud (1) | 2 |
| 6.3e-04 | فَتَى *fatā* “boy” (root فتي) | Joseph (1) + Moses (2) | 3 |
| 6.3e-04 | أَبْرَحَ *ʾabraḥa* “cease” (root برح) | Joseph (1) + Moses (2) | 3 |
| 6.6e-04 | سَفِينَة *safīna* “ship” (root سفن) | Moses (2) + Noah (1) | 3 |
| 7.7e-04 | صَلَبُ *ṣalabu* “crucified” (root صلب) | Jesus and Mary (1) + Joseph (1) | 2 |
| 9.3e-04 | سَقِيم *saqīm* “sick” (root سقم) | Abraham (1) + Jonah (1) | 2 |
| 9.5e-04 | أَوْجَسَ *ʾawjasa* “felt” (root وجس) | Abraham (2) + Moses (1) | 3 |
| 9.5e-04 | حَرِّقُ *ḥarriqu* “burn” (root حرق) | Abraham (2) + Moses (1) | 3 |
| 9.7e-04 | عَصِيّ *ʿaṣī* “disobedient” (root عصي) | Abraham (1) + Zechariah and John (1) | 2 |
| 1.1e-03 | تَبْتَئِسْ *tabtaʾis* “distressed” (root باس) | Joseph (1) + Noah (1) | 2 |
| 1.3e-03 | تَماثِيل *tamāthīl* “statue” (root مثل) | Abraham (1) + Solomon (1) | 2 |
| 1.5e-03 | مُنَجُّو *munajjū* “save” (root نجو) | Abraham (1) + Lot (1) | 2 |
| 5.1e-03 | تابُوت *tābūt* “ark” (no root: loanword candidate) · Hebrew cognate תֵּבָה *têbâh* H8392 · **cognate is also a Hebrew Bible bridge** | Moses (1) + Saul (Talut) and Goliath (1) | 2 |
| 5.3e-03 | خُبْر *khubr* “any” (root خبر) | Dhul-Qarnayn (1) + Moses (1) | 2 |
| 5.3e-03 | مُلِيم *mulīm* “blameworthy” (root لوم) | Jonah (1) + Moses (1) | 2 |
| 5.9e-03 | مُفْتَري *muftary* “invent” (root فري) | Hud and ʿAd (1) + Moses (1) | 2 |
| 6.5e-03 | رُكْن *rukn* “support” (root ركن) | Lot (1) + Moses (1) | 2 |
| 6.5e-03 | مُشْرِق *mushriq* “sunrise” (root شرق) | Lot (1) + Moses (1) | 2 |
| 6.7e-03 | يَتَكَبَّرُ *yatakabbaru* “arrogant” (root كبر) | Adam and Iblis (1) + Moses (1) | 2 |
| 6.7e-03 | عالي *ʿāly* “haughty” (root علو) | Adam and Iblis (1) + Moses (1) | 2 |
| 7.4e-03 | الْتَقَطَ *altaqaṭa* “pick” (root لقط) · Hebrew cognate לָקַט *lâqaṭ* H3950 | Joseph (1) + Moses (1) | 2 |
| 7.4e-03 | نَجا *najā* “saved” (root نجو) | Joseph (1) + Moses (1) | 2 |
| 7.4e-03 | نَجِيّ *najī* “private” (root نجو) | Joseph (1) + Moses (1) | 2 |
| 7.6e-03 | طُوفان *ṭūfān* “flood” (root طوف) | Moses (1) + Noah (1) | 2 |

## Hebrew Bible: concentration (79 candidates)

| Score | Lemma | Narrative | In narrative | Units | q | Flags |
|---|---|---|---|---|---|---|
| 98.38 | תֵּבָה *têbâh* “a box” (H8392) | Noah and the Flood | 23/25 (92%; base 0%) | 4 | 1.3e-51 | synonym skew vs אָרוֹן (174, 0% here) |
| 73.13 | מִלָּה *millâh* “a word” (H4405) | Job | 34/38 (89%; base 5%) | 21 | 1.8e-39 | synonym skew vs דָּבָר (1290, 2% here) |
| 35.16 | דָּת *dâth* “a royal edict or statute” (H1881) | Esther | 19/21 (90%; base 1%) | 6 | 1.4e-37 |  |
| 31.12 | מַלְכָּה *malkâh* “a queen” (H4436) | Esther | 24/34 (71%; base 1%) | 7 | 1.6e-42 |  |
| 30.08 | מְדִינָה *mᵉdîynâh* “properly, a judgeship, i.e. jurisdiction” (H4082) | Esther | 26/40 (65%; base 1%) | 6 | 1.3e-44 |  |
| 28.25 | אֱלוֹהַּ *ʼĕlôwahh* “a deity or the Deity” (H433) | Job | 41/59 (69%; base 5%) | 23 | 2.7e-39 |  |
| 24.45 | פָּתַר *pâthar* “to open up, i.e. (figuratively) interpret (a dream)” (H6622) | Joseph | 7/7 (100%; base 2%) | 2 | 7.7e-12 | synonym skew vs פָּקַח (18, 0% here), פָּתַח (133, 3% here) |
| 20.93 | דְּבִיר *dᵉbîyr* “the shrine or innermost part of the sanctuary” (H1687) | Solomon | 15/16 (94%; base 3%) | 6 | 2.3e-21 |  |
| 15.67 | מַעֲרָכָה *maʻărâkâh* “an arrangement” (H4634) | Saul | 11/18 (61%; base 3%) | 2 | 2.3e-12 | synonym skew vs עֵדֶר (34, 3% here) |
| 13.97 | שָׁבַר *shâbar* “to deal in grain” (H7666) | Joseph | 14/20 (70%; base 2%) | 5 | 3.8e-19 |  |
| 12.87 | יָשַׁט *yâshaṭ* “to extend” (H3447) | Esther | 3/3 (100%; base 1%) | 3 | 1.8e-06 | synonym skew vs סָרַח (7, 0% here) |
| 12.66 | נָקֹד *nâqôd* “spotted” (H5348) | Jacob | 7/7 (100%; base 2%) | 2 | 3.2e-12 |  |
| 12.51 | מִקְלַעַת *miqlaʻath* “a sculpture (probably in bas-relief)” (H4734) | Solomon | 4/4 (100%; base 3%) | 2 | 2.6e-06 | synonym skew vs פִּתּוּחַ (11, 27% here) |
| 12.51 | שָׁחַט *shâchaṭ* “to hammer out” (H7820) | Solomon | 4/4 (100%; base 3%) | 2 | 2.6e-06 | synonym skew vs לָטַשׁ (5, 0% here) |
| 11.55 | כֹתֶרֶת *kôthereth* “the capital of a column” (H3805) | Solomon | 10/12 (83%; base 3%) | 2 | 2.4e-13 |  |
| 11.04 | בִּירָה *bîyrâh* “a castle or palace” (H1002) | Esther | 10/16 (62%; base 1%) | 5 | 6.5e-17 |  |
| 10.98 | מַבּוּל *mabbûwl* “a deluge” (H3999) | Noah and the Flood | 8/12 (67%; base 0%) | 3 | 8.0e-16 |  |
| 10.9 | פַּתְבַּג *pathbag* “a dainty” (H6598) | Daniel | 6/6 (100%; base 2%) | 2 | 1.3e-10 |  |
| 10.85 | עָקֹד *ʻâqôd* “striped (with bands)” (H6124) | Jacob | 6/6 (100%; base 2%) | 2 | 1.5e-10 |  |
| 10.7 | יָשִׁישׁ *yâshîysh* “an old man” (H3453) | Job | 4/4 (100%; base 5%) | 4 | 1.7e-05 | synonym skew vs זָקֵן (171, 2% here), יָשָׁן (5, 0% here) |
| 10.48 | סֹהַר *çôhar* “a dungeon (as surrounded by walls)” (H5470) | Joseph | 6/6 (100%; base 2%) | 2 | 3.3e-10 |  |
| 9.89 | צְפַרְדֵּעַ *tsᵉphardêaʻ* “a marsh-leaper, i.e. frog” (H6854) | Moses | 11/13 (85%; base 6%) | 2 | 2.4e-11 |  |
| 9.87 | חָוָה *châvâh* “properly, to live” (H2331) | Job | 5/6 (83%; base 5%) | 3 | 5.0e-06 | synonym skew vs חָיַי (20, 0% here), חָיָה (239, 2% here) |
| 8.91 | אֳנִי *ʼŏnîy* “-a ship or (collectively) a fleet” (H590) | Solomon | 4/5 (80%; base 3%) | 2 | 1.1e-05 | synonym skew vs אֳנִיָּה (28, 11% here) |
| 8.76 | דָּחַף *dâchaph* “to urge, i.e. hasten” (H1765) | Esther | 3/4 (75%; base 1%) | 3 | 6.0e-06 | synonym skew vs עָנַשׁ (8, 0% here) |
| 8.76 | גִּנָּה *ginnâh* “a garden” (H1594) | Esther | 3/4 (75%; base 1%) | 2 | 6.0e-06 | synonym skew vs גַּן (37, 0% here), כֶּרֶם (81, 0% here) |
| 8.73 | פִּתְרוֹן *pithrôwn* “interpretation (of a dream)” (H6623) | Joseph | 5/5 (100%; base 2%) | 2 | 1.4e-08 |  |
| 8.31 | שֶׁבֶר *sheber* “grain (as if broken into kernels)” (H7668) | Joseph | 7/9 (78%; base 2%) | 4 | 2.1e-10 |  |
| 7.82 | עָגֹל *ʻâgôl* “circular” (H5696) | Solomon | 5/5 (100%; base 3%) | 3 | 1.0e-07 |  |
| 7.82 | מְכוֹנָה *mᵉkôwnâh* “a pedestal, also a spot” (H4350) | Solomon | 11/18 (61%; base 3%) | 2 | 2.4e-12 |  |
| 7.46 | עַוָּל *ʻavvâl* “evil (morally)” (H5767) | Job | 4/5 (80%; base 5%) | 4 | 6.5e-05 | synonym skew vs שָׁוְא (48, 10% here) |
| 6.44 | בִּיתָן *bîythân* “a palace (i.e. large house)” (H1055) | Esther | 3/3 (100%; base 1%) | 2 | 1.8e-06 |  |
| 6.44 | כֶּתֶר *kether* “properly, a circlet, i.e. a diadem” (H3804) | Esther | 3/3 (100%; base 1%) | 3 | 1.8e-06 |  |
| 6.44 | מַאֲמַר *maʼămar* “something (authoritatively) said, i.e. an edict” (H3982) | Esther | 3/3 (100%; base 1%) | 3 | 1.8e-06 |  |
| 6.44 | שַׁרְבִיט *sharbîyṭ* “a rod of empire” (H8275) | Esther | 3/3 (100%; base 1%) | 3 | 1.8e-06 |  |
| 6.24 | אֹפֶל *ʼôphel* “dusk” (H652) | Job | 5/8 (62%; base 5%) | 5 | 3.4e-05 | synonym skew vs עֶרֶב (125, 2% here) |
| 6.15 | טֵפַח *ṭêphach* “a spread of the hand, i.e. a palm-breadth (not 'span' of the fingers)” (H2947) | Solomon | 3/4 (75%; base 3%) | 2 | 2.0e-04 | synonym skew vs טֹפַח (5, 0% here), זֶרֶת (5, 0% here) |
| 6.15 | חֵשֶׁק *chêsheq* “delight” (H2837) | Solomon | 3/4 (75%; base 3%) | 2 | 2.0e-04 | synonym skew vs חֶמְדָּה (18, 0% here), מָשׂוֹשׂ (16, 0% here) |
| 5.94 | בָּרָה *bârâh* “to select” (H1262) | David | 6/7 (86%; base 5%) | 4 | 6.8e-07 |  |
| 5.92 | סַר *çar* “peevish” (H5620) | Elijah | 3/3 (100%; base 1%) | 2 | 5.0e-06 |  |

## Hebrew Bible: bridges (40 candidates)

| p | Lemma | Narratives | Verses |
|---|---|---|---|
| 4.9e-45 | מַלְכָּה *malkâh* “a queen” (H4436) | Esther (24) + Solomon (8) | 34 |
| 1.9e-32 | מִלָּה *millâh* “a word” (H4405) | David (1) + Job (34) | 38 |
| 8.6e-31 | תֵּבָה *têbâh* “a box” (H8392) | Moses (2) + Noah and the Flood (23) | 25 |
| 4.6e-23 | דָּת *dâth* “a royal edict or statute” (H1881) | Esther (19) + Moses (1) | 21 |
| 6.2e-09 | בְּכִירָה *bᵉkîyrâh* “the eldest daughter” (H1067) | Jacob (1) + Saul (1) | 6 |
| 8.2e-08 | בְּשׂוֹרָה *bᵉsôwrâh* “glad tidings” (H1309) | David (5) + Elisha (1) | 6 |
| 8.6e-07 | אוּת *ʼûwth* “properly, to come, i.e. (implied) to assent” (H225) | Elisha (1) + Jacob (3) | 4 |
| 1.6e-06 | פַּס *paç* “a long and sleeved tunic (perhaps simply a wide one” (H6446) | David (2) + Joseph (3) | 5 |
| 2.7e-06 | אָסוֹן *ʼâçôwn* “hurt” (H611) | Joseph (3) + Moses (2) | 5 |
| 1.1e-05 | פַּרְתַּם *partam* “a grandee” (H6579) | Daniel (1) + Esther (2) | 3 |
| 1.1e-05 | תֹּקֶף *tôqeph* “might or (figuratively) positiveness” (H8633) | Daniel (1) + Esther (2) | 3 |
| 1.6e-05 | גָּהַר *gâhar* “to prostrate oneself” (H1457) | Elijah (1) + Elisha (2) | 3 |
| 2.5e-05 | קֶצֶב *qetseb* “shape (as if cut out)” (H7095) | Jonah (1) + Solomon (2) | 3 |
| 7.4e-05 | פַּךְ *pak* “a flask (from which a liquid may flow)” (H6378) | Elisha (2) + Saul (1) | 3 |
| 1.2e-04 | מְרֹרָה *mᵉrôrâh* “properly, bitterness” (H4846) | Job (3) + Moses (1) | 4 |
| 1.8e-04 | סָעִף *çâʻiph* “divided (in mind), i.e. (abstractly) a sentiment” (H5587) | Elijah (1) + Job (2) | 3 |
| 2.6e-04 | אָחוּ *ʼâchûw* “a bulrush or any marshy grass (particularly that along the Nile)” (H260) | Job (1) + Joseph (2) | 3 |
| 4.0e-04 | מוּצָק *mûwtsâq* “properly, fusion, i.e. literally, a casting (of metal)” (H4165) | Job (1) + Solomon (2) | 3 |
| 4.2e-04 | מֹהַר *môhar* “a price (for a wife)” (H4119) | Jacob (1) + Moses (1) | 3 |
| 5.2e-04 | רֶוַח *revach* “room, literally (an interval) or figuratively (deliverance)” (H7305) | Esther (1) + Jacob (1) | 2 |
| 8.1e-04 | חֹרֵשׁ *chôrêsh* “a fabricator or mechanic” (H2794) | Cain and Abel (1) + Solomon (1) | 2 |
| 1.0e-03 | שֹׁקֶת *shôqeth* “a trough (for watering)” (H8268) | Abraham (1) + Jacob (1) | 2 |
| 1.2e-03 | פָּלִיל *pâlîyl* “a magistrate” (H6414) | Job (1) + Moses (2) | 3 |
| 1.2e-03 | יָשַׂם *yâsam* “to place” (H3455) | Abraham (1) + Joseph (1) | 2 |
| 1.4e-03 | זֹנוֹת *zônôwth* “harlots” (H2185) | Elijah (1) + Solomon (1) | 2 |
| 2.5e-03 | אֵד *ʼêd* “a fog” (H108) | Creation and Eden (1) + Job (1) | 2 |
| 2.5e-03 | אֶרֶג *ʼereg* “a weaving” (H708) | Job (1) + Samson (1) | 2 |
| 3.6e-03 | הֵלֶךְ *hêlek* “properly, a journey, i.e. (by implication) a wayfarer” (H1982) | David (1) + Saul (1) | 2 |
| 3.8e-03 | עֲבֻדָּה *ʻăbuddâh* “something wrought, i.e. (concretely) service” (H5657) | Jacob (1) + Job (1) | 2 |
| 3.9e-03 | בְּדֹלַח *bᵉdôlach* “something in pieces, i.e. bdellium, a (fragrant) gum (perhaps amber)” (H916) | Creation and Eden (1) + Moses (1) | 2 |
| 3.9e-03 | לַהַט *lahaṭ* “a blaze” (H3858) | Creation and Eden (1) + Moses (1) | 2 |
| 4.0e-03 | נְפִיל *nᵉphîyl* “properly, a feller, i.e. a bully or tyrant” (H5303) | Moses (1) + Noah and the Flood (1) | 2 |
| 4.8e-03 | פָּזַז *pâzaz* “to solidify (as if by refining)” (H6339) | David (1) + Joseph (1) | 2 |
| 5.4e-03 | שִׂיב *sîyb* “properly, to become aged, i.e. (by implication) to grow gray” (H7867) | Job (1) + Saul (1) | 2 |
| 5.4e-03 | מַסָּע *maççâʻ* “a missile (spear or arrow)” (H4551) | Job (1) + Solomon (1) | 2 |
| 5.5e-03 | רֹבַע *rôbaʻ* “a quarter” (H7255) | Elisha (1) + Moses (1) | 2 |
| 5.5e-03 | חָם *châm* “hot” (H2525) | Job (1) + Joshua (1) | 2 |
| 5.7e-03 | גּוֹזָל *gôwzâl* “a nestling (as being comparatively nude of feathers)” (H1469) | Abraham (1) + Moses (1) | 2 |
| 1.1e-02 | יָרַט *yâraṭ* “to precipitate or hurl (rush) headlong” (H3399) | Job (1) + Moses (1) | 2 |
| 1.2e-02 | חָזֵק *châzêq* “powerful” (H2390) | David (1) + Moses (1) | 2 |
