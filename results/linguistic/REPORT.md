# Linguistic layer

Generated 2026-10-29 by `tools/linguistic.py` over the whole Hebrew Bible (23,213 verses, Hebrew and Aramaic) and the whole Quran (6,216 verses). Full data is in `linguistic.json`.

Phrases are sequences of content lemmas (nouns including names, verbs, adjectives) inside one verse, found in at least two chapters or surahs. Function words are skipped, so a phrase can match across different prepositions and particles. Score: the rarer the words and the rarer the sequence, the higher.

## Hebrew Bible: summary

- Phrase echoes (≤12 occurrences, outside doublet chapters): 7,922
- Stock formulas (>12 occurrences): 219
- Name-heavy sequences (genealogies, lists), listed in the JSON only: 975
- Doublet chapter pairs (verbatim parallels): 202
- Hapax legomena (lemma occurs once): 2,539; dis legomena: 1,293
- Loanword candidates by Strong's derivation: 123 (a dated 1894 lexicon; treat as leads)

## Hebrew Bible: top phrase echoes

| Score | Phrase (lemmas) | Count | Places |
|---|---|---|---|
| 71.82 | כֹּל *kôl* · עַם *ʻam* · אֻמָּה *ʼummâh* · לִשָּׁן *lishshân* · דּוּר *dûwr* · דּוּר *dûwr* · כֹּל *kôl* · אֲרַע *ʼăraʻ* · שְׁלָם *shᵉlâm* · שְׂגָא *sᵉgâʼ* | 2 | Dan 3:31, Dan 6:26 |
| 54.35 | קָצַר *qâtsar* · קָצִיר *qâtsîyr* · אֶרֶץ *ʼerets* · כָּלָה *kâlâh* · פֵּאָה *pêʼâh* · שָׂדֶה *sâdeh* · קָצַר *qâtsar* · לֶקֶט *leqeṭ* · קָצִיר *qâtsîyr* · לָקַט *lâqaṭ* | 2 | Lev 19:9, Lev 23:22 |
| 51.71 | שָׁבַע *shâbaʻ* · בַּת *bath* · יְרוּשָׁלַ͏ִם *Yᵉrûwshâlaim* · צְבִי *tsᵉbîy* · אַיָּלָה *ʼayâlâh* · שָׂדֶה *sâdeh* · עוּר *ʻûwr* · עוּר *ʻûwr* · אַהֲבָה *ʼahăbâh* · חָפֵץ *châphêts* | 2 | Song 2:7, Song 3:5 |
| 45.83 | מְעַט *mᵉʻaṭ* · שֵׁנָה *shênâh* · מְעַט *mᵉʻaṭ* · תְּנוּמָה *tᵉnûwmâh* · מְעַט *mᵉʻaṭ* · חִבֻּק *chibbuq* · יָד *yâd* · שָׁכַב *shâkab* | 2 | Prov 24:33, Prov 6:10 |
| 45.79 | תְּכֵלֶת *tᵉkêleth* · אַרְגָּמָן *ʼargâmân* · תּוֹלָע *tôwlâʻ* · שָׁנִי *shânîy* · שֵׁשׁ *shêsh* · שָׁזַר *shâzar* · מַעֲשֶׂה *maʻăseh* · רָקַם *râqam* | 3 | Exod 26:36, Exod 27:16, Exod 36:37 |
| 45.25 | חֹדֶשׁ *chôdesh* · שְׁבִיעִי *shᵉbîyʻîy* · בּוֹא *bôwʼ* · יִשְׁמָעֵאל *Yishmâʻêʼl* · בֵּן *bên* · נְתַנְיָה *Nᵉthanyâh* · בֵּן *bên* · אֱלִישָׁמָע *ʼĔlîyshâmâʻ* · זֶרַע *zeraʻ* · מְלוּכָה *mᵉlûwkâh* | 2 | 2Kgs 25:25, Jer 41:1 |
| 44.97 | חַלָּה *challâh* · מַצָּה *matstsâh* · בָּלַל *bâlal* · שֶׁמֶן *shemen* · רָקִיק *râqîyq* · מַצָּה *matstsâh* · מָשַׁח *mâshach* · שֶׁמֶן *shemen* | 3 | Exod 29:2, Lev 2:4, Lev 7:12 |
| 44.48 | צִיּוֹן *Tsîyôwn* · שָׂדֶה *sâdeh* · חָרַשׁ *chârash* · יְרוּשָׁלַ͏ִם *Yᵉrûwshâlaim* · עִי *ʻîy* · הָיָה *hâyâh* · הַר *har* · בַּיִת *bayith* · בָּמָה *bâmâh* · יַעַר *yaʻar* | 2 | Jer 26:18, Mic 3:12 |
| 44.43 | פֶּטֶר *peṭer* · חֲמוֹר *chămôwr* · פָּדָה *pâdâh* · שֶׂה *seh* · פָּדָה *pâdâh* · עָרַף *ʻâraph* · כֹּל *kôl* · בְּכוֹר *bᵉkôwr* | 2 | Exod 13:13, Exod 34:20 |
| 43.68 | יָבֵשׁ *yâbêsh* · תּוֹעֵבַה *tôwʻêbah* · עָשָׂה *ʻâsâh* · בּוּשׁ *bûwsh* · בּוּשׁ *bûwsh* · כָּלַם *kâlam* · יָדַע *yâdaʻ* · נָפַל *nâphal* · נָפַל *nâphal* · עֵת *ʻêth* | 2 | Jer 6:15, Jer 8:12 |
| 43.46 | תְּכֵלֶת *tᵉkêleth* · אַרְגָּמָן *ʼargâmân* · תּוֹלָע *tôwlâʻ* · שָׁנִי *shânîy* · שֵׁשׁ *shêsh* · שָׁזַר *shâzar* · מַעֲשֶׂה *maʻăseh* · חָשַׁב *châshab* | 3 | Exod 26:31, Exod 28:6, Exod 36:35 |
| 43.08 | קוֹל *qôwl* · שָׂשׂוֹן *sâsôwn* · קוֹל *qôwl* · שִׂמְחָה *simchâh* · קוֹל *qôwl* · חָתָן *châthân* · קוֹל *qôwl* · כַּלָּה *kallâh* · קוֹל *qôwl* | 2 | Jer 25:10, Jer 33:11 |
| 42.6 | עָלָה *ʻâlâh* · נָשִׂיא *nâsîyʼ* · קָצֶה *qâtseh* · אֶרֶץ *ʼerets* · בָּרָק *bârâq* · מָטַר *mâṭar* · עָשָׂה *ʻâsâh* · יָצָא *yâtsâʼ* · רוּחַ *rûwach* · אוֹצָר *ʼôwtsâr* | 2 | Jer 51:16, Ps 135:7 |
| 42.56 | רוּם *rûwm* · אַמָּה *ʼammâh* · שִׁתִּין *shittîyn* · פְּתַי *pᵉthay* · אַמָּה *ʼammâh* | 2 | Dan 3:1, Ezra 6:3 |
| 42.45 | אֵל *ʼêl* · רַחוּם *rachûwm* · חַנּוּן *channûwn* · אָרֵךְ *ʼârêk* · אַף *ʼaph* · רַב *rab* · חֵסֵד *chêçêd* · אֶמֶת *ʼemeth* | 2 | Exod 34:6, Ps 86:15 |
| 42.17 | שְׁנַיִם *shᵉnayim* · כִּלְיָה *kilyâh* · חֶלֶב *cheleb* · כֶּסֶל *keçel* · יֹתֶרֶת *yôthereth* · כָּבֵד *kâbêd* · כִּלְיָה *kilyâh* · סוּר *çûwr* | 5 | Lev 3:10, Lev 3:15, Lev 3:4, Lev 4:9, Lev 7:4 |
| 41.74 | חַנּוּן *channûwn* · רַחוּם *rachûwm* · אָרֵךְ *ʼârêk* · אַף *ʼaph* · רַב *rab* · חֵסֵד *chêçêd* · נָחַם *nâcham* · רַע *raʻ* | 2 | Joel 2:13, Jonah 4:2 |
| 40.65 | הָיָה *hâyâh* · חֹדֶשׁ *chôdesh* · שְׁבִיעִי *shᵉbîyʻîy* · בּוֹא *bôwʼ* · יִשְׁמָעֵאל *Yishmâʻêʼl* · בֵּן *bên* · נְתַנְיָה *Nᵉthanyâh* · בֵּן *bên* · אֱלִישָׁמָע *ʼĔlîyshâmâʻ* · זֶרַע *zeraʻ* | 2 | 2Kgs 25:25, Jer 41:1 |
| 39.8 | קָטָן *qâṭân* · גָּדוֹל *gâdôwl* · כֹּל *kôl* · בָּצַע *bâtsaʻ* · בֶּצַע *betsaʻ* · נָבִיא *nâbîyʼ* · כֹּהֵן *kôhên* · כֹּל *kôl* · עָשָׂה *ʻâsâh* · שֶׁקֶר *sheqer* | 2 | Jer 6:13, Jer 8:10 |
| 39.36 | נָחַל *nâchal* · אֶלְעָזָר *ʼElʻâzâr* · כֹּהֵן *kôhên* · יְהוֹשׁוּעַ *Yᵉhôwshûwaʻ* · בֵּן *bên* · נוּן *Nûwn* · רֹאשׁ *rôʼsh* · אָב *ʼâb* · מַטֶּה *maṭṭeh* · בֵּן *bên* | 2 | Josh 14:1, Josh 19:51 |
| 39.32 | אֵילִם *ʼÊylim* · שְׁנַיִם *shᵉnayim* · עָשָׂר *ʻâsâr* · עַיִן *ʻayin* · מַיִם *mayim* · שִׁבְעִים *shibʻîym* · תָּמָר *tâmâr* · חָנָה *chânâh* | 2 | Exod 15:27, Num 33:9 |
| 39.03 | שָׁחַח *shâchach* · נֶפֶשׁ *nephesh* · הָמָה *hâmâh* · יָחַל *yâchal* · אֱלֹהִים *ʼĕlôhîym* · יָדָה *yâdâh* · יְשׁוּעָה *yᵉshûwʻâh* · פָּנִים *pânîym* · אֱלֹהִים *ʼĕlôhîym* | 2 | Ps 42:12, Ps 43:5 |
| 38.87 | חָדָשׁ *châdâsh* · נָתַן *nâthan* · קֶרֶב *qereb* · סוּר *çûwr* · לֵב *lêb* · אֶבֶן *ʼeben* · בָּשָׂר *bâsâr* · נָתַן *nâthan* · לֵב *lêb* · בָּשָׂר *bâsâr* | 2 | Ezek 11:19, Ezek 36:26 |
| 38.52 | רוּחַ *rûwach* · חָדָשׁ *châdâsh* · נָתַן *nâthan* · קֶרֶב *qereb* · סוּר *çûwr* · לֵב *lêb* · אֶבֶן *ʼeben* · בָּשָׂר *bâsâr* · נָתַן *nâthan* · לֵב *lêb* | 2 | Ezek 11:19, Ezek 36:26 |
| 38.4 | יָצָא *yâtsâʼ* · אֵשׁ *ʼêsh* · חֵמָה *chêmâh* · בָּעַר *bâʻar* · כָּבָה *kâbâh* · פָּנִים *pânîym* · רֹעַ *rôaʻ* · מַעֲלָל *maʻălâl* | 2 | Jer 21:12, Jer 4:4 |
| 38.05 | שָׁלוֹשׁ *shâlôwsh* · טוּר *ṭûwr* · גָּזִית *gâzîyth* · טוּר *ṭûwr* · כָּרֻתָה *kâruthâh* · אֶרֶז *ʼerez* | 2 | 1Kgs 6:36, 1Kgs 7:12 |
| 37.91 | שְׁנַיִם *shᵉnayim* · שַׁד *shad* · שְׁנַיִם *shᵉnayim* · עֹפֶר *ʻôpher* · תָּאוֹם *tâʼôwm* · צְבִיָּה *tsᵉbîyâh* | 2 | Song 4:5, Song 7:4 |
| 37.9 | נָתַן *nâthan* · בָּלָק *Bâlâq* · מְלֹא *mᵉlôʼ* · בַּיִת *bayith* · כֶּסֶף *keçeph* · זָהָב *zâhâb* · יָכֹל *yâkôl* · עָבַר *ʻâbar* · פֶּה *peh* · יְהֹוָה *Yᵉhôvâh* | 2 | Num 22:18, Num 24:13 |
| 37.63 | מַצֵּבָה *matstsêbâh* · אֲשֵׁרָה *ʼăshêrâh* · כֹּל *kôl* · גִּבְעָה *gibʻâh* · גָּבֹהַּ *gâbôahh* · כֹּל *kôl* · עֵץ *ʻêts* · רַעֲנָן *raʻănân* | 2 | 1Kgs 14:23, 2Kgs 17:10 |
| 37.54 | שׂוּם *sûwm* · מִדְבָּר *midbâr* · אֲגַם *ʼăgam* · מַיִם *mayim* · אֶרֶץ *ʼerets* · צִיָּה *tsîyâh* · מוֹצָא *môwtsâʼ* · מַיִם *mayim* | 2 | Isa 41:18, Ps 107:35 |
| 37.45 | מִין *mîyn* · בְּהֵמָה *bᵉhêmâh* · מִין *mîyn* · כֹּל *kôl* · רֶמֶשׂ *remes* · אֲדָמָה *ʼădâmâh* · מִין *mîyn* | 2 | Gen 1:25, Gen 6:20 |
| 37.18 | שָׁכַב *shâkab* · שְׁלֹמֹה *Shᵉlômôh* · אָב *ʼâb* · קָבַר *qâbar* · עִיר *ʻîyr* · דָּוִד *Dâvid* · אָב *ʼâb* · מָלַךְ *mâlak* · רְחַבְעָם *Rᵉchabʻâm* · בֵּן *bên* | 2 | 1Kgs 11:43, 2Chr 9:31 |
| 36.92 | עֶשְׂרִים *ʻesrîym* · אֶחָד *ʼechâd* · שָׁנֶה *shâneh* · צִדְקִיָּה *Tsidqîyâh* · מָלַךְ *mâlak* · אֶחָד *ʼechâd* · עָשָׂר *ʻâsâr* · שָׁנֶה *shâneh* · מָלַךְ *mâlak* · יְרוּשָׁלַ͏ִם *Yᵉrûwshâlaim* | 3 | 2Chr 36:11, 2Kgs 24:18, Jer 52:1 |
| 36.83 | אֵל *ʼêl* · גָּדוֹל *gâdôwl* · יָרֵא *yârêʼ* · שָׁמַר *shâmar* · בְּרִית *bᵉrîyth* · חֵסֵד *chêçêd* · אָהַב *ʼâhab* · שָׁמַר *shâmar* · מִצְוָה *mitsvâh* | 2 | Dan 9:4, Neh 1:5 |
| 36.76 | תָּמָר *Tâmâr* · מַיִם *mayim* · מְרִיבָה *mᵉrîybâh* · קָדֵשׁ *Qâdêsh* · נַחַל *nachal* · יָם *yâm* · גָּדוֹל *gâdôwl* | 2 | Ezek 47:19, Ezek 48:28 |
| 36.45 | קוֹל *qôwl* · שָׂשׂוֹן *sâsôwn* · קוֹל *qôwl* · שִׂמְחָה *simchâh* · קוֹל *qôwl* · חָתָן *châthân* · קוֹל *qôwl* · כַּלָּה *kallâh* | 4 | Jer 16:9, Jer 25:10, Jer 33:11, Jer 7:34 |
| 36.01 | יְמָנִי *yᵉmânîy* · בֹּהֶן *bôhen* · יָד *yâd* · יְמָנִי *yᵉmânîy* · בֹּהֶן *bôhen* · רֶגֶל *regel* · יְמָנִי *yᵉmânîy* | 7 | Exod 29:20, Lev 14:14, Lev 14:17, Lev 14:25, Lev 14:28, Lev 8:23, Lev 8:24 |
| 35.9 | חַג *chag* · מַצָּה *matstsâh* · חַג *chag* · שָׁבוּעַ *shâbûwaʻ* · חַג *chag* · סֻכָּה *çukkâh* | 2 | 2Chr 8:13, Deut 16:16 |
| 35.76 | תְּכֵלֶת *tᵉkêleth* · אַרְגָּמָן *ʼargâmân* · תּוֹלָע *tôwlâʻ* · שָׁנִי *shânîy* · שֵׁשׁ *shêsh* · שָׁזַר *shâzar* · מַעֲשֶׂה *maʻăseh* | 6 | Exod 26:31, Exod 26:36, Exod 27:16, Exod 28:6, Exod 36:35, Exod 36:37 |
| 35.3 | בֵּן *bên* · עֶשְׂרִים *ʻesrîym* · אֶחָד *ʼechâd* · שָׁנֶה *shâneh* · צִדְקִיָּה *Tsidqîyâh* · מָלַךְ *mâlak* · אֶחָד *ʼechâd* · עָשָׂר *ʻâsâr* · שָׁנֶה *shâneh* · מָלַךְ *mâlak* | 3 | 2Chr 36:11, 2Kgs 24:18, Jer 52:1 |
| 35.25 | שָׁחַח *shâchach* · נֶפֶשׁ *nephesh* · הָמָה *hâmâh* · יָחַל *yâchal* · אֱלֹהִים *ʼĕlôhîym* · יָדָה *yâdâh* · יְשׁוּעָה *yᵉshûwʻâh* · פָּנִים *pânîym* | 3 | Ps 42:12, Ps 42:6, Ps 43:5 |
| 35.18 | שֶׁמֶשׁ *shemesh* · יָרֵחַ *yârêach* · קָדַר *qâdar* · כּוֹכָב *kôwkâb* · אָסַף *ʼâçaph* · נֹגַהּ *nôgahh* | 2 | Joel 2:10, Joel 4:15 |
| 35.12 | לָקַח *lâqach* · יוֹחָנָן *Yôwchânân* · בֵּן *bên* · קָרֵחַ *Qârêach* · כֹּל *kôl* · שַׂר *sar* · חַיִל *chayil* · כֹּל *kôl* · שְׁאֵרִית *shᵉʼêrîyth* | 2 | Jer 41:16, Jer 43:5 |
| 35.06 | דָּבָר *dâbâr* · נִרְגָּן *nirgân* · לָהַם *lâham* · יָרַד *yârad* · חֶדֶר *cheder* · בֶּטֶן *beṭen* | 2 | Prov 18:8, Prov 26:22 |
| 34.86 | כֹּל *kôl* · בְּכוֹר *bᵉkôwr* · אֶרֶץ *ʼerets* · מִצְרַיִם *Mitsrayim* · בְּכוֹר *bᵉkôwr* · פַּרְעֹה *Parʻôh* · יָשַׁב *yâshab* · כִּסֵּא *kiççêʼ* · בְּכוֹר *bᵉkôwr* | 2 | Exod 11:5, Exod 12:29 |
| 34.86 | עוֹר *ʻôwr* · אַיִל *ʼayil* · אָדַם *ʼâdam* · מִכְסֶה *mikçeh* · עוֹר *ʻôwr* · תַּחַשׁ *tachash* | 3 | Exod 26:14, Exod 36:19, Exod 39:34 |
| 34.59 | שֵׁשׁ *shêsh* · שָׁזַר *shâzar* · תְּכֵלֶת *tᵉkêleth* · אַרְגָּמָן *ʼargâmân* · תּוֹלָע *tôwlâʻ* · שָׁנִי *shânîy* | 3 | Exod 26:1, Exod 36:8, Exod 39:29 |
| 34.36 | תְּעָלָה *tᵉʻâlâh* · בְּרֵכָה *bᵉrêkâh* · עֶלְיוֹן *ʻelyôwn* · מְסִלָּה *mᵉçillâh* · שָׂדֶה *sâdeh* · כָּבַס *kâbaç* | 3 | 2Kgs 18:17, Isa 36:2, Isa 7:3 |
| 33.97 | נָסַע *nâçaʻ* · סֻכּוֹת *Çukkôwth* · חָנָה *chânâh* · אֵתָם *ʼÊthâm* · קָצֶה *qâtseh* · מִדְבָּר *midbâr* | 2 | Exod 13:20, Num 33:6 |
| 33.78 | כְּנַעַנִי *Kᵉnaʻanîy* · חִתִּי *Chittîy* · אֱמֹרִי *ʼĔmôrîy* · פְּרִזִּי *Pᵉrizzîy* · חִוִּי *Chivvîy* · יְבוּסִי *Yᵉbûwçîy* | 3 | Exod 3:17, Exod 3:8, Judg 3:5 |
| 33.78 | חִתִּי *Chittîy* · אֱמֹרִי *ʼĔmôrîy* · כְּנַעַנִי *Kᵉnaʻanîy* · פְּרִזִּי *Pᵉrizzîy* · חִוִּי *Chivvîy* · יְבוּסִי *Yᵉbûwçîy* | 3 | Deut 20:17, Josh 12:8, Josh 9:1 |
| 33.65 | קָוָה *qâvâh* · שָׁלוֹם *shâlôwm* · טוֹב *ṭôwb* · עֵת *ʻêth* · מַרְפֵּא *marpêʼ* · בְּעָתָה *bᵉʻâthâh* | 2 | Jer 14:19, Jer 8:15 |
| 33.61 | שֵׁשׁ *shêsh* · יוֹם *yôwm* · עָשָׂה *ʻâsâh* · מְלָאכָה *mᵉlâʼkâh* · יוֹם *yôwm* · שְׁבִיעִי *shᵉbîyʻîy* · שַׁבָּת *shabbâth* · שַׁבָּתוֹן *shabbâthôwn* | 2 | Exod 31:15, Lev 23:3 |
| 33.56 | כֶּבֶשׂ *kebes* · שֵׁנִי *shênîy* · עָשָׂה *ʻâsâh* · עֶרֶב *ʻereb* · מִנְחָה *minchâh* · בֹּקֶר *bôqer* · נֶסֶךְ *neçek* · עָשָׂה *ʻâsâh* | 2 | Exod 29:41, Num 28:8 |
| 33.27 | אֶלְעָזָר *ʼElʻâzâr* · כֹּהֵן *kôhên* · יְהוֹשׁוּעַ *Yᵉhôwshûwaʻ* · בֵּן *bên* · נוּן *Nûwn* · רֹאשׁ *rôʼsh* · אָב *ʼâb* · מַטֶּה *maṭṭeh* · בֵּן *bên* · יִשְׂרָאֵל *Yisrâʼêl* | 4 | Josh 14:1, Josh 19:51, Josh 21:1, Num 32:28 |
| 32.84 | נֶגֶב *negeb* · מַעֲלֵה עַקְרַבִּים *Maʻălêh ʻAqrabbîym* · מַעֲלֵה עַקְרַבִּים *Maʻălêh ʻAqrabbîym* · עָבַר *ʻâbar* · צִן *Tsin* | 2 | Josh 15:3, Num 34:4 |
| 32.5 | יָרַשׁ *yârash* · כְּנַעַנִי *Kᵉnaʻanîy* · יָשַׁב *yâshab* · גֶּזֶר *Gezer* · יָשַׁב *yâshab* · כְּנַעַנִי *Kᵉnaʻanîy* · קֶרֶב *qereb* | 2 | Josh 16:10, Judg 1:29 |
| 32.22 | שָׂדֶה *sâdeh* · כֶּרֶם *kerem* · שָׁתָה *shâthâh* · מַיִם *mayim* · בְּאֵר *bᵉʼêr* · דֶּרֶךְ *derek* · מֶלֶךְ *melek* · יָלַךְ *yâlak* | 2 | Num 20:17, Num 21:22 |
| 32.11 | חֶרְפָּה *cherpâh* · שָׁכֵן *shâkên* · לַעַג *laʻag* · קֶלֶס *qeleç* · סָבִיב *çâbîyb* | 2 | Ps 44:14, Ps 79:4 |
| 32.05 | קוּם *qûwm* · עָפָר *ʻâphâr* · דַּל *dal* · אַשְׁפֹּת *ʼashpôth* · רוּם *rûwm* · אֶבְיוֹן *ʼebyôwn* | 2 | 1Sam 2:8, Ps 113:7 |
| 32.01 | שְׁלֹמֹה *Shᵉlômôh* · בַּיִת *bayith* · יְהֹוָה *Yᵉhôvâh* · בּוֹא *bôwʼ* · שְׁלֹמֹה *Shᵉlômôh* · קֹדֶשׁ *qôdesh* · דָּוִד *Dâvid* · אָב *ʼâb* · כֶּסֶף *keçeph* · זָהָב *zâhâb* | 2 | 1Kgs 7:51, 2Chr 5:1 |
| 31.86 | כֶּבֶשׂ *kebes* · אֶחָד *ʼechâd* · עָשָׂה *ʻâsâh* · בֹּקֶר *bôqer* · כֶּבֶשׂ *kebes* · שֵׁנִי *shênîy* · עָשָׂה *ʻâsâh* · עֶרֶב *ʻereb* | 2 | Exod 29:39, Num 28:4 |
| 31.83 | קָרָא *qârâʼ* · עָנָה *ʻânâh* · דָבַר *dâbar* · שָׁמַע *shâmaʻ* · עָשָׂה *ʻâsâh* · רַע *raʻ* · עַיִן *ʻayin* · חָפֵץ *châphêts* · בָּחַר *bâchar* | 2 | Isa 65:12, Isa 66:4 |
| 31.82 | חַנּוּן *channûwn* · רַחוּם *rachûwm* · אָרֵךְ *ʼârêk* · אַף *ʼaph* · רַב *rab* · חֵסֵד *chêçêd* | 3 | Joel 2:13, Jonah 4:2, Neh 9:17 |
| 31.63 | עַיִן *ʻayin* · עַיִן *ʻayin* · שֵׁן *shên* · שֵׁן *shên* · יָד *yâd* · יָד *yâd* · רֶגֶל *regel* · רֶגֶל *regel* | 2 | Deut 19:21, Exod 21:24 |
| 31.52 | רָגַע *râgaʻ* · יָם *yâm* · הָמָה *hâmâh* · גַּל *gal* · יְהֹוָה *Yᵉhôvâh* · צָבָא *tsâbâʼ* · שֵׁם *shêm* | 2 | Isa 51:15, Jer 31:35 |
| 31.47 | אָמַר *ʼâmar* · אָב *ʼâb* · אָכַל *ʼâkal* · בֹּסֶר *bôçer* · שֵׁן *shên* · בֵּן *bên* · קָהָה *qâhâh* | 2 | Ezek 18:2, Jer 31:29 |
| 31.42 | בָּלַל *bâlal* · שֶׁמֶן *shemen* · רָקִיק *râqîyq* · מַצָּה *matstsâh* · מָשַׁח *mâshach* · שֶׁמֶן *shemen* | 4 | Exod 29:2, Lev 2:4, Lev 7:12, Num 6:15 |
| 31.41 | קֶשֶׁר *qesher* · קָשַׁר *qâshar* · כָּתַב *kâthab* · סֵפֶר *çêpher* · דָּבָר *dâbâr* · יוֹם *yôwm* · מֶלֶךְ *melek* · יִשְׂרָאֵל *Yisrâʼêl* | 2 | 1Kgs 16:20, 2Kgs 15:15 |
| 31.33 | רְאוּבֵנִי *Rᵉʼûwbênîy* · גָּדִי *Gâdîy* · חֵצִי *chêtsîy* · שֵׁבֶט *shêbeṭ* · מְנַשִּׁי *Mᵉnashshîy* | 2 | 1Chr 26:32, Deut 29:7 |
| 31.05 | סִיחוֹן *Çîychôwn* · יִשְׂרָאֵל *Yisrâʼêl* · עָבַר *ʻâbar* · גְּבוּל *gᵉbûwl* · אָסַף *ʼâçaph* · סִיחוֹן *Çîychôwn* · כֹּל *kôl* · עַם *ʻam* | 2 | Judg 11:20, Num 21:23 |
| 31.05 | שָׁלוֹשׁ *shâlôwsh* · עִשָּׂרוֹן *ʻissârôwn* · סֹלֶת *çôleth* · מִנְחָה *minchâh* · בָּלַל *bâlal* · שֶׁמֶן *shemen* | 2 | Lev 14:10, Num 28:12 |
| 30.96 | שַׂר *sar* · אֶלֶף *ʼeleph* · שַׂר *sar* · מֵאָה *mêʼâh* · שַׂר *sar* · חֲמִשִּׁים *chămishshîym* · שַׂר *sar* · עֶשֶׂר *ʻeser* | 3 | Deut 1:15, Exod 18:21, Exod 18:25 |
| 30.92 | אָמַר *ʼâmar* · חֵלֶק *chêleq* · דָּוִד *Dâvid* · נַחֲלָה *nachălâh* · בֵּן *bên* · יִשַׁי *Yishay* · אִישׁ *ʼîysh* · אֹהֶל *ʼôhel* · יִשְׂרָאֵל *Yisrâʼêl* | 2 | 2Chr 10:16, 2Sam 20:1 |
| 30.92 | עִיר *ʻîyr* · אָכַל *ʼâkal* · כֶּלֶב *keleb* · מוּת *mûwth* · שָׂדֶה *sâdeh* · אָכַל *ʼâkal* · עוֹף *ʻôwph* · שָׁמַיִם *shâmayim* | 3 | 1Kgs 14:11, 1Kgs 16:4, 1Kgs 21:24 |
| 30.63 | שֵׁשׁ *shêsh* · מֵאָה *mêʼâh* · אֶלֶף *ʼeleph* · שָׁלוֹשׁ *shâlôwsh* · אֶלֶף *ʼeleph* · חָמֵשׁ *châmêsh* · מֵאָה *mêʼâh* · חֲמִשִּׁים *chămishshîym* | 3 | Exod 38:26, Num 1:46, Num 2:32 |
| 30.59 | כָּתַב *kâthab* · לוּחַ *lûwach* · דָּבָר *dâbâr* · הָיָה *hâyâh* · לוּחַ *lûwach* · רִאשׁוֹן *riʼshôwn* · שָׁבַר *shâbar* | 2 | Deut 10:2, Exod 34:1 |
| 30.56 | פָּרַשׂ *pâras* · רֶשֶׁת *resheth* · תָּפַשׂ *tâphas* · מָצוּד *mâtsûwd* · בּוֹא *bôwʼ* · בָּבֶל *Bâbel* | 2 | Ezek 12:13, Ezek 17:20 |
| 30.55 | אַרְבָּעִים *ʼarbâʻîym* · יוֹם *yôwm* · אַרְבָּעִים *ʼarbâʻîym* · לַיִל *layil* · לֶחֶם *lechem* · אָכַל *ʼâkal* · מַיִם *mayim* · שָׁתָה *shâthâh* | 3 | Deut 9:18, Deut 9:9, Exod 34:28 |
| 30.55 | מִשְׁפָּחָה *mishpâchâh* · מַחְלִי *Machlîy* · מִשְׁפָּחָה *mishpâchâh* · מוּשִׁי *Mûwshîy* · מִשְׁפָּחָה *mishpâchâh* | 2 | Num 26:58, Num 3:33 |
| 30.19 | חֲמִשִּׁים *chămishshîym* · אַמָּה *ʼammâh* · רֹחַב *rôchab* · שְׁלוֹשִׁים *shᵉlôwshîym* · אַמָּה *ʼammâh* · קוֹמָה *qôwmâh* | 2 | 1Kgs 7:2, Gen 6:15 |
| 30.14 | פֶּלַח *pelach* · רִמּוֹן *rimmôwn* · רַקָּה *raqqâh* · צַמָּה *tsammâh* | 2 | Song 4:3, Song 6:7 |
| 30.11 | הָיָה *hâyâh* · נְבֵלָה *nᵉbêlâh* · מַאֲכָל *maʼăkâl* · עוֹף *ʻôwph* · שָׁמַיִם *shâmayim* · בְּהֵמָה *bᵉhêmâh* · אֶרֶץ *ʼerets* | 2 | Jer 16:4, Jer 34:20 |
| 29.89 | אֱמֹרִי *ʼĔmôrîy* · חִתִּי *Chittîy* · פְּרִזִּי *Pᵉrizzîy* · חִוִּי *Chivvîy* · יְבוּסִי *Yᵉbûwçîy* | 2 | 1Kgs 9:20, Exod 33:2 |
| 29.66 | עָבַד *ʻâbad* · אֲדָמָה *ʼădâmâh* · שָׂבַע *sâbaʻ* · לֶחֶם *lechem* · רָדַף *râdaph* · רֵיק *rêyq* | 2 | Prov 12:11, Prov 28:19 |
| 29.64 | יְהֹוָה *Yᵉhôvâh* · עָשָׂה *ʻâsâh* · קוּם *qûwm* · מְזִמָּה *mᵉzimmâh* · לֵב *lêb* · אַחֲרִית *ʼachărîyth* · יוֹם *yôwm* · בִּין *bîyn* | 2 | Jer 23:20, Jer 30:24 |
| 29.54 | הַדָּם *haddâm* · עֲבַד *ʻăbad* · בַּיִת *bayith* · נְוָלוּ *nᵉvâlûw* | 2 | Dan 2:5, Dan 3:29 |
| 29.48 | שָׁמַע *shâmaʻ* · יוֹחָנָן *Yôwchânân* · בֵּן *bên* · קָרֵחַ *Qârêach* · כֹּל *kôl* · שַׂר *sar* · חַיִל *chayil* · כֹּל *kôl* | 2 | Jer 41:11, Jer 43:4 |
| 29.43 | יוֹם *yôwm* · חֹשֶׁךְ *chôshek* · אֲפֵלָה *ʼăphêlâh* · יוֹם *yôwm* · עָנָן *ʻânân* · עֲרָפֶל *ʻărâphel* | 2 | Joel 2:2, Zeph 1:15 |
| 29.4 | עוּר *ʻûwr* · נֶבֶל *nebel* · כִּנּוֹר *kinnôwr* · עוּר *ʻûwr* · שַׁחַר *shachar* | 2 | Ps 108:3, Ps 57:9 |
| 29.34 | כִּלְיָה *kilyâh* · לֵב *lêb* · רָאָה *râʼâh* · נְקָמָה *nᵉqâmâh* · גָּלָה *gâlâh* · רִיב *rîyb* | 2 | Jer 11:20, Jer 20:12 |
| 29.33 | בֵּן *bên* · חֲמוֹר *Chămôwr* · אָב *ʼâb* · שְׁכֶם *Shᵉkem* · מֵאָה *mêʼâh* · קְשִׂיטָה *qᵉsîyṭâh* | 2 | Gen 33:19, Josh 24:32 |
| 29.33 | עָלָה *ʻâlâh* · רַחְצָה *rachtsâh* · כֹּל *kôl* · תָּאַם *tâʼam* · שַׁכּוּל *shakkûwl* | 2 | Song 4:2, Song 6:6 |
| 29.23 | תְּכֵלֶת *tᵉkêleth* · אַרְגָּמָן *ʼargâmân* · תּוֹלָע *tôwlâʻ* · שָׁנִי *shânîy* · שֵׁשׁ *shêsh* · שָׁזַר *shâzar* | 12 | Exod 26:31, Exod 26:36, Exod 27:16, Exod 28:15, Exod 28:6, Exod 28:8, Exod 36:35, Exod 36:37, Exod 38:18, Exod 39:2, Exod 39:5, Exod 39:8 |
| 29.19 | חֲלוֹם *chălôwm* · לַיִל *layil* · אֶחָד *ʼechâd* · אִישׁ *ʼîysh* · פִּתְרוֹן *pithrôwn* · חֲלוֹם *chălôwm* | 2 | Gen 40:5, Gen 41:11 |
| 29.11 | עָשָׂה *ʻâsâh* · שְׁנַיִם *shᵉnayim* · מֶלֶךְ *melek* · אֱמֹרִי *ʼĔmôrîy* · עֵבֶר *ʻêber* · יַרְדֵּן *Yardên* · סִיחוֹן *Çîychôwn* | 2 | Josh 2:10, Josh 9:10 |
| 29.09 | הָמָן *Hâmân* · בֵּן *bên* · מְדָתָא *Mᵉdâthâʼ* · אֲגָגִי *ʼĂgâgîy* · צָרַר *tsârar* | 2 | Esth 3:10, Esth 9:24 |
| 29.07 | יוֹחָנָן *Yôwchânân* · בֵּן *bên* · קָרֵחַ *Qârêach* · כֹּל *kôl* · שַׂר *sar* · חַיִל *chayil* · כֹּל *kôl* · עַם *ʻam* | 2 | Jer 42:8, Jer 43:4 |
| 29.05 | תָּוֶךְ *tâvek* · אֶרֶץ *ʼerets* · שָׁמֵם *shâmêm* · עִיר *ʻîyr* · תָּוֶךְ *tâvek* · עִיר *ʻîyr* · חָרַב *chârab* · הָיָה *hâyâh* | 2 | Ezek 29:12, Ezek 30:7 |
| 29.03 | פּוֹטִיפַר *Pôwṭîyphar* · סָרִיס *çârîyç* · פַּרְעֹה *Parʻôh* · שַׂר *sar* · טַבָּח *ṭabbâch* | 2 | Gen 37:36, Gen 39:1 |
| 28.94 | הָיָה *hâyâh* · עֵר *ʻÊr* · בְּכוֹר *bᵉkôwr* · יְהוּדָה *Yᵉhûwdâh* · רַע *raʻ* · עַיִן *ʻayin* · יְהֹוָה *Yᵉhôvâh* · מוּת *mûwth* | 2 | 1Chr 2:3, Gen 38:7 |
| 28.9 | יָשַׁט *yâshaṭ* · מֶלֶךְ *melek* · אֶסְתֵּר *ʼEçtêr* · שַׁרְבִיט *sharbîyṭ* · זָהָב *zâhâb* | 2 | Esth 5:2, Esth 8:4 |
| 28.89 | אֹרֶךְ *ʼôrek* · עֶשְׂרִים *ʻesrîym* · אַמָּה *ʼammâh* · רֹחַב *rôchab* · עֶשֶׂר *ʻeser* · אַמָּה *ʼammâh* | 2 | 2Chr 4:1, Zech 5:2 |
| 28.84 | רַב *rab* · רָבָה *râbâh* · נַחֲלָה *nachălâh* · מְעַט *mᵉʻaṭ* · מָעַט *mâʻaṭ* · נַחֲלָה *nachălâh* | 2 | Num 26:54, Num 33:54 |
| 28.81 | מַסָּה *maççâh* · גָּדוֹל *gâdôwl* · רָאָה *râʼâh* · עַיִן *ʻayin* · אוֹת *ʼôwth* · מוֹפֵת *môwphêth* | 2 | Deut 29:2, Deut 7:19 |
| 28.72 | אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* · מֹשֶׁה *Môsheh* · שָׁכַם *shâkam* · בֹּקֶר *bôqer* · יָצַב *yâtsab* · פָּנִים *pânîym* · פַּרְעֹה *Parʻôh* | 2 | Exod 8:16, Exod 9:13 |
| 28.67 | מָלַךְ *mâlak* · אֶחָד *ʼechâd* · עָשָׂר *ʻâsâr* · שָׁנֶה *shâneh* · מָלַךְ *mâlak* · יְרוּשָׁלַ͏ִם *Yᵉrûwshâlaim* · שֵׁם *shêm* · אֵם *ʼêm* | 3 | 2Kgs 23:36, 2Kgs 24:18, Jer 52:1 |
| 28.63 | יָד *yâd* · חָזָק *châzâq* · זְרוֹעַ *zᵉrôwaʻ* · נָטָה *nâṭâh* · מוֹרָא *môwrâʼ* · גָּדוֹל *gâdôwl* | 2 | Deut 26:8, Deut 4:34 |
| 28.47 | יָפֶה *yâpheh* · רַעְיָה *raʻyâh* · יָפֶה *yâpheh* · עַיִן *ʻayin* · יוֹנָה *yôwnâh* | 2 | Song 1:15, Song 4:1 |
| 28.4 | גּוֹי *gôwy* · יָדָה *yâdâh* · שֵׁם *shêm* · קֹדֶשׁ *qôdesh* · שָׁבַח *shâbach* · תְּהִלָּה *tᵉhillâh* | 2 | 1Chr 16:35, Ps 106:47 |
| 28.36 | שְׁמֹנֶה *shᵉmôneh* · עָשָׂר *ʻâsâr* · אַמָּה *ʼammâh* · קוֹמָה *qôwmâh* · עַמּוּד *ʻammûwd* · אֶחָד *ʼechâd* | 2 | 1Kgs 7:15, 2Kgs 25:17 |
| 28.34 | עֶשְׂרִים *ʻesrîym* · אַמָּה *ʼammâh* · אֹרֶךְ *ʼôrek* · עֶשְׂרִים *ʻesrîym* · אַמָּה *ʼammâh* · רֹחַב *rôchab* | 2 | 1Kgs 6:20, 2Chr 4:1 |
| 28.34 | אֹרֶךְ *ʼôrek* · עֶשְׂרִים *ʻesrîym* · אַמָּה *ʼammâh* · רֹחַב *rôchab* · עֶשְׂרִים *ʻesrîym* · אַמָּה *ʼammâh* | 2 | 1Kgs 6:20, Ezek 41:4 |
| 28.34 | בּוֹא *bôwʼ* · הָלַךְ *hâlak* · רֵישׁ *rêysh* · מַחְסוֹר *machçôwr* · אִישׁ *ʼîysh* · מָגֵן *mâgên* | 2 | Prov 24:34, Prov 6:11 |
| 28.25 | שָׁבַע *shâbaʻ* · אָב *ʼâb* · נָתַן *nâthan* · אֶרֶץ *ʼerets* · זוּב *zûwb* · חָלָב *châlâb* · דְּבַשׁ *dᵉbash* | 3 | Exod 13:5, Jer 11:5, Jer 32:22 |
| 28.04 | אֶרֶץ *ʼerets* · בָּרָק *bârâq* · מָטַר *mâṭar* · עָשָׂה *ʻâsâh* · יָצָא *yâtsâʼ* · רוּחַ *rûwach* · אוֹצָר *ʼôwtsâr* | 3 | Jer 10:13, Jer 51:16, Ps 135:7 |
| 27.92 | פָּקַד *pâqad* · עָוֺן *ʻâvôn* · אָב *ʼâb* · בֵּן *bên* · שִׁלֵּשׁ *shillêsh* · רִבֵּעַ *ribbêaʻ* | 3 | Deut 5:9, Exod 20:5, Num 14:18 |
| 27.89 | סַבָּל *çabbâl* · שְׁמֹנִים *shᵉmônîym* · אֶלֶף *ʼeleph* · חָצַב *châtsab* · הַר *har* | 2 | 1Kgs 5:29, 2Chr 2:17 |
| 27.79 | בָרַךְ *bârak* · יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · יִשְׂרָאֵל *Yisrâʼêl* · עוֹלָם *ʻôwlâm* · עוֹלָם *ʻôwlâm* · אָמַר *ʼâmar* · כֹּל *kôl* · עַם *ʻam* · הָלַל *hâlal* | 2 | 1Chr 16:36, Ps 106:48 |
| 27.74 | רֵעַ *rêaʻ* · בְּלִי *bᵉlîy* · דַּעַת *daʻath* · שָׂנֵא *sânêʼ* · שִׁלְשׁוֹם *shilshôwm* | 2 | Deut 19:4, Deut 4:42 |
| 27.68 | חִתִּי *Chittîy* · אֱמֹרִי *ʼĔmôrîy* · פְּרִזִּי *Pᵉrizzîy* · חִוִּי *Chivvîy* · יְבוּסִי *Yᵉbûwçîy* | 4 | 2Chr 8:7, Exod 3:17, Exod 3:8, Judg 3:5 |
| 27.64 | שֶׁמֶן *shemen* · מִשְׁחָה *mishchâh* · מָשַׁח *mâshach* · מִשְׁכָּן *mishkân* · כֹּל *kôl* · קָדַשׁ *qâdash* | 2 | Exod 40:9, Lev 8:10 |
| 27.54 | רֶגֶל *regel* · רַע *raʻ* · רוּץ *rûwts* · מָהַר *mâhar* · שָׁפַךְ *shâphak* · דָּם *dâm* | 2 | Isa 59:7, Prov 1:16 |
| 27.53 | קְעָרָה *qᵉʻârâh* · כַּף *kaph* · מְנַקִּית *mᵉnaqqîyth* · קָשָׂה *qâsâh* | 2 | Exod 37:16, Num 4:7 |
| 27.48 | שׂוּם *sûwm* · סַד *çad* · רֶגֶל *regel* · שָׁמַר *shâmar* · כֹּל *kôl* · אֹרַח *ʼôrach* | 2 | Job 13:27, Job 33:11 |
| 27.43 | מְעָרָה *mᵉʻârâh* · שָׂדֶה *sâdeh* · מַכְפֵּלָה *Makpêlâh* · פָּנִים *pânîym* · מַמְרֵא *Mamrêʼ* | 2 | Gen 23:19, Gen 49:30 |
| 27.4 | מְדִינָה *mᵉdîynâh* · מְדִינָה *mᵉdîynâh* · כָּתָב *kâthâb* · עַם *ʻam* · עַם *ʻam* · לָשׁוֹן *lâshôwn* | 3 | Esth 1:22, Esth 3:12, Esth 8:9 |
| 27.39 | אָזַר *ʼâzar* · גֶּבֶר *geber* · חָלָץ *châlâts* · שָׁאַל *shâʼal* · יָדַע *yâdaʻ* | 2 | Job 38:3, Job 40:7 |
| 27.37 | זָרַק *zâraq* · בֵּן *bên* · אַהֲרוֹן *ʼAhărôwn* · כֹּהֵן *kôhên* · דָּם *dâm* · מִזְבֵּחַ *mizbêach* · סָבִיב *çâbîyb* | 2 | Lev 1:11, Lev 3:2 |
| 27.37 | מַלְכוּ *malkûw* · רְבִיעַי *rᵉbîyʻay* · רְבִיעַי *rᵉbîyʻay* · הָוָא *hâvâʼ* | 2 | Dan 2:40, Dan 7:23 |
| 27.36 | עֵץ *ʻêts* · אֶרֶז *ʼerez* · אֵזוֹב *ʼêzôwb* · שָׁנִי *shânîy* · תּוֹלָע *tôwlâʻ* | 3 | Lev 14:51, Lev 14:52, Num 19:6 |
| 27.32 | אֱמֹרִי *ʼĔmôrîy* · כְּנַעַנִי *Kᵉnaʻanîy* · פְּרִזִּי *Pᵉrizzîy* · חִוִּי *Chivvîy* · יְבוּסִי *Yᵉbûwçîy* | 4 | Deut 20:17, Deut 7:1, Josh 12:8, Josh 9:1 |
| 27.31 | מִזְבֵּחַ *mizbêach* · עֹלָה *ʻôlâh* · כֹּל *kôl* · כְּלִי *kᵉlîy* · כִּיּוֹר *kîyôwr* · כֵּן *kên* | 2 | Exod 30:28, Exod 31:9 |
| 27.23 | שֶׁקֶל *sheqel* · שֶׁקֶל *sheqel* · קֹדֶשׁ *qôdesh* · עֶשְׂרִים *ʻesrîym* · גֵּרָה *gêrâh* | 2 | Exod 30:13, Num 18:16 |
| 27.23 | טוֹב *ṭôwb* · רוּשׁ *rûwsh* · הָלַךְ *hâlak* · תֹּם *tôm* · עִקֵּשׁ *ʻiqqêsh* | 2 | Prov 19:1, Prov 28:6 |
| 27.17 | חָמֵשׁ *châmêsh* · אַמָּה *ʼammâh* · אֹרֶךְ *ʼôrek* · חָמֵשׁ *châmêsh* · אַמָּה *ʼammâh* · רֹחַב *rôchab* | 3 | 2Chr 6:13, Exod 27:1, Exod 38:1 |
| 27.15 | בֶּגֶד *beged* · קֹדֶשׁ *qôdesh* · אַהֲרוֹן *ʼAhărôwn* · כֹּהֵן *kôhên* · בֶּגֶד *beged* · בֵּן *bên* · כָּהַן *kâhan* | 3 | Exod 31:10, Exod 35:19, Exod 39:41 |
| 27.14 | רֹאשׁ *rôʼsh* · זָנָב *zânâb* · כִּפָּה *kippâh* · אַגְמוֹן *ʼagmôwn* | 2 | Isa 19:15, Isa 9:13 |
| 27.12 | כֹּל *kôl* · רֹאשׁ *rôʼsh* · קׇרְחָה *qorchâh* · כֹּל *kôl* · זָקָן *zâqân* · גָּרַע *gâraʻ* | 2 | Isa 15:2, Jer 48:37 |
| 27.08 | יָשַׁב *yâshab* · עִיר *ʻîyr* · מוּת *mûwth* · חֶרֶב *chereb* · רָעָב *râʻâb* · דֶּבֶר *deber* · יָצָא *yâtsâʼ* | 2 | Jer 21:9, Jer 38:2 |
| 27.01 | הָיָה *hâyâh* · גְּבוּל *gᵉbûwl* · נֶגֶב *negeb* · קָצֶה *qâtseh* · יָם *yâm* · מֶלַח *melach* | 2 | Josh 15:2, Num 34:3 |
| 27.01 | נְבֵלָה *nᵉbêlâh* · מַאֲכָל *maʼăkâl* · עוֹף *ʻôwph* · שָׁמַיִם *shâmayim* · בְּהֵמָה *bᵉhêmâh* · אֶרֶץ *ʼerets* | 3 | Jer 16:4, Jer 19:7, Jer 34:20 |
| 26.96 | בּוֹא *bôwʼ* · שָׁפַט *shâphaṭ* · אֶרֶץ *ʼerets* · שָׁפַט *shâphaṭ* · תֵּבֵל *têbêl* · צֶדֶק *tsedeq* · עַם *ʻam* | 2 | Ps 96:13, Ps 98:9 |
| 26.9 | עוֹלֵל *ʻôwlêl* · רָטָשׁ *râṭâsh* · הָרֶה *hâreh* · בָּקַע *bâqaʻ* | 2 | 2Kgs 8:12, Hos 14:1 |
| 26.81 | מִזְבֵּחַ *mizbêach* · נָתַץ *nâthats* · מַצֵּבָה *matstsêbâh* · שָׁבַר *shâbar* · אֲשֵׁרָה *ʼăshêrâh* | 2 | Deut 7:5, Exod 34:13 |
| 26.7 | אָמַר *ʼâmar* · נָכָה *nâkâh* · שָׁאוּל *Shâʼûwl* · אֶלֶף *ʼeleph* · אֶלֶף *ʼeleph* · דָּוִד *Dâvid* · רְבָבָה *rᵉbâbâh* | 2 | 1Sam 18:7, 1Sam 21:12 |
| 26.7 | כֶּסֶף *keçeph* · זָהָב *zâhâb* · יָכֹל *yâkôl* · נָצַל *nâtsal* · יוֹם *yôwm* · עֶבְרָה *ʻebrâh* · יְהֹוָה *Yᵉhôvâh* | 2 | Ezek 7:19, Zeph 1:18 |
| 26.69 | דֶּרֶךְ *derek* · יָשָׁר *yâshâr* · פָּנִים *pânîym* · אִישׁ *ʼîysh* · אַחֲרִית *ʼachărîyth* · דֶּרֶךְ *derek* · מָוֶת *mâveth* | 2 | Prov 14:12, Prov 16:25 |
| 26.62 | שָׁמַע *shâmaʻ* · כְּנַעַנִי *Kᵉnaʻanîy* · מֶלֶךְ *melek* · עֲרָד *ʻĂrâd* · יָשַׁב *yâshab* · נֶגֶב *negeb* | 2 | Num 21:1, Num 33:40 |
| 26.62 | עֹז *ʻôz* · זִמְרָת *zimrâth* · יָהּ *Yâhh* · הָיָה *hâyâh* · יְשׁוּעָה *yᵉshûwʻâh* | 2 | Exod 15:2, Ps 118:14 |
| 26.57 | שָׁכַב *shâkab* · יְהוֹשָׁפָט *Yᵉhôwshâphâṭ* · אָב *ʼâb* · קָבַר *qâbar* · אָב *ʼâb* · עִיר *ʻîyr* · דָּוִד *Dâvid* | 2 | 1Kgs 22:51, 2Chr 21:1 |
| 26.57 | שֵׂעָר *sêʻâr* · עֵדֶר *ʻêder* · עֵז *ʻêz* · גָּלַשׁ *gâlash* | 2 | Song 4:1, Song 6:5 |
| 26.56 | פָּתַח *pâthach* · אֹזֶן *ʼôzen* · קַשָּׁב *qashshâb* · תְּפִלָּה *tᵉphillâh* · מָקוֹם *mâqôwm* | 2 | 2Chr 6:40, 2Chr 7:15 |
| 26.37 | מוּת *mûwth* · אָב *ʼâb* · בֵּן *bên* · בֵּן *bên* · מוּת *mûwth* · אָב *ʼâb* · אִישׁ *ʼîysh* · חֵטְא *chêṭᵉʼ* · מוּת *mûwth* | 3 | 2Chr 25:4, 2Kgs 14:6, Deut 24:16 |
| 26.31 | קָנָה *qânâh* · עֵץ *ʻêts* · אֶבֶן *ʼeben* · מַחְצֵב *machtsêb* · חָזַק *châzaq* | 2 | 2Kgs 12:13, 2Kgs 22:6 |
| 26.3 | פָּנָה *pânâh* · נָסַע *nâçaʻ* · מִדְבָּר *midbâr* · דֶּרֶךְ *derek* · יָם *yâm* · סוּף *çûwph* | 3 | Deut 1:40, Deut 2:1, Num 14:25 |
| 26.29 | לָחַם *lâcham* · בֵּן *bên* · עַמּוֹן *ʻAmmôwn* · הָיָה *hâyâh* · רֹאשׁ *rôʼsh* · כֹּל *kôl* · יָשַׁב *yâshab* · גִּלְעָד *Gilʻâd* | 2 | Judg 10:18, Judg 11:8 |
| 26.29 | הָיָה *hâyâh* · לֵבָב *lêbâb* · שָׁלֵם *shâlêm* · יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · לֵבָב *lêbâb* · דָּוִד *Dâvid* · אָב *ʼâb* | 2 | 1Kgs 11:4, 1Kgs 15:3 |
| 26.23 | שָׁסַס *shâçaç* · בַּיִת *bayith* · אִשָּׁה *ʼishshâh* · שָׁגַל *shâgal* · שָׁכַב *shâkab* | 2 | Isa 13:16, Zech 14:2 |
| 26.19 | בְּנָיָה *Bᵉnâyâh* · בֵּן *bên* · יְהוֹיָדָע *Yᵉhôwyâdâʻ* · כְּרֵתִי *Kᵉrêthîy* · פְּלֵתִי *Pᵉlêthîy* | 4 | 1Chr 18:17, 1Kgs 1:38, 1Kgs 1:44, 2Sam 8:18 |
| 26.18 | עֶשְׂרִים *ʻesrîym* · תֵּשַׁע *têshaʻ* · שָׁנֶה *shâneh* · מָלַךְ *mâlak* · יְרוּשָׁלַ͏ִם *Yᵉrûwshâlaim* · שֵׁם *shêm* · אֵם *ʼêm* | 4 | 2Chr 25:1, 2Chr 29:1, 2Kgs 14:2, 2Kgs 18:2 |
| 26.18 | אֵל *ʼêl* · יָצָא *yâtsâʼ* · מִצְרַיִם *Mitsrayim* · תּוֹעָפָה *tôwʻâphâh* · רְאֵם *rᵉʼêm* | 2 | Num 23:22, Num 24:8 |
| 26.15 | חָרַם *châram* · כֹּל *kôl* · עִיר *ʻîyr* · מַת *math* · אִשָּׁה *ʼishshâh* · טַף *ṭaph* | 2 | Deut 2:34, Deut 3:6 |
| 26.01 | עָשָׂה *ʻâsâh* · אֲשֵׁרָה *ʼăshêrâh* · שָׁחָה *shâchâh* · כֹּל *kôl* · צָבָא *tsâbâʼ* · שָׁמַיִם *shâmayim* · עָבַד *ʻâbad* | 2 | 2Chr 33:3, 2Kgs 17:16 |
| 25.97 | רְאוּבֵנִי *Rᵉʼûwbênîy* · גָּדִי *Gâdîy* · חֵצִי *chêtsîy* · שֵׁבֶט *shêbeṭ* · מְנַשֶּׁה *Mᵉnashsheh* | 4 | 1Chr 12:38, 1Chr 5:26, Josh 1:12, Josh 12:6 |
| 25.91 | יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · בָּשַׁל *bâshal* · גְּדִי *gᵉdîy* · חָלָב *châlâb* · אֵם *ʼêm* | 3 | Deut 14:21, Exod 23:19, Exod 34:26 |
| 25.9 | רִאשׁוֹן *riʼshôwn* · אַחֲרוֹן *ʼachărôwn* · כָּתַב *kâthab* · סֵפֶר *çêpher* · מֶלֶךְ *melek* · יְהוּדָה *Yᵉhûwdâh* · יִשְׂרָאֵל *Yisrâʼêl* | 3 | 2Chr 16:11, 2Chr 25:26, 2Chr 28:26 |
| 25.87 | שָׁלוֹשׁ *shâlôwsh* · פַּעַם *paʻam* · שָׁנֶה *shâneh* · רָאָה *râʼâh* · כֹּל *kôl* · זָכוּר *zâkûwr* · פָּנִים *pânîym* | 3 | Deut 16:16, Exod 23:17, Exod 34:23 |
| 25.86 | נָשַׁל *nâshal* · נַעַל *naʻal* · רֶגֶל *regel* · מָקוֹם *mâqôwm* · עָמַד *ʻâmad* | 2 | Exod 3:5, Josh 5:15 |
| 25.82 | מָצָא *mâtsâʼ* · חֵן *chên* · עַיִן *ʻayin* · מֶלֶךְ *melek* · מֶלֶךְ *melek* · טוֹב *ṭôwb* · נָתַן *nâthan* | 2 | Esth 5:8, Esth 7:3 |
| 25.82 | לְבָנוֹן *Lᵉbânôwn* · נָהָר *nâhâr* · גָּדוֹל *gâdôwl* · נָהָר *nâhâr* · פְּרָת *Pᵉrâth* | 2 | Deut 1:7, Josh 1:4 |
| 25.82 | אִשָּׁה *ʼishshâh* · זוּר *zûwr* · נׇכְרִי *nokrîy* · אֵמֶר *ʼêmer* · חָלַק *châlaq* | 2 | Prov 2:16, Prov 7:5 |
| 25.77 | אָסַף *ʼâçaph* · קָבַר *qâbar* · דֹּמֶן *dômen* · פָּנִים *pânîym* · אֲדָמָה *ʼădâmâh* · הָיָה *hâyâh* | 2 | Jer 25:33, Jer 8:2 |
| 25.72 | עָשָׂה *ʻâsâh* · רַע *raʻ* · עַיִן *ʻayin* · יְהֹוָה *Yᵉhôvâh* · יָלַךְ *yâlak* · דֶּרֶךְ *derek* · יָרׇבְעָם *Yârobʻâm* · חַטָּאָה *chaṭṭâʼâh* | 2 | 1Kgs 15:34, 1Kgs 16:19 |
| 25.72 | גּוֹי *gôwy* · מַמְלָכָה *mamlâkâh* · נָתַשׁ *nâthash* · נָתַץ *nâthats* · אָבַד *ʼâbad* | 2 | Jer 1:10, Jer 18:7 |
| 25.68 | עָנָה *ʻânâh* · יְהֹוָה *Yᵉhôvâh* · אִיּוֹב *ʼÎyôwb* · סַעַר *çaʻar* · סַעַר *çaʻar* · אָמַר *ʼâmar* | 2 | Job 38:1, Job 40:6 |
| 25.67 | קֶרֶב *qereb* · כָּרָע *kârâʻ* · רָחַץ *râchats* · מַיִם *mayim* · קָטַר *qâṭar* | 2 | Lev 1:9, Lev 8:21 |
| 25.65 | אֹיֵב *ʼôyêb* · אֶרֶץ *ʼerets* · יָדַע *yâdaʻ* · אֵשׁ *ʼêsh* · קָדַח *qâdach* · אַף *ʼaph* | 2 | Jer 15:14, Jer 17:4 |
| 25.61 | דָּבָר *dâbâr* · דָבַר *dâbar* · יְהֹוָה *Yᵉhôvâh* · הַר *har* · תָּוֶךְ *tâvek* · אֵשׁ *ʼêsh* · יוֹם *yôwm* · קָהָל *qâhâl* | 2 | Deut 10:4, Deut 9:10 |
| 25.59 | מָקוֹר *mâqôwr* · חַי *chay* · סוּר *çûwr* · מוֹקֵשׁ *môwqêsh* · מָוֶת *mâveth* | 2 | Prov 13:14, Prov 14:27 |
| 25.56 | הָיָה *hâyâh* · אָלָה *ʼâlâh* · שַׁמָּה *shammâh* · קְלָלָה *qᵉlâlâh* · חֶרְפָּה *cherpâh* | 2 | Jer 42:18, Jer 44:12 |
| 25.53 | שָׁמַע *shâmaʻ* · דִּבָּה *dibbâh* · רַב *rab* · מָגוֹר *mâgôwr* · סָבִיב *çâbîyb* | 2 | Jer 20:10, Ps 31:14 |
| 25.48 | נָתַן *nâthan* · זְוָעָה *zᵉvâʻâh* · זַעֲוָה *zaʻăvâh* · כֹּל *kôl* · מַמְלָכָה *mamlâkâh* · אֶרֶץ *ʼerets* | 3 | Jer 15:4, Jer 29:18, Jer 34:17 |
| 25.45 | נָקָה *nâqâh* · נָקָה *nâqâh* · פָּקַד *pâqad* · עָוֺן *ʻâvôn* · אָב *ʼâb* · בֵּן *bên* | 2 | Exod 34:7, Num 14:18 |
| 25.45 | חִזָּיוֹן *chizzâyôwn* · לַיִל *layil* · נָפַל *nâphal* · תַּרְדֵּמָה *tardêmâh* · אִישׁ *ʼîysh* | 2 | Job 33:15, Job 4:13 |
| 25.44 | רֹאשׁ *rôʼsh* · יוֹסֵף *Yôwçêph* · קׇדְקֹד *qodqôd* · נָזִיר *nâzîyr* · אָח *ʼâch* | 2 | Deut 33:16, Gen 49:26 |
| 25.21 | חֹזֶה *chôzeh* · שָׁוְא *shâvᵉʼ* · קָסַם *qâçam* · כָּזָב *kâzâb* | 2 | Ezek 13:9, Ezek 22:28 |
| 25.2 | לָקַח *lâqach* · בֶּגֶד *beged* · עָרַב *ʻârab* · זוּר *zûwr* · נׇכְרִי *nokrîy* | 2 | Prov 20:16, Prov 27:13 |
| 25.19 | אָמַר *ʼâmar* · אָב *ʼâb* · שׁוּב *shûwb* · שָׁבַר *shâbar* · מְעַט *mᵉʻaṭ* · אֹכֶל *ʼôkel* | 2 | Gen 43:2, Gen 44:25 |
| 25.19 | עִשָּׂרוֹן *ʻissârôwn* · סֹלֶת *çôleth* · מִנְחָה *minchâh* · בָּלַל *bâlal* · שֶׁמֶן *shemen* | 4 | Lev 14:10, Num 28:12, Num 28:13, Num 28:9 |
| 25.19 | עָנָן *ʻânân* · בֹּקֶר *bôqer* · טַל *ṭal* · שָׁכַם *shâkam* · הָלַךְ *hâlak* | 2 | Hos 13:3, Hos 6:4 |
| 25.18 | יָלַךְ *yâlak* · דֶּרֶךְ *derek* · שָׁלוֹשׁ *shâlôwsh* · יוֹם *yôwm* · מִדְבָּר *midbâr* · זָבַח *zâbach* · יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* | 2 | Exod 3:18, Exod 5:3 |
| 25.15 | אֶרֶץ *ʼerets* · כְּנַעַנִי *Kᵉnaʻanîy* · חִתִּי *Chittîy* · אֱמֹרִי *ʼĔmôrîy* · פְּרִזִּי *Pᵉrizzîy* | 2 | Exod 3:17, Neh 9:8 |
| 25.13 | כֹּהֵן *kôhên* · חָצַר *châtsar* · חָצַר *châtsar* · חֲצֹצְרָה *chătsôtsᵉrâh* | 2 | 1Chr 15:24, 2Chr 13:14 |
| 25.04 | שׂוּם *sûwm* · טְעֵם *ṭᵉʻêm* · כֹּל *kôl* · אֱנָשׁ *ʼĕnâsh* | 2 | Dan 3:10, Ezra 6:11 |
| 25.02 | גֶּשֶׁם *geshem* · שָׁטַף *shâṭaph* · אֶבֶן *ʼeben* · אֶלְגָּבִישׁ *ʼelgâbîysh* | 2 | Ezek 13:11, Ezek 38:22 |
| 24.88 | קָרָא *qârâʼ* · מַיִם *mayim* · יָם *yâm* · שָׁפַךְ *shâphak* · פָּנִים *pânîym* · אֶרֶץ *ʼerets* · יְהֹוָה *Yᵉhôvâh* · שֵׁם *shêm* | 2 | Amos 5:8, Amos 9:6 |
| 24.85 | צְבִי *tsᵉbîy* · עֹפֶר *ʻôpher* · אַיָּל *ʼayâl* · הַר *har* | 2 | Song 2:17, Song 8:14 |
| 24.84 | הַר *har* · סִינַי *Çîynay* · שְׁנַיִם *shᵉnayim* · לוּחַ *lûwach* · עֵדוּת *ʻêdûwth* | 2 | Exod 31:18, Exod 34:29 |
| 24.71 | עֲרוֹעֵר *ʻĂrôwʻêr* · שָׂפָה *sâphâh* · נַחַל *nachal* · אַרְנוֹן *ʼArnôwn* · עִיר *ʻîyr* | 3 | Deut 2:36, Josh 13:16, Josh 13:9 |

## Hebrew Bible: doublet chapter pairs

Chapter pairs sharing at least 4 long phrases: verbatim parallel passages, kept apart from the echoes.

- 1Chr.1 = Gen.10 (21)
- 1Chr.1 = Gen.36 (24)
- 1Chr.10 = 1Sam.31 (16)
- 1Chr.11 = 2Sam.23 (25)
- 1Chr.11 = 2Sam.5 (10)
- 1Chr.13 = 2Sam.6 (10)
- 1Chr.14 = 2Sam.5 (12)
- 1Chr.15 = 2Sam.6 (6)
- 1Chr.16 = 2Sam.6 (5)
- 1Chr.16 = Ps.105 (14)
- 1Chr.16 = Ps.96 (13)
- 1Chr.17 = 2Sam.7 (29)
- 1Chr.18 = 2Sam.8 (32)
- 1Chr.19 = 2Sam.10 (28)
- 1Chr.20 = 2Sam.12 (4)
- 1Chr.20 = 2Sam.21 (8)
- 1Chr.21 = 2Sam.24 (13)
- 1Chr.23 = 1Chr.24 (4)
- 1Chr.29 = 1Kgs.2 (4)
- 1Chr.3 = 2Sam.3 (4)
- 1Chr.5 = Exod.6 (4)
- 1Chr.6 = Josh.21 (20)
- 1Chr.8 = 1Chr.9 (13)
- 1Chr.9 = Neh.11 (12)
- 1Kgs.10 = 2Chr.1 (12)
- 1Kgs.10 = 2Chr.9 (53)
- 1Kgs.12 = 2Chr.10 (38)
- 1Kgs.12 = 2Chr.11 (6)
- 1Kgs.14 = 1Kgs.15 (7)
- 1Kgs.14 = 2Chr.12 (27)
- 1Kgs.15 = 1Kgs.22 (5)
- 1Kgs.15 = 2Chr.13 (5)
- 1Kgs.15 = 2Chr.16 (13)
- 1Kgs.16 = 2Kgs.13 (4)
- 1Kgs.21 = 2Kgs.9 (4)
- 1Kgs.22 = 2Chr.18 (83)
- 1Kgs.22 = 2Chr.20 (10)
- 1Kgs.22 = 2Kgs.3 (5)
- 1Kgs.7 = 2Chr.4 (44)
- 1Kgs.7 = Jer.52 (6)
- 1Kgs.8 = 2Chr.5 (21)
- 1Kgs.8 = 2Chr.6 (122)
- 1Kgs.8 = 2Chr.7 (11)
- 1Kgs.8 = Neh.1 (4)
- 1Kgs.9 = 2Chr.7 (13)
- 1Kgs.9 = 2Chr.8 (8)
- 1Sam.24 = 1Sam.26 (4)
- 2Chr.1 = 2Chr.9 (4)
- 2Chr.21 = 2Kgs.8 (15)
- 2Chr.22 = 2Kgs.11 (5)
- 2Chr.22 = 2Kgs.8 (16)
- 2Chr.23 = 2Kgs.11 (25)
- 2Chr.25 = 2Kgs.14 (35)
- 2Chr.26 = 2Kgs.14 (4)
- 2Chr.26 = 2Kgs.15 (6)
- 2Chr.27 = 2Kgs.15 (8)
- 2Chr.28 = 2Kgs.16 (10)
- 2Chr.30 = 2Chr.35 (5)
- 2Chr.33 = 2Kgs.21 (26)
- 2Chr.34 = 2Kgs.22 (38)
- 2Chr.34 = 2Kgs.23 (6)
- 2Chr.36 = 2Kgs.23 (5)
- 2Chr.36 = 2Kgs.24 (5)
- 2Chr.36 = Ezra.1 (22)
- 2Kgs.13 = 2Kgs.14 (9)
- 2Kgs.14 = 2Kgs.18 (7)
- 2Kgs.16 = Isa.7 (4)
- 2Kgs.18 = Isa.36 (71)
- 2Kgs.19 = Isa.37 (107)
- 2Kgs.20 = Isa.38 (19)
- 2Kgs.20 = Isa.39 (21)
- 2Kgs.23 = 2Kgs.24 (6)
- 2Kgs.24 = Jer.52 (14)
- 2Kgs.25 = Jer.39 (5)
- 2Kgs.25 = Jer.40 (6)
- 2Kgs.25 = Jer.52 (70)
- 2Kgs.8 = 2Kgs.9 (6)
- 2Sam.22 = Ps.18 (33)
- Dan.4 = Dan.5 (6)
- Dan.5 = Dan.6 (4)
- Deut.1 = Deut.30 (4)
- Deut.1 = Deut.6 (4)
- Deut.11 = Deut.28 (6)
- Deut.11 = Deut.30 (7)
- Deut.11 = Deut.6 (5)
- Deut.11 = Josh.1 (4)
- Deut.11 = Josh.22 (4)
- Deut.12 = Deut.14 (5)
- Deut.12 = Deut.16 (6)
- Deut.13 = Deut.28 (4)
- Deut.14 = Deut.31 (6)
- Deut.14 = Deut.7 (4)
- Deut.14 = Lev.11 (10)
- Deut.15 = Deut.24 (4)
- Deut.15 = Deut.28 (8)
- Deut.19 = Deut.30 (4)
- Deut.28 = Deut.30 (7)
- Deut.28 = Deut.31 (4)
- Deut.28 = Deut.7 (4)
- Deut.3 = Josh.12 (4)
- Deut.3 = Num.21 (10)
- Deut.30 = Deut.6 (4)
- Deut.34 = Exod.33 (4)
- Deut.5 = Exod.20 (18)
- Eccl.1 = Eccl.2 (4)
- Esth.1 = Esth.8 (4)
- Esth.2 = Esth.6 (4)
- Esth.3 = Esth.8 (9)
- Esth.5 = Esth.6 (4)
- Esth.8 = Esth.9 (4)
- Exod.10 = Exod.7 (5)
- Exod.10 = Exod.9 (9)
- Exod.12 = Num.28 (7)
- Exod.12 = Num.9 (4)
- Exod.16 = Num.14 (4)
- Exod.23 = Exod.34 (10)
- Exod.25 = Exod.35 (5)
- Exod.25 = Exod.37 (56)
- Exod.26 = Exod.36 (69)
- Exod.27 = Exod.38 (13)
- Exod.27 = Lev.24 (4)
- Exod.28 = Exod.39 (33)
- Exod.29 = Exod.40 (4)
- Exod.29 = Lev.7 (8)
- Exod.29 = Lev.8 (17)
- Exod.3 = Exod.4 (4)
- Exod.30 = Exod.37 (6)
- Exod.30 = Exod.38 (4)
- Exod.30 = Exod.40 (4)
- Exod.31 = Exod.35 (11)
- Exod.35 = Exod.38 (6)
- Exod.35 = Exod.39 (8)
- Exod.39 = Num.1 (5)
- Exod.39 = Num.2 (4)
- Exod.39 = Num.9 (4)
- Exod.7 = Exod.8 (6)
- Exod.7 = Exod.9 (6)
- Ezek.1 = Ezek.10 (4)
- Ezek.18 = Ezek.33 (9)
- Ezek.20 = Ezek.34 (4)
- Ezek.20 = Ezek.36 (5)
- Ezek.3 = Ezek.33 (6)
- Ezek.31 = Ezek.32 (4)
- Ezek.36 = Ezek.6 (9)
- Ezek.45 = Ezek.46 (4)
- Ezek.45 = Ezek.48 (6)
- Ezra.2 = Neh.7 (69)
- Ezra.5 = Ezra.6 (8)
- Gen.1 = Gen.9 (4)
- Gen.11 = Gen.5 (4)
- Gen.6 = Gen.7 (5)
- Gen.7 = Gen.8 (4)
- Hag.1 = Hag.2 (5)
- Isa.2 = Mic.4 (14)
- Isa.35 = Isa.51 (6)
- Jer.10 = Jer.51 (9)
- Jer.16 = Jer.23 (9)
- Jer.19 = Jer.49 (4)
- Jer.19 = Jer.7 (5)
- Jer.25 = Jer.35 (4)
- Jer.27 = Jer.28 (4)
- Jer.27 = Jer.32 (4)
- Jer.30 = Jer.46 (6)
- Jer.32 = Jer.34 (5)
- Jer.35 = Jer.44 (6)
- Jer.39 = Jer.52 (10)
- Jer.49 = Jer.50 (9)
- Jer.49 = Obad.1 (4)
- Jer.50 = Jer.6 (6)
- Job.1 = Job.2 (13)
- Josh.10 = Josh.11 (4)
- Josh.15 = Josh.18 (4)
- Josh.15 = Judg.1 (8)
- Josh.17 = Judg.1 (4)
- Josh.17 = Num.27 (6)
- Josh.24 = Judg.2 (5)
- Josh.3 = Josh.4 (8)
- Lev.14 = Lev.15 (4)
- Lev.17 = Lev.22 (5)
- Lev.23 = Lev.25 (4)
- Lev.23 = Num.28 (9)
- Lev.23 = Num.29 (6)
- Lev.4 = Lev.5 (6)
- Lev.8 = Lev.9 (4)
- Num.1 = Num.10 (8)
- Num.1 = Num.2 (28)
- Num.1 = Num.26 (4)
- Num.1 = Num.7 (10)
- Num.1 = Num.9 (4)
- Num.10 = Num.2 (16)
- Num.10 = Num.7 (17)
- Num.13 = Num.14 (4)
- Num.16 = Num.27 (4)
- Num.2 = Num.26 (8)
- Num.2 = Num.7 (26)
- Num.28 = Num.29 (16)
- Num.3 = Num.4 (7)
- Num.3 = Num.8 (7)
- Ps.108 = Ps.60 (7)
- Ps.115 = Ps.135 (4)
- Ps.14 = Ps.53 (6)
- Ps.40 = Ps.70 (4)

## Hebrew Bible: most frequent stock formulas

| Phrase | Count |
|---|---|
| אָמַר *ʼâmar* · אֲדֹנָי *ʼĂdônây* · יְהֹוִה *Yᵉhôvih* | 152 |
| יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · יִשְׂרָאֵל *Yisrâʼêl* | 121 |
| הָיָה *hâyâh* · דָּבָר *dâbâr* · יְהֹוָה *Yᵉhôvâh* | 113 |
| אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* · צָבָא *tsâbâʼ* | 106 |
| דָבַר *dâbar* · יְהֹוָה *Yᵉhôvâh* · מֹשֶׁה *Môsheh* | 100 |
| נְאֻם *nᵉʼum* · אֲדֹנָי *ʼĂdônây* · יְהֹוִה *Yᵉhôvih* | 92 |
| אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* | 86 |
| יְהֹוָה *Yᵉhôvâh* · מֹשֶׁה *Môsheh* · אָמַר *ʼâmar* | 82 |
| דָבַר *dâbar* · יְהֹוָה *Yᵉhôvâh* · מֹשֶׁה *Môsheh* · אָמַר *ʼâmar* | 70 |
| דָּבָר *dâbâr* · יְהֹוָה *Yᵉhôvâh* · אָמַר *ʼâmar* | 70 |
| אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* · מֹשֶׁה *Môsheh* | 68 |
| אָמַר *ʼâmar* · אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* | 64 |
| הָיָה *hâyâh* · דָּבָר *dâbâr* · יְהֹוָה *Yᵉhôvâh* · אָמַר *ʼâmar* | 61 |
| צָוָה *tsâvâh* · יְהֹוָה *Yᵉhôvâh* · מֹשֶׁה *Môsheh* | 58 |
| רַע *raʻ* · עַיִן *ʻayin* · יְהֹוָה *Yᵉhôvâh* | 55 |
| עָשָׂה *ʻâsâh* · רַע *raʻ* · עַיִן *ʻayin* | 52 |
| בֵּן *bên* · יִשְׂרָאֵל *Yisrâʼêl* · אָמַר *ʼâmar* | 51 |
| יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · כֹּל *kôl* | 47 |
| נְבוּכַדְנֶאצַּר *Nᵉbûwkadneʼtstsar* · מֶלֶךְ *melek* · בָּבֶל *Bâbel* | 46 |
| עָשָׂה *ʻâsâh* · רַע *raʻ* · עַיִן *ʻayin* · יְהֹוָה *Yᵉhôvâh* | 46 |
| פֶּתַח *pethach* · אֹהֶל *ʼôhel* · מוֹעֵד *môwʻêd* | 45 |
| יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · נָתַן *nâthan* | 45 |
| יָצָא *yâtsâʼ* · אֶרֶץ *ʼerets* · מִצְרַיִם *Mitsrayim* | 42 |
| צָבָא *tsâbâʼ* · אֱלֹהִים *ʼĕlôhîym* · יִשְׂרָאֵל *Yisrâʼêl* | 42 |
| יְהֹוָה *Yᵉhôvâh* · צָבָא *tsâbâʼ* · אֱלֹהִים *ʼĕlôhîym* | 42 |
| אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · יִשְׂרָאֵל *Yisrâʼêl* | 39 |
| פָּנִים *pânîym* · יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* | 39 |
| יְהֹוָה *Yᵉhôvâh* · צָבָא *tsâbâʼ* · אֱלֹהִים *ʼĕlôhîym* · יִשְׂרָאֵל *Yisrâʼêl* | 38 |
| יְהֹוָה *Yᵉhôvâh* · אֱלֹהִים *ʼĕlôhîym* · אָב *ʼâb* | 38 |
| כָּתַב *kâthab* · סֵפֶר *çêpher* · דָּבָר *dâbâr* | 37 |
| כָּתַב *kâthab* · סֵפֶר *çêpher* · דָּבָר *dâbâr* · יוֹם *yôwm* | 36 |
| כֶּבֶשׂ *kebes* · בֵּן *bên* · שָׁנֶה *shâneh* | 36 |
| שָׁמַע *shâmaʻ* · קוֹל *qôwl* · יְהֹוָה *Yᵉhôvâh* | 36 |
| שָׁנֶה *shâneh* · מָלַךְ *mâlak* · יְרוּשָׁלַ͏ִם *Yᵉrûwshâlaim* | 35 |
| דָּבָר *dâbâr* · יוֹם *yôwm* · מֶלֶךְ *melek* | 35 |
| כָּתַב *kâthab* · סֵפֶר *çêpher* · דָּבָר *dâbâr* · יוֹם *yôwm* · מֶלֶךְ *melek* | 34 |
| אָמַר *ʼâmar* · יְהֹוָה *Yᵉhôvâh* · צָבָא *tsâbâʼ* · אֱלֹהִים *ʼĕlôhîym* · יִשְׂרָאֵל *Yisrâʼêl* | 34 |
| שָׁמַע *shâmaʻ* · דָּבָר *dâbâr* · יְהֹוָה *Yᵉhôvâh* | 34 |
| מָצָא *mâtsâʼ* · חֵן *chên* · עַיִן *ʻayin* | 33 |
| אָרוֹן *ʼârôwn* · בְּרִית *bᵉrîyth* · יְהֹוָה *Yᵉhôvâh* | 32 |

## Hebrew Bible: loanword candidates

| Marker | Lemma | Count | Gloss | First place |
|---|---|---|---|---|
| egyptian | אֵיפָה *ʼêyphâh* (H374) | 40 | an ephah or measure for grain; hence, a measure in general | Exod 16:36 |
| egyptian | סוּף *çûwph* (H5488) | 28 | a reed, especially the papyrus | Exod 2:3 |
| egyptian | הִין *hîyn* (H1969) | 22 | a hin or liquid measure | Exod 29:40 |
| egyptian | אָחוּ *ʼâchûw* (H260) | 3 | a bulrush or any marshy grass (particularly that along the Nile) | Gen 41:2 |
| egyptian | עֲנָמִים *ʻĂnâmîym* (H6047) | 2 | Anamim, a son of Mizraim and his descendants, with their country | Gen 10:13 |
| egyptian | אַבְרֵךְ *ʼabrêk* (H86) | 1 | kneel | Gen 41:43 |
| egyptian | בְּהֵמוֹת *bᵉhêmôwth* (H930) | 1 | a water-ox, i.e. the hippopotamus or Nile-horse | Job 40:15 |
| egyptian | אַפִּרְיוֹן *ʼappiryôwn* (H668) | 1 | a palanquin | Song 3:9 |
| foreign | תְּאֵן *tᵉʼên* (H8384) | 39 | the fig (tree or fruit) | Gen 3:7 |
| foreign | אַרְגָּמָן *ʼargâmân* (H713) | 38 | purple (the color or the dyed stuff) | Exod 25:4 |
| foreign | תֵּבָה *têbâh* (H8392) | 28 | a box | Gen 6:14 |
| foreign | פֶּחָה *pechâh* (H6346) | 28 | a prefect (of a city or small district) | 1Kgs 10:15 |
| foreign | דָּת *dâth* (H1881) | 22 | a royal edict or statute | Deut 33:2 |
| foreign | בִּירָה *bîyrâh* (H1002) | 16 | a castle or palace | 1Chr 29:1 |
| foreign | רַב־סָרִיס *Rab-Çârîyç* (H7249) | 6 | Rab-Saris, a Babylonian official | 2Kgs 18:17 |
| foreign | הַמְנִיךְ *hamnîyk* (H2002, Aram.) | 6 | a necklace | Dan 5:7 |
| foreign | תִּרְשָׁתָא *Tirshâthâʼ* (H8660) | 5 | Tirshatha, the title of a Persian deputy or governor | Ezra 2:63 |
| foreign | סָרֵךְ *çârêk* (H5632, Aram.) | 5 | an emir | Dan 6:3 |
| foreign | פִּטְדָה *piṭdâh* (H6357) | 4 | a gem, probably the topaz | Exod 28:17 |
| foreign | אֲהָלִים *ʼăhâlîym* (H174) | 4 | aloe wood (i.e. sticks) | Num 24:6 |
| foreign | פַּרְשֶׁגֶן *parshegen* (H6572) | 4 | a transcript | Ezra 7:11 |
| foreign | רַב־מָג *Rab-Mâg* (H7248) | 4 | Rab-Mag, a Babylonian official | Jer 39:3 |
| foreign | פַּרְבָּר *Parbâr* (H6503) | 3 | Parbar or Parvar, a quarter of Jerusalem | 2Kgs 23:11 |
| foreign | אֲפַרְסְכַי *ʼĂpharçᵉkay* (H671, Aram.) | 3 | an Apharsekite or Apharsathkite, an unknown Assyrian tribe | Ezra 4:9 |
| foreign | פַּרְדֵּס *pardêç* (H6508) | 3 | a park | Neh 2:8 |
| foreign | נֵרְדְּ *nêrd* (H5373) | 3 | nard, an aromatic | Song 1:12 |
| foreign | נַפְתֻּחִים *Naphtuchîym* (H5320) | 2 | Naphtuchim, an Egyptian tribe | Gen 10:13 |
| foreign | שֶׁנְהַבִּים *shenhabbîym* (H8143) | 2 | probably, tooth of elephants, i.e. ivory tusk | 1Kgs 10:22 |
| foreign | קוֹף *qôwph* (H6971) | 2 | a monkey | 1Kgs 10:22 |
| foreign | תֻּכִּי *tukkîy* (H8500) | 2 | probably of foreign derivation; some imported creature, probably a peacock | 1Kgs 10:22 |
| foreign | תַּרְתָּן *Tartân* (H8661) | 2 | Tartan, an Assyrian | 2Kgs 18:17 |
| foreign | הָבַר *hâbar* (H1895) | 2 | to be a horoscopist | Isa 47:13 |
| foreign | טִפְסַר *ṭiphçar* (H2951) | 2 | a military governor | Jer 51:27 |
| foreign | גִּזְבָּר *gizbâr* (H1489) | 1 | treasurer | Ezra 1:8 |
| foreign | טַרְפְּלַי *Ṭarpᵉlay* (H2967, Aram.) | 1 | a Tarpelite (collectively) or inhabitants of Tarpel, a place in Assyria | Ezra 4:9 |
| foreign | אֲפָרְסַי *ʼĂphârᵉçay* (H670, Aram.) | 1 | an Apherasite or inhabitant of an unknown region of Assyria | Ezra 4:9 |
| foreign | שׁוּשַׁנְכִי *Shûwshankîy* (H7801, Aram.) | 1 | a Shushankite (collectively) or inhabitants of some unknown place in Assyrian | Ezra 4:9 |
| foreign | כַּרְפַּס *karpaç* (H3768) | 1 | byssus or fine vegetable wool | Esth 1:6 |
| foreign | רַמָּךְ *rammâk* (H7424) | 1 | a brood mare | Esth 8:10 |
| foreign | אַפֶּדֶן *ʼappeden* (H643) | 1 | a pavilion or palace-tent | Dan 11:45 |
| greek | קִיתָרֹס *qîythârôç* (H7030, Aram.) | 8 | a lyre | Dan 3:5 |
| greek | פְּסַנְטֵרִין *pᵉçanṭêrîyn* (H6460, Aram.) | 4 | psalterion; a lyre | Dan 3:5 |
| greek | סוּמְפּוֹנְיָה *çûwmᵉpôwnᵉyâh* (H5481, Aram.) | 4 | a bagpipe (with a double pipe) | Dan 3:5 |
| greek | כְּרַז *kᵉraz* (H3745, Aram.) | 1 | to proclaim | Dan 5:29 |
| of uncertain derivation | כְּרוּב *kᵉrûwb* (H3742) | 91 | a cherub or imaginary figure | Gen 3:24 |
| of uncertain derivation | אֱדַיִן *ʼĕdayin* (H116, Aram.) | 57 | then (of time) | Ezra 4:9 |
| of uncertain derivation | שָׁנִי *shânîy* (H8144) | 42 | crimson, properly, the insect or its color, also stuff dyed with it | Gen 38:28 |
| of uncertain derivation | דַּי *day* (H1767) | 39 | enough (as noun or adverb), used chiefly with preposition in phrases | Exod 36:5 |
| of uncertain derivation | פִּילֶגֶשׁ *pîylegesh* (H6370) | 37 | a concubine; also (masculine) a paramour | Gen 22:24 |
| of uncertain derivation | חִטָּה *chiṭṭâh* (H2406) | 30 | wheat, whether the grain or the plant | Gen 30:14 |
| of uncertain derivation | בְּרוֹשׁ *bᵉrôwsh* (H1265) | 20 | a cypress (?) tree; hence, a lance or a musical instrument (as made of that wood) | 2Sam 6:5 |
| of uncertain derivation | דָּרוֹם *dârôwm* (H1864) | 17 | the south; poet. the south wind | Deut 33:23 |
| of uncertain derivation | אַבְנֵט *ʼabnêṭ* (H73) | 9 | a belt | Exod 28:4 |
| of uncertain derivation | גִּרְגָּשִׁי *Girgâshîy* (H1622) | 7 | a Girgashite, one of the native tribes of Canaan | Gen 10:16 |
| of uncertain derivation | שִׁקְמָה *shiqmâh* (H8256) | 7 | a sycamore (usually the tree) | 1Kgs 10:27 |
| of uncertain derivation | עַקְרָב *ʻaqrâb* (H6137) | 6 | a scorpion; figuratively, a scourge or knotted whip | Deut 8:15 |
| of uncertain derivation | דֹּמֶן *dômen* (H1828) | 6 | manure | 2Kgs 9:37 |
| of uncertain derivation | הֲדַס *hădaç* (H1918) | 6 | the myrtle | Neh 8:15 |
| of uncertain derivation | אָסוֹן *ʼâçôwn* (H611) | 5 | hurt | Gen 42:4 |
| of uncertain derivation | סְנַפִּיר *çᵉnappîyr* (H5579) | 5 | a fin (collectively) | Lev 11:9 |
| of uncertain derivation | חָגָב *châgâb* (H2284) | 5 | a locust | Lev 11:22 |
| of uncertain derivation | אֵת *ʼêth* (H855) | 5 | a hoe or other digging implement | 1Sam 13:20 |
| of uncertain derivation | דּוֹנַג *dôwnag* (H1749) | 4 | wax; | Ps 22:15 |
| of uncertain derivation | סַנְוֵר *çanvêr* (H5575) | 3 | (in plural) blindness | Gen 19:11 |
| of uncertain derivation | עֲטַלֵּף *ʻăṭallêph* (H5847) | 3 | a bat | Lev 11:19 |
| of uncertain derivation | סְמָדַר *çᵉmâdar* (H5563) | 3 | a vine blossom; used also adverbially, abloom | Song 2:13 |
| of uncertain derivation | אָח *ʼâch* (H254) | 3 | a fire-pot or chafing dish | Jer 36:22 |
| of uncertain derivation | חַשְׁמַל *chashmal* (H2830) | 3 | probably bronze or polished spectrum metal | Ezek 1:4 |
| of uncertain derivation | דַּרְדַּר *dardar* (H1863) | 2 | a thorn | Gen 3:18 |
| of uncertain derivation | אַרְנֶבֶת *ʼarnebeth* (H768) | 2 | the hare | Lev 11:6 |
| of uncertain derivation | דּוּכִיפַת *dûwkîyphath* (H1744) | 2 | the hoopoe or else the grouse | Lev 11:19 |
| of uncertain derivation | דׇּרְבוֹן *dorbôwn* (H1861) | 2 | a goad | 1Sam 13:21 |
| of uncertain derivation | אֶשְׁפָּר *ʼeshpâr* (H829) | 2 | a measured portion | 2Sam 6:19 |
| of uncertain derivation | אֲגַרְטָל *ʼăgarṭâl* (H105) | 2 | a basin | Ezra 1:9 |
| of uncertain derivation | גּוּשׁ *gûwsh* (H1487) | 2 | a mass of earth | Job 7:5 |
| of uncertain derivation | חַרְצֻבָּה *chartsubbâh* (H2784) | 2 | a fetter; figuratively, a pain | Ps 73:4 |
| of uncertain derivation | חֲבַצֶּלֶת *chăbatstseleth* (H2261) | 2 | probably meadow-saffron | Song 2:1 |
| of uncertain derivation | אֲזָד *ʼăzâd* (H230, Aram.) | 2 | firm | Dan 2:5 |
| of uncertain derivation | נְבִזְבָּה *nᵉbizbâh* (H5023, Aram.) | 2 | a largess | Dan 2:6 |
| of uncertain derivation | סַרְבַּל *çarbal* (H5622, Aram.) | 2 | a cloak | Dan 3:21 |
| of uncertain derivation | אֲבַטִּיחַ *ʼăbaṭṭîyach* (H20) | 1 | a melon (only plural) | Num 11:5 |
| of uncertain derivation | בֵּרִי *Bêrîy* (H1276) | 1 | (only in the plural and with the article) the Berites, a place in Palestine | 2Sam 20:14 |
| of uncertain derivation | דִּבְיוֹן *dibyôwn* (H1686) | 1 | probably some cheap vegetable, perhaps a bulbous root | 2Kgs 6:25 |
| of uncertain derivation | נָדָן *nâdân* (H5084) | 1 | a sheath (of a sword) | 1Chr 21:27 |
| of uncertain derivation | דַּהֲוָא *Dahăvâʼ* (H1723, Aram.) | 1 | Dahava, a people colonized in Samaria | Ezra 4:9 |
| of uncertain derivation | כִּידוֹר *kîydôwr* (H3593) | 1 | perhaps tumult | Job 15:24 |
| of uncertain derivation | חֲנָמָל *chănâmâl* (H2602) | 1 | perhaps the aphis or plantlouse | Ps 78:47 |
| of uncertain derivation | גּוּמָּץ *gûwmmâts* (H1475) | 1 | a pit | Eccl 10:8 |
| of uncertain derivation | פְּתִיגִיל *pᵉthîygîyl* (H6614) | 1 | probably a figured mantle forholidays | Isa 3:24 |
| of uncertain derivation | דְּיוֹ *dᵉyôw* (H1773) | 1 | ink | Jer 36:18 |
| of uncertain derivation | דֹּחַן *dôchan* (H1764) | 1 | millet | Ezek 4:9 |
| of uncertain derivation | פַּנַּג *pannag* (H6436) | 1 | probably pastry | Ezek 27:17 |
| of uncertain derivation | הָגִין *hâgîyn* (H1903) | 1 | perhaps suitable or turning | Ezek 42:12 |
| of uncertain derivation | שְׁטַר *shᵉṭar* (H7859, Aram.) | 1 | a side | Dan 7:5 |
| of uncertain derivation | אֶלְקֹשִׁי *ʼElqôshîy* (H512) | 1 | an Elkoshite or native of Elkosh | Nah 1:1 |
| persian | פַּתְבַּג *pathbag* (H6598) | 8 | a dainty | Dan 1:5 |
| persian | אׇסְפַּרְנָא *ʼoçparnâʼ* (H629, Aram.) | 7 | diligently | Ezra 5:8 |
| persian | דַּרְכְּמוֹן *darkᵉmôwn* (H1871) | 4 | a 'drachma', or coin | Ezra 2:69 |
| persian | אֲחַשְׁדַּרְפַּן *ʼăchashdarpan* (H323) | 4 | a satrap or governorof amain province (of Persia) | Ezra 8:36 |
| persian | אִגְּרָא *ʼiggᵉrâʼ* (H104, Aram.) | 3 | an epistle (as carried by a state courier or postman) | Ezra 4:8 |
| persian | פַּרְתַּם *partam* (H6579) | 3 | a grandee | Esth 1:3 |
| persian | אֲדַרְכֹּן *ʼădarkôn* (H150) | 2 | a daric or Persian coin | 1Chr 29:7 |
| persian | נִשְׁתְּוָן *nishtᵉvân* (H5406) | 2 | an epistle | Ezra 4:7 |
| persian | פִּתְגָּם *pithgâm* (H6599) | 2 | a (judicial) sentence | Esth 1:20 |
| persian | אֲחַשְׁתָּרָן *ʼăchashtârân* (H327) | 2 | a mule | Esth 8:10 |
| persian | מֶלְצָר *meltsâr* (H4453) | 2 | the butler or other officer in the Babylonian court | Dan 1:11 |
| persian | דְּתָבָר *dᵉthâbâr* (H1884, Aram.) | 2 | meaning one skilled in law; a judge | Dan 3:2 |
| persian | אַפְּתֹם *ʼappᵉthôm* (H674, Aram.) | 1 | revenue; others at the last | Ezra 4:13 |
| persian | אַדְרַזְדָּא *ʼadrazdâʼ* (H149, Aram.) | 1 | quickly or carefully | Ezra 7:23 |
| persian | אֱגוֹז *ʼĕgôwz* (H93) | 1 | a nut | Song 6:11 |
| persian | בַּג *bag* (H897) | 1 | food | Ezek 25:7 |
| probably of foreign | אֵפוֹד *ʼêphôwd* (H646) | 49 | a girdle; specifically the ephod or highpriest's shoulder-piece; also generally, an image | Exod 25:7 |
| probably of foreign | תַּחַשׁ *tachash* (H8476) | 14 | a (clean) animal with fur, probably a species of antelope | Exod 25:5 |
| probably of foreign | אֵזוֹב *ʼêzôwb* (H231) | 10 | hyssop | Exod 12:22 |
| probably of foreign | תַּרְשִׁישׁ *tarshîysh* (H8658) | 7 | a gem, perhaps the topaz | Exod 28:20 |
| probably of foreign | הַדָּבָר *haddâbâr* (H1907, Aram.) | 4 | a vizier | Dan 3:24 |
| probably of foreign | אַלְמֻגִּים *ʼalmuggîym* (H484) | 3 | almug (i.e. probably sandle-wood) sticks | 1Kgs 10:11 |
| probably of foreign | כַּרְמִיל *karmîyl* (H3758) | 3 | carmine, a deep red | 2Chr 2:6 |
| probably of foreign | כַּסְלֻחִים *Kaçluchîym* (H3695) | 2 | Casluchim, a people cognate to the Egyptians | Gen 10:14 |
| probably of foreign | שַׁעַטְנֵז *shaʻaṭnêz* (H8162) | 2 | linsey-woolsey, i.e. cloth of linen and wool carded and spun together | Lev 19:19 |
| probably of foreign | לוּז *lûwz* (H3869) | 1 | some kind of nuttree, perhaps the almond | Gen 30:37 |
| probably of foreign | כַּרְכֹּם *karkôm* (H3750) | 1 | the crocus | Song 4:14 |
| probably of foreign | בְּרוֹם *bᵉrôwm* (H1264) | 1 | damask (stuff of variegated thread) | Ezek 27:24 |

## Hebrew Bible: hapax legomena (2,539)

| Lemma | Gloss | Place |
|---|---|---|
| שַׁמּוֹת *Shammôwth* (H8054) | Shammoth, an Israelite | 1Chr 11:27 |
| הֲרוֹרִי *Hărôwrîy* (H2033) | a Harorite or mountaineer | 1Chr 11:27 |
| עִילַי *ʻÎylay* (H5866) | Ilai, an Israelite | 1Chr 11:29 |
| חֵלֶד *chêled* (H2466) | Cheled, an Israelite | 1Chr 11:30 |
| חוּרַי *Chûwray* (H2360) | Churai, an Israelite | 1Chr 11:32 |
| בַּחֲרוּמִי *Bachărûwmîy* (H978) | a Bacharumite or inhabitant of Bachurim | 1Chr 11:33 |
| הָשֵׁם *Hâshêm* (H2044) | Hashem, an Israelite | 1Chr 11:34 |
| גִּזוֹנִי *Gizôwnîy* (H1493) | a Gizonite or inhabitant of Gizoh | 1Chr 11:34 |
| שָׁגֶא *Shâgeʼ* (H7681) | Shage, an Israelite | 1Chr 11:34 |
| אֱלִיפָל *ʼĔlîyphâl* (H465) | Eliphal, an Israelite | 1Chr 11:35 |
| מְכֵרָתִי *Mᵉkêrâthîy* (H4382) | a Mekerathite, or inhabitant of Mekerah | 1Chr 11:36 |
| נַעֲרַי *Naʻăray* (H5293) | Naarai, an Israelite | 1Chr 11:37 |
| אֶזְבַּי *ʼEzbay* (H229) | Ezbai, an Israelite | 1Chr 11:37 |
| מִבְחָר *Mibchâr* (H4006) | Mibchar, an Israelite | 1Chr 11:38 |
| בֵּרֹתִי *Bêrôthîy* (H1307) | a Berothite, or inhabitant of Berothai | 1Chr 11:39 |
| עֲדִינָא *ʻĂdîynâʼ* (H5721) | Adina, an Israelite | 1Chr 11:42 |
| שִׁיזָא *Shîyzâʼ* (H7877) | Shiza, an Israelite | 1Chr 11:42 |
| מִתְנִי *Mithnîy* (H4981) | a Mithnite, or inhabitant of Methen | 1Chr 11:43 |
| עֻזִּיָּא *ʻUzzîyâʼ* (H5814) | Uzzija, an Israelite | 1Chr 11:44 |
| עַשְׁתְּרָתִי *ʻAshtᵉrâthîy* (H6254) | an Ashterathite or inhabitant of Ashtaroth | 1Chr 11:44 |
| שָׁמָע *Shâmâʻ* (H8091) | Shama, an Israelite | 1Chr 11:44 |
| עֲרֹעֵרִי *ʻĂrôʻêrîy* (H6200) | an Aroerite or inhabitant of Aroer | 1Chr 11:44 |
| תִּיצִי *Tîytsîy* (H8491) | a Titsite or descendant or inhabitant of an unknown Tits | 1Chr 11:45 |
| מַחֲוִים *Machăvîym* (H4233) | a Machavite or inhabitant of some place named Machaveh | 1Chr 11:46 |
| יְרִיבַי *Yᵉrîybay* (H3403) | Jeribai, an Israelite | 1Chr 11:46 |
| יוֹשַׁוְיָה *Yôwshavyâh* (H3145) | Joshavjah, an Israelite | 1Chr 11:46 |
| אֶלְנַעַם *ʼElnaʻam* (H493) | Elnaam, an Israelite | 1Chr 11:46 |
| יִתְמָה *Yithmâh* (H3495) | Jithmah, an Israelite | 1Chr 11:46 |
| מְצֹבָיָה *Mᵉtsôbâyâh* (H4677) | Metsobajah, a place in Palestine | 1Chr 11:47 |
| מִשְׁמַנָּה *Mishmannâh* (H4925) | Mashmannah, an Israelite | 1Chr 12:11 |
| מַכְבַּנַּי *Makbannay* (H4344) | a Macbannite or native of Macbena | 1Chr 12:14 |
| גִּדְיָה *gidyâh* (H1428) | a river brink | 1Chr 12:16 |
| שְׁמָעָה *Shᵉmâʻâh* (H8094) | Shemaah, an Israelite | 1Chr 12:3 |
| גִּבְעָתִי *Gibʻâthîy* (H1395) | a Gibathite, or inhabitant of Gibath | 1Chr 12:3 |
| גְּדֵרָתִי *Gᵉdêrâthîy* (H1452) | a Gederathite, or inhabitant of Gederah | 1Chr 12:5 |
| אֶלְעוּזַי *ʼElʻûwzay* (H498) | Eluzai, an Israelite | 1Chr 12:6 |
| בְּעַלְיָה *Bᵉʻalyâh* (H1183) | Bealjah, an Israelite | 1Chr 12:6 |
| יוֹעֶזֶר *Yôwʻezer* (H3134) | Joezer, an Israelite | 1Chr 12:7 |
| יוֹעֵאלָה *Yôwʻêʼlâh* (H3132) | Joelah, an Israelite | 1Chr 12:8 |
| כִּידוֹן *Kîydôwn* (H3592) | Kidon, a place in Palestine | 1Chr 13:9 |
| בְּעֶלְיָדָע *Bᵉʻelyâdâʻ* (H1182) | Beeljada, an Israelite | 1Chr 14:7 |
| קוּשָׁיָהוּ *qûwshâyâhûw* (H6984) | Kushajah, an Israelite | 1Chr 15:17 |
| בֵּן *Bên* (H1122) | Ben, an Israelite | 1Chr 15:18 |
| יַעֲזִיאֵל *Yaʻăzîyʼêl* (H3268) | Jaaziel, an Israelite | 1Chr 15:18 |
| עֲזִיאֵל *ʻĂzîyʼêl* (H5815) | Aziel, an Israelite | 1Chr 15:20 |
| יְחִיָּה *Yᵉchîyâh* (H3174) | Jechijah, an Israelite | 1Chr 15:24 |
| כַּרְבֵּל *karbêl* (H3736) | to gird or clothe | 1Chr 15:27 |
| תּוֹר *tôwr* (H8448) | a manner (as a sort of turn) | 1Chr 17:17 |
| שַׁוְשָׁא *Shavshâʼ* (H7798) | Shavsha, an Israelite | 1Chr 18:16 |
| טִבְחַת *Ṭibchath* (H2880) | Tibchath, a place in Syria | 1Chr 18:8 |
| כּוּן *Kûwn* (H3560) | Kun, a place in Syria | 1Chr 18:8 |
| מִפְשָׂעָה *miphsâʻâh* (H4667) | a stride, i.e. (by euphemism) the crotch | 1Chr 19:4 |
| הוֹמָם *Hôwmâm* (H1950) | Homam, an Edomitish chieftain | 1Chr 1:39 |
| חַמְרָן *Chamrân* (H2566) | Chamran, an Idumaean | 1Chr 1:41 |
| יַעֲקָן *Yaʻăqân* (H3292) | Jaakan, an Idumaean | 1Chr 1:42 |
| שׂוּר *sûwr* (H7787) | to saw | 1Chr 20:3 |
| סִפַּי *Çippay* (H5598) | Sippai, a Philistine | 1Chr 20:4 |
| לַחְמִי *Lachmîy* (H3902) | Lachmi, an Israelite; or rather probably a brief form | 1Chr 20:5 |
| נָדָן *nâdân* (H5084) | a sheath (of a sword) | 1Chr 21:27 |
| שֶׁקֶט *sheqeṭ* (H8253) | tranquillity | 1Chr 22:9 |
| זִינָא *Zîynâʼ* (H2126) | Zina, an Israelite | 1Chr 23:10 |
| זִיזָה *Zîyzâh* (H2125) | Zizah, an Israelite | 1Chr 23:11 |
| חֲזִיאֵל *Chăzîyʼêl* (H2381) | Chaziel, a Levite | 1Chr 23:9 |
| חֻפָּה *Chuppâh* (H2647) | Chuppah, an Israelite | 1Chr 24:13 |
| יֶשֶׁבְאָב *Yeshebʼâb* (H3428) | Jeshebab, an Israelite | 1Chr 24:13 |
| פִּצֵּץ *Pitstsêts* (H6483) | Pitstsets, a priest | 1Chr 24:15 |
| גָּמוּל *gâmûwl* (H1577) | Gamul, an Israelite | 1Chr 24:17 |
| שָׁמוּר *Shâmûwr* (H8053) | Shamur, an Israelite | 1Chr 24:24 |
| שֹׁהַם *Shôham* (H7719) | Shoham, an Israelite | 1Chr 24:27 |
| עִבְרִי *ʻIbrîy* (H5681) | Ibri, an Israelite | 1Chr 24:27 |
| שְׂעֹרִים *Sᵉʻôrîym* (H8188) | Seorim, an Israelite | 1Chr 24:8 |
| יִצְרִי *Yitsrîy* (H3339) | Jitsri, an Israelite | 1Chr 25:11 |
| יְשַׂרְאֵלָה *Yᵉsarʼêlâh* (H3480) | Jesarelah, an Israelite | 1Chr 25:14 |
| אֲשַׂרְאֵלָה *ʼĂsarʼêlâh* (H841) | Asarelah, an Israelite | 1Chr 25:2 |
| צְרִי *Tsᵉrîy* (H6874) | Tseri, an Israelite | 1Chr 25:3 |
| תַּלְמִיד *talmîyd* (H8527) | a pupil | 1Chr 25:8 |
| טְבַלְיָהוּ *Ṭᵉbalyâhûw* (H2882) | Tebaljah, an Israelite | 1Chr 26:11 |
| שַׁלֶּכֶת *Shalleketh* (H7996) | Shalleketh, a gate in Jerusalem | 1Chr 26:16 |
| יַתְנִיאֵל *Yathnîyʼêl* (H3496) | Jathniel, an Israelite | 1Chr 26:2 |
| פְּעֻלְּתַי *Pᵉʻullᵉthay* (H6469) | Peullethai, an Israelite | 1Chr 26:5 |
| עׇתְנִי *ʻOthnîy* (H6273) | Othni, an Israelite | 1Chr 26:7 |
| רְפָאֵל *Rᵉphâʼêl* (H7501) | Rephael, an Israelite | 1Chr 26:7 |
| סְמַכְיָהוּ *Çᵉmakyâhûw* (H5565) | Semakjah, an Israelite | 1Chr 26:7 |
| עֶזְרִי *ʻEzrîy* (H5836) | Ezri, an Israelite | 1Chr 27:26 |
| רָמָתִי *Râmâthîy* (H7435) | a Ramathite or inhabitant of Ramah | 1Chr 27:27 |
| שִׁפְמִי *Shiphmîy* (H8225) | a Shiphmite or inhabitant of Shepham | 1Chr 27:27 |
| גְּדֵרִי *Gᵉdêrîy* (H1451) | a Gederite, or inhabitant of Geder | 1Chr 27:28 |
| שָׁרוֹנִי *Shârôwnîy* (H8290) | a Sharonite or inhabitant of Sharon | 1Chr 27:29 |
| עַדְלַי *ʻAdlay* (H5724) | Adlai, an Israelite | 1Chr 27:29 |
| אוֹבִיל *ʼôwbîyl* (H179) | Obil, an Ishmaelite | 1Chr 27:30 |
| יָזִיז *Yâzîyz* (H3151) | Jaziz, an Israelite | 1Chr 27:31 |
| דּוֹדַי *Dôwday* (H1737) | Dodai, an Israelite | 1Chr 27:4 |
| עַמִּיזָבָד *ʻAmmîyzâbâd* (H5990) | Ammizabad, an Israelite | 1Chr 27:6 |
| שַׁמְהוּת *Shamhûwth* (H8049) | Shamhuth, an Israelite | 1Chr 27:8 |
| יִזְרָח *Yizrâch* (H3155) | a Jizrach (i.e. Ezrachite or Zarchite) or descendant of Zerach | 1Chr 27:8 |
| גִּנְזַךְ *ginzak* (H1597) | a treasury | 1Chr 28:11 |
| שַׁיִשׁ *shayish* (H7893) | white, i.e. marble. | 1Chr 29:2 |
| רַדַּי *Radday* (H7288) | Raddai, an Israelite | 1Chr 2:14 |
| יְרִיעוֹת *Yᵉrîyʻôwth* (H3408) | Jerioth, an Israelitess | 1Chr 2:18 |
| יֵשֶׁר *Yêsher* (H3475) | Jesher, an Israelite | 1Chr 2:18 |
| אַרְדּוֹן *ʼArdôwn* (H715) | Ardon, an Israelite | 1Chr 2:18 |
| בּוּנָה *Bûwnâh* (H946) | Bunah, an Israelite | 1Chr 2:25 |
| אֹרֶן *ʼÔren* (H767) | Oren, an Israelite | 1Chr 2:25 |
| עֲטָרָה *ʻĂṭârâh* (H5851) | Atarah, an Israelitess | 1Chr 2:26 |
| מַעַץ *Maʻats* (H4619) | Maats, an Israelite | 1Chr 2:27 |
| עֵקֶר *ʻÊqer* (H6134) | Eker, an Israelite | 1Chr 2:27 |
| אַחְבָן *ʼAchbân* (H257) | Achban, an Israelite | 1Chr 2:29 |
| מוֹלִיד *Môwlîyd* (H4140) | Molid, an Israelite | 1Chr 2:29 |
| זָזָא *zâzâʼ* (H2117) | Zaza, an Israelite | 1Chr 2:33 |
| מֵישָׁע *Mêyshâʻ* (H4337) | Mesha, an Israelite | 1Chr 2:42 |
| רַחַם *Racham* (H7357) | Racham, an Israelite | 1Chr 2:44 |
| יׇרְקְעָם *Yorqᵉʻâm* (H3421) | Jorkeam, a place in Palestine | 1Chr 2:44 |
| יֶהְדַי *Yehday* (H3056) | Jehdai, an Israelite | 1Chr 2:47 |
| רֶגֶם *Regem* (H7276) | Regem, an Israelite | 1Chr 2:47 |
| גֵּישָׁן *Gêyshân* (H1529) | Geshan, an Israelite | 1Chr 2:47 |
| שֶׁבֶר *Sheber* (H7669) | Sheber, an Israelite | 1Chr 2:48 |
| תִּרְחֲנָה *Tirchănâh* (H8647) | Tirchanah, an Israelite | 1Chr 2:48 |
| מַכְבֵּנָא *Makbênâʼ* (H4343) | Macbena, a place in Palestine settled by him | 1Chr 2:49 |
| גִּבְעָא *Gibʻâʼ* (H1388) | Giba, a place in Palestine | 1Chr 2:49 |
| חָרֵף *Chârêph* (H2780) | Chareph, an Israelite | 1Chr 2:51 |
| רֹאֵה *Rôʼêh* (H7204) | Roeh, an Israelite | 1Chr 2:52 |
| פּוּתִי *Pûwthîy* (H6336) | a Puthite (collectively) or descendants of an unknown Puth | 1Chr 2:53 |
| שֻׁמָתִי *Shumâthîy* (H8126) | a Shumathite (collectively) or descendants of Shumah | 1Chr 2:53 |
| מִשְׁרָעִי *Mishrâʻîy* (H4954) | a Mishraite, or inhabitant (collectively) of Mishra | 1Chr 2:53 |
| אֶשְׁתָּאֻלִי *ʼEshtâʼulîy* (H848) | an Eshtaolite (collectively) or inhabitant of Eshtaol | 1Chr 2:53 |
| תִּרְעָתִי *Tirʻâthîy* (H8654) | a Tirathite or inhabitant of an unknown Tirah | 1Chr 2:55 |
| שִׁמְעָתִי *Shimʻâthîy* (H8101) | a Shimathite (collectively) or descendants of Shimah | 1Chr 2:55 |
| שׂוּכָתִי *Sûwkâthîy* (H7756) | a Sukathite or descendant of an unknown Israelite named Sukah | 1Chr 2:55 |
| דָּרַע *Dâraʻ* (H1873) | Dara, an Israelite | 1Chr 2:6 |
| עָכָר *ʻÂkâr* (H5917) | Akar, an Israelite | 1Chr 2:7 |
| כְּלוּבַי *Kᵉlûwbay* (H3621) | Kelubai, an Israelite | 1Chr 2:9 |
| מַלְכִּירָם *Malkîyrâm* (H4443) | Malkiram, an Israelite | 1Chr 3:18 |
| שֶׁנְאַצַּר *Shenʼatstsar* (H8137) | Shenatstsar, an Israelite | 1Chr 3:18 |
| הוֹשָׁמָע *Hôwshâmâʻ* (H1953) | Hoshama, an Israelite | 1Chr 3:18 |
| נְדַבְיָה *Nᵉdabyâh* (H5072) | Nedabjah, an Israelite | 1Chr 3:18 |
| חֲשֻׁבָה *Chăshubâh* (H2807) | Cashubah, an Israelite | 1Chr 3:20 |
| אֹהֶל *ʼÔhel* (H169) | Ohel, an Israelite | 1Chr 3:20 |
| חֲסַדְיָה *Chăçadyâh* (H2619) | Chasadjah, an Israelite | 1Chr 3:20 |
| אַרְנָן *ʼArnân* (H770) | Arnan, an Israelite | 1Chr 3:21 |
| בָּרִיחַ *Bârîyach* (H1282) | Bariach, an Israelite | 1Chr 3:22 |
| הוֹדַיְוָהוּ *Hôwdayvâhûw* (H1939) | Hodajvah, an Israelite | 1Chr 3:24 |
| עֲנָנִי *ʻĂnânîy* (H6054) | Anani, an Israelite | 1Chr 3:24 |
| שׁוּחָה *Shûwchâh* (H7746) | Shuchah, an Israelite | 1Chr 4:11 |
| מְחִיר *Mᵉchîyr* (H4243) | Mechir, an Israelite | 1Chr 4:11 |
| תְּחִנָּה *Tᵉchinnâh* (H8468) | Techinnah, an Israelite | 1Chr 4:12 |
| חֲתַת *Chăthath* (H2867) | Chathath, an Israelite | 1Chr 4:13 |
| מְעוֹנֹתַי *Mᵉʻôwnôthay* (H4587) | Meonothai, an Israelite | 1Chr 4:14 |
| חֲרָשִׁים *Chărâshîym* (H2798) | mechanics, the name of a valley in Jerusalem | 1Chr 4:14 |
| עִירוּ *ʻÎyrûw* (H5900) | Iru, an Israelite | 1Chr 4:15 |
| נַעַם *Naʻam* (H5277) | Naam, an Israelite | 1Chr 4:15 |
| זִיפָה *Zîyphâh* (H2129) | Ziphah, an Israelite | 1Chr 4:16 |
| תִּירְיָא *Tîyrᵉyâʼ* (H8493) | fearful, Tirja, an Israelite | 1Chr 4:16 |
| אֲשַׂרְאֵל *ʼĂsarʼêl* (H840) | Asarel, an Israelite | 1Chr 4:16 |
| עֶזְרָה *ʻEzrâh* (H5834) | Ezrah, an Israelite | 1Chr 4:17 |
| יָלוֹן *Yâlôwn* (H3210) | Jalon, an Israelite | 1Chr 4:17 |
| יִשְׁבַּח *Yishbach* (H3431) | Jishbach, an Israelite | 1Chr 4:17 |
| יְהֻדִיָּה *Yᵉhudîyâh* (H3057) | Jehudijah, a Jewess | 1Chr 4:18 |
| יְקוּתִיאֵל *Yᵉqûwthîyʼêl* (H3354) | Jekuthiel, an Israelite | 1Chr 4:18 |
| בִּתְיָה *Bithyâh* (H1332) | Bithjah, an Egyptian woman | 1Chr 4:18 |
| נַחַם *Nacham* (H5163) | Nacham, an Israelite | 1Chr 4:19 |
| גַּרְמִי *Garmîy* (H1636) | bony, i.e. strong | 1Chr 4:19 |
| אֲחוּמַי *ʼĂchûwmay* (H267) | Achumai, an Israelite | 1Chr 4:2 |
| לַהַד *Lahad* (H3855) | Lahad, an Israelite | 1Chr 4:2 |
| שִׁימוֹן *Shîymôwn* (H7889) | Shimon, an Israelite | 1Chr 4:20 |
| רִנָּה *Rinnâh* (H7441) | Rinnah, an Israelite | 1Chr 4:20 |
| זוֹחֵת *Zôwchêth* (H2105) | Zocheth, an Israelite | 1Chr 4:20 |
| לֵכָה *lêkâh* (H3922) | Lekah, a place in Palestine | 1Chr 4:21 |
| לַעְדָּה *Laʻdâh* (H3935) | Ladah, an Israelite | 1Chr 4:21 |
| אַשְׁבֵּעַ *ʼAshbêaʻ* (H791) | Asbea, an Israelite | 1Chr 4:21 |
| יוֹקִים *Yôwqîym* (H3137) | Jokim, an Israelite | 1Chr 4:22 |
| כֹּזְבָא *Kôzᵉbâʼ* (H3578) | Cozeba, a place in Palestine | 1Chr 4:22 |
| שָׂרָף *Sârâph* (H8315) | Saraph, an Israelite | 1Chr 4:22 |
| נְטָעִים *Nᵉṭâʻîym* (H5196) | Netaim, a place in Palestine | 1Chr 4:23 |
| חַמּוּאֵל *Chammûwʼêl* (H2536) | Chammuel, an Israelite | 1Chr 4:26 |
| תּוֹלָד *Tôwlâd* (H8434) | Tolad, a place in Palestine | 1Chr 4:29 |
| יִשְׁמָא *Yishmâʼ* (H3457) | Jishma, an Israelite | 1Chr 4:3 |
| יִדְבָּשׁ *Yidbâsh* (H3031) | Jidbash, an Israelite | 1Chr 4:3 |
| צְלֶלְפּוֹנִי *Tsᵉlelpôwnîy* (H6753) | Tselelponi, an Israelitess | 1Chr 4:3 |
| תֹּכֶן *Tôken* (H8507) | Token, a place in Palestine | 1Chr 4:32 |
| מְשׁוֹבָב *Mᵉshôwbâb* (H4877) | Meshobab, an Israelite | 1Chr 4:34 |
| יַמְלֵךְ *Yamlêk* (H3230) | Jamlek, an Israelite | 1Chr 4:34 |
| יוֹשָׁה *Yôwshâh* (H3144) | Joshah, an Israelite | 1Chr 4:34 |
| יוֹשִׁבְיָה *Yôwshibyâh* (H3143) | Josibjah, an Israelite | 1Chr 4:35 |
| עֲשִׂיאֵל *ʻĂsîyʼêl* (H6221) | Asiel, an Israelite | 1Chr 4:35 |
| יַעֲקֹבָה *Yaʻăqôbâh* (H3291) | Jaakobah, an Israelite | 1Chr 4:36 |
| יְשׁוֹחָיָה *Yᵉshôwchâyâh* (H3439) | Jeshochajah, an Israelite | 1Chr 4:36 |
| יְשִׁימָאֵל *Yᵉshîymâʼêl* (H3450) | Jesimael, an Israelite | 1Chr 4:36 |
| שִׁפְעִי *Shiphʻîy* (H8230) | Shiphi, an Israelite | 1Chr 4:37 |
| חוּשָׁה *Chûwshâh* (H2364) | Chushah, an Israelite | 1Chr 4:4 |
| אֲחֻזָּם *ʼĂchuzzâm* (H275) | Achuzzam, an Israelite | 1Chr 4:6 |
| תֵּימְנִי *Têymᵉnîy* (H8488) | Temeni, an Israelite | 1Chr 4:6 |
| אֲחַשְׁתָּרִי *ʼăchashtârîy* (H326) | an achastarite (i.e. courier); the designation (rather than name) of an Israelite | 1Chr 4:6 |
| צֶרֶת *Tsereth* (H6889) | Tsereth, an Israelite | 1Chr 4:7 |
| יִצְחַר *Yitschar* (H3328) | Jitschar, an Israelite | 1Chr 4:7 |
| אֶתְנַן *ʼEthnan* (H869) | Ethnan, an Israelite | 1Chr 4:7 |
| עָנוּב *ʻÂnûwb* (H6036) | Anub, an Israelite | 1Chr 4:8 |
| צֹבֵבָה *Tsôbêbâh* (H6637) | Tsobebah, an Israelitess | 1Chr 4:8 |
| אֲחַרְחֵל *ʼĂcharchêl* (H316) | Acharchel, an Israelite | 1Chr 4:8 |
| הָרֻם *Hârum* (H2037) | Harum, an Israelite | 1Chr 4:8 |
| שָׁפָם *Shâphâm* (H8223) | Shapham, an Israelite | 1Chr 5:12 |
| יַעֲנַי *Yaʻănay* (H3285) | Jaanai, an Israelite | 1Chr 5:12 |
| יוֹרַי *Yôwray* (H3140) | Jorai, an Israelite | 1Chr 5:13 |
| יַעְכָּן *Yaʻkân* (H3275) | Jakan, an Israelite | 1Chr 5:13 |
| זִיעַ *Zîyaʻ* (H2127) | Zia, an Israelite | 1Chr 5:13 |
| חוּרִי *Chûwrîy* (H2359) | Churi, an Israelite | 1Chr 5:14 |
| יָרוֹחַ *Yârôwach* (H3386) | Jaroach, an Israelite | 1Chr 5:14 |
| יְשִׁישָׁי *Yᵉshîyshây* (H3454) | Jeshishai, an Israelite | 1Chr 5:14 |
| יַחְדוֹ *Yachdôw* (H3163) | Jachdo, an Israelite | 1Chr 5:14 |
| עַבְדִיאֵל *ʻAbdîyʼêl* (H5661) | Abdiel, an Israelite | 1Chr 5:15 |
| נוֹדָב *Nôwdâb* (H5114) | Nodab, an Arab tribe | 1Chr 5:19 |
| יַחְדִּיאֵל *Yachdîyʼêl* (H3164) | Jachdiel, an Israelite | 1Chr 5:24 |
| הָרָא *Hârâʼ* (H2024) | Hara, a region of Media | 1Chr 5:26 |
| בְּאֵרָה *Bᵉʼêrâh* (H880) | Beerah, an Israelite | 1Chr 5:6 |
| עָזָז *ʻÂzâz* (H5811) | Azaz, an Israelite | 1Chr 5:8 |
| אֲחִימוֹת *ʼĂchîymôwth* (H287) | Achimoth, an Israelite | 1Chr 6:10 |
| וַשְׁנִי *Vashnîy* (H2059) | Vashni, an Israelite | 1Chr 6:13 |
| חַגִּיָּה *Chaggîyâh* (H2293) | Chaggijah, an Israelite | 1Chr 6:15 |
| תּוֹחַ *Tôwach* (H8430) | Toach, an Israelite | 1Chr 6:19 |
| בַּעֲשֵׂיָה *Baʻăsêyâh* (H1202) | Baasejah, an Israelite | 1Chr 6:25 |
| אֶתְנִי *ʼEthnîy* (H867) | Ethni, an Israelite | 1Chr 6:26 |
| קִישִׁי *Qîyshîy* (H7029) | Kishi, an Israelite | 1Chr 6:29 |
| חִילֵן *Chîylên* (H2432) | Chilen, a place in Palestine | 1Chr 6:43 |
| עָנֵם *ʻÂnêm* (H6046) | Anem, a place in Palestine | 1Chr 6:58 |
| מָשָׁל *Mâshâl* (H4913) | Mashal, a place in Palestine | 1Chr 6:59 |
| יְאָתְרַי *yᵉʼâthᵉray* (H2979) | Jeatherai, an Israelite | 1Chr 6:6 |
| זֵיתָן *Zêythân* (H2133) | Zethan, an Israelite | 1Chr 7:10 |
| אֲחִישַׁחַר *ʼĂchîyshachar* (H300) | Achishachar, an Israelite | 1Chr 7:10 |
| עִיר *ʻÎyr* (H5893) | Ir, an Israelite | 1Chr 7:12 |
| אַחֵר *ʼAchêr* (H313) | Acher, an Israelite | 1Chr 7:12 |
| יַחְצִיאֵל *Yachtsîyʼêl* (H3185) | Jachtsiel, an Israelite | 1Chr 7:13 |
| פֶּרֶשׁ *Peresh* (H6570) | Peresh, an Israelite | 1Chr 7:16 |
| שֶׁרֶשׁ *Sheresh* (H8329) | Sheresh, an Israelite | 1Chr 7:16 |
| מֹלֶכֶת *Môleketh* (H4447) | Moleketh, an Israelitess | 1Chr 7:18 |
| אִישְׁהוֹד *ʼÎyshᵉhôwd* (H379) | Ishod, an Israelite | 1Chr 7:18 |
| אַחְיָן *ʼAchyân* (H291) | Achjan, an Israelite | 1Chr 7:19 |
| לִקְחִי *Liqchîy* (H3949) | Likchi, an Israelite | 1Chr 7:19 |
| אֲנִיעָם *ʼĂnîyʻâm* (H593) | Aniam, an Israelite | 1Chr 7:19 |
| יְרִיאֵל *Yᵉrîyʼêl* (H3400) | Jeriel, an Israelite | 1Chr 7:2 |
| יַחְמַי *Yachmay* (H3181) | Jachmai, an Israelite | 1Chr 7:2 |
| יִבְשָׂם *Yibsâm* (H3005) | Jibsam, an Israelite | 1Chr 7:2 |
| אֶלְעָדָה *ʼElʻâdâh* (H497) | Eladah, an Israelite | 1Chr 7:20 |
| עֶזֶר *ʻEzer* (H5827) | Ezer, the name of two Israelites | 1Chr 7:21 |
| אֶלְעָד *ʼElʻâd* (H496) | Elad, an Israelite | 1Chr 7:21 |
| שֶׁאֱרָה *Sheʼĕrâh* (H7609) | Sheerah, an Israelitess | 1Chr 7:24 |
| רֶפַח *Rephach* (H7506) | Rephach, an Israelite | 1Chr 7:25 |
| רֶשֶׁף *Resheph* (H7566) | Resheph, an Israelite | 1Chr 7:25 |
| תֶּלַח *Telach* (H8520) | Telach, an Israelite | 1Chr 7:25 |
| נַעֲרָן *Naʻărân* (H5295) | Naaran, a place in Palestine | 1Chr 7:28 |
| פָּסַךְ *Pâçak* (H6457) | Pasak, an Israelite | 1Chr 7:33 |
| בִּמְהָל *Bimhâl* (H1118) | Bimhal, an Israelite | 1Chr 7:33 |
| עַשְׁוָת *ʻAshvâth* (H6220) | Ashvath, an Israelite | 1Chr 7:33 |
| הֶלֶם *Helem* (H1987) | Helem, the name of two Israelites | 1Chr 7:35 |
| יִמְנָע *Yimnâʻ* (H3234) | Jimna, an Israelite | 1Chr 7:35 |
| שֶׁלֶשׁ *Shelesh* (H8028) | Shelesh, an Israelite | 1Chr 7:35 |
| עָמָל *ʻÂmâl* (H6000) | Amal, an Israelite | 1Chr 7:35 |
| סוּחַ *Çûwach* (H5477) | Suach, an Israelite | 1Chr 7:36 |
| חַרְנֶפֶר *Charnepher* (H2774) | Charnepher, an Israelite | 1Chr 7:36 |
| בֵּרִי *Bêrîy* (H1275) | Beri, an Israelite | 1Chr 7:36 |
| יִמְרָה *Yimrâh* (H3236) | Jimrah, an Israelite | 1Chr 7:36 |
| הוֹד *Hôwd* (H1936) | Hod, an Israelite | 1Chr 7:37 |
| שִׁלְשָׁה *Shilshâh* (H8030) | Shilshah, an Israelite | 1Chr 7:37 |
| בְּאֵרָא *Bᵉʼêrâʼ* (H878) | Beera, an Israelite | 1Chr 7:37 |
| פִּסְפָּה *Piçpâh* (H6462) | Pispah, an Israelite | 1Chr 7:38 |
| אֲרָא *ʼărâʼ* (H690) | Ara, an Israelite | 1Chr 7:38 |
| עֻלָּא *ʻUllâʼ* (H5925) | Ulla, an Israelite | 1Chr 7:39 |
| רִצְיָא *Ritsyâʼ* (H7525) | Ritsjah, an Israelite | 1Chr 7:39 |
| עִירִי *ʻÎyrîy* (H5901) | Iri, an Israelite | 1Chr 7:7 |
| זְמִירָה *Zᵉmîyrâh* (H2160) | Zemirah, an Israelite | 1Chr 7:8 |
| אַחְרַח *ʼAchrach* (H315) | Achrach, an Israelite | 1Chr 8:1 |
| יְעוּץ *Yᵉʻûwts* (H3263) | Jeuts, an Israelite | 1Chr 8:10 |
| שׇׁבְיָה *Shobyâh* (H7634) | Shobjah, an Israelite | 1Chr 8:10 |
| מִרְמָה *Mirmâh* (H4821) | Mirmah, an Israelite | 1Chr 8:10 |
| אֲבִיטוּב *ʼĂbîyṭûwb* (H36) | Abitub, an Israelite | 1Chr 8:11 |
| מִשְׁעָם *Mishʻâm* (H4936) | Misham, an Israelite | 1Chr 8:12 |
| עֶדֶר *ʻEder* (H5738) | Eder, an Israelite | 1Chr 8:15 |
| יִשְׁפָּה *Yishpâh* (H3472) | Jishpah, an Israelite | 1Chr 8:16 |
| חִזְקִי *Chizqîy* (H2395) | Chizki, an Israelite | 1Chr 8:17 |
| יִשְׁמְרַי *Yishmᵉray* (H3461) | Jishmerai, an Israelite | 1Chr 8:18 |
| יִזְלִיאָה *Yizlîyʼâh* (H3152) | Jizliah, an Israelite | 1Chr 8:18 |
| נוֹחָה *Nôwchâh* (H5119) | Nochah, an Israelite | 1Chr 8:2 |
| אֱלִיעֵינַי *ʼĔlîyʻêynay* (H462) | Elienai, an Israelite | 1Chr 8:20 |
| בְּרָאיָה *Bᵉrâʼyâh* (H1256) | Berajah, an Israelite | 1Chr 8:21 |
| שִׁמְרָת *Shimrâth* (H8119) | Shimrath, an Israelite | 1Chr 8:21 |
| יִשְׁפָּן *Yishpân* (H3473) | Jishpan, an Israelite | 1Chr 8:22 |
| עַנְתֹתִיָּה *ʻAnthôthîyâh* (H6070) | Anthothijah, an Israelite | 1Chr 8:24 |
| יִפְדְּיָה *Yiphdᵉyâh* (H3301) | Jiphdejah, an Israelite | 1Chr 8:25 |
| שַׁמְשְׁרַי *Shamshᵉray* (H8125) | Shamsherai, an Israelite | 1Chr 8:26 |
| שְׁחַרְיָה *Shᵉcharyâh* (H7841) | Shecharjah, an Israelite | 1Chr 8:26 |
| יַעֲרֶשְׁיָה *Yaʻăreshyâh* (H3298) | Jaareshjah, an Israelite | 1Chr 8:27 |
| אֲבִיהוּד *ʼĂbîyhûwd* (H31) | Abihud, the name of two Israelites | 1Chr 8:3 |
| זֶכֶר *Zeker* (H2144) | Zeker, an Israelite | 1Chr 8:31 |
| שִׁמְאָה *Shimʼâh* (H8039) | Shimah, an Israelite | 1Chr 8:32 |
| תַּאֲרֵעַ *Taʼărêaʻ* (H8390) | Taarea, an Israelite | 1Chr 8:35 |
| עֵשֶׁק *ʻÊsheq* (H6232) | Eshek, an Israelite | 1Chr 8:39 |
| אֲחוֹחַ *ʼĂchôwach* (H265) | Achoach, an Israelite | 1Chr 8:4 |
| אֵחוּד *ʼÊchûwd* (H261) | Echud, the name of three Israelites | 1Chr 8:6 |
| אֲחִיחֻד *ʼĂchîychud* (H284) | Achichud, an Israelite | 1Chr 8:7 |
| שַׁחֲרַיִם *Shachărayim* (H7842) | Shacharajim, an Israelite | 1Chr 8:8 |
| בָּעֲרָא *Bâʻărâʼ* (H1199) | Baara, an Israelitish woman | 1Chr 8:8 |
| חֹדֶשׁ *Chôdesh* (H2321) | Chodesh, an Israelitess | 1Chr 8:9 |
| צִבְיָא *Tsibyâʼ* (H6644) | Tsibja, an Israelite | 1Chr 8:9 |
| מֵישָׁא *Mêyshâʼ* (H4331) | Mesha, a place in Arabia; also an Israelite | 1Chr 8:9 |
| מַעֲשַׂי *Maʻăsay* (H4640) | Maasai, an Israelite | 1Chr 9:12 |
| יַחְזֵרָה *Yachzêrâh* (H3170) | Jachzerah, an Israelite | 1Chr 9:12 |
| מְשִׁלֵּמִית *Mᵉshillêmîyth* (H4921) | Meshillemith, an Israelite | 1Chr 9:12 |
| בַּקְבַּקַּר *Baqbaqqar* (H1230) | Bakbakkar, an Israelite | 1Chr 9:15 |
| חֶרֶשׁ *Cheresh* (H2792) | Cheresh, a Levite | 1Chr 9:15 |
| חָבֵת *châbêth* (H2281) | something fried, probably a griddle-cake | 1Chr 9:31 |
| פָּטִיר *pâṭîyr* (H6359) | open, i.e. unoccupied | 1Chr 9:33 |
| שִׁמְאָם *Shimʼâm* (H8043) | Shimam, an Israelite | 1Chr 9:38 |
| תַּחְרֵעַ *Tachrêaʻ* (H8475) | Tachrea, an Israelite | 1Chr 9:41 |
| יְעוּאֵל *Yᵉʻûwʼêl* (H3262) | Jeuel, the name of four Israelites | 1Chr 9:6 |
| יִבְנְיָה *Yibnᵉyâh* (H2997) | Jibnejah, an Israelite | 1Chr 9:8 |
| מִכְרִי *Mikrîy* (H4381) | Mikri, an Israelite | 1Chr 9:8 |
| יִבְנִיָּה *Yibnîyâh* (H2998) | Jibnijah, an Israelite | 1Chr 9:8 |
| מִסְעָד *miçʻâd* (H4552) | a balustrade (for stairs) | 1Kgs 10:12 |
| מִסְחָר *miçchâr* (H4536) | trade | 1Kgs 10:15 |
| פָּזַז *pâzaz* (H6338) | to refine (gold) | 1Kgs 10:18 |
| אֲדַד *ʼĂdad* (H111) | Adad (or Hadad), an Edomite | 1Kgs 11:17 |
| רְזוֹן *Rᵉzôwn* (H7331) | Rezon, a Syrian | 1Kgs 11:23 |
| צְרוּעָה *Tsᵉrûwʻâh* (H6871) | Tseruah, an Israelitess | 1Kgs 11:26 |
| סִבָּה *çibbâh* (H5438) | a (providential) turn (of affairs) | 1Kgs 12:15 |
| גָּלָל *gâlâl* (H1557) | dung (as in balls) | 1Kgs 14:10 |
| שֵׂיב *sêyb* (H7869) | old age | 1Kgs 14:4 |
| טַבְרִמּוֹן *Ṭabrimmôwn* (H2886) | Tabrimmon, a Syrian | 1Kgs 15:18 |
| חֶזְיוֹן *Chezyôwn* (H2383) | Chezjon, a Syrian | 1Kgs 15:18 |
| אֶתְבַּעַל *ʼEthbaʻal* (H856) | Ethbaal, a Phoenician king | 1Kgs 16:31 |
| חִיאֵל *Chîyʼêl* (H2419) | Chiel, an Israelite | 1Kgs 16:34 |
| אַרְצָא *ʼartsâʼ* (H777) | Artsa, an Israelite | 1Kgs 16:9 |
| שִׂיג *sîyg* (H7873) | a withdrawal (into a private place) | 1Kgs 18:27 |
| שָׁנַס *shânaç* (H8151) | to compress (with a belt) | 1Kgs 18:46 |
| רֶצֶף *retseph* (H7529) | a red-hot stone (for baking) | 1Kgs 19:6 |
| אֲכִילָה *ʼăkîylâh* (H396) | something eatable, i.e. food | 1Kgs 19:8 |
| רֵעִי *Rêʻîy* (H7472) | Rei, an Israelite | 1Kgs 1:8 |
| זֹחֶלֶת *Zôcheleth* (H2120) | Zocheleth, a boundary stone in. Palestine | 1Kgs 1:9 |
| חָשִׂף *châsiph* (H2835) | properly, drawn off, i.e. separated; hence, a small company (as divided from the rest) | 1Kgs 20:27 |
| חָלַט *châlaṭ* (H2480) | to snatch at | 1Kgs 20:33 |
| יִשְׁרָה *yishrâh* (H3483) | rectitude | 1Kgs 3:6 |
| אֲרֻבּוֹת *ʼĂrubbôwth* (H700) | Arubboth, a place in Palestine | 1Kgs 4:10 |
| טָפַת *Ṭâphath* (H2955) | Taphath, an Israelitess | 1Kgs 4:11 |
| אֲחִינָדָב *ʼĂchîynâdâb* (H292) | Achinadab, an Israelite | 1Kgs 4:14 |
| פָּרוּחַ *Pârûwach* (H6515) | Paruach, an Israelite | 1Kgs 4:17 |
| אֵלָא *ʼÊlâʼ* (H414) | Ela, an Israelite | 1Kgs 4:18 |
| גֶּבֶר *Geber* (H1398) | Geber, the name of two Israelites | 1Kgs 4:19 |
| אֱלִיחֹרֶף *ʼĔlîychôreph* (H456) | Elichoreph, an Israelite | 1Kgs 4:3 |
| שִׁישָׁא *Shîyshâʼ* (H7894) | Shisha, an Israelite | 1Kgs 4:3 |
| זָבוּד *Zâbûwd* (H2071) | given, Zabud, an Israelite | 1Kgs 4:5 |
| אֲחִישָׁר *ʼĂchîyshâr* (H301) | Achishar, an Israelite | 1Kgs 4:6 |
| מָקַץ *Mâqats* (H4739) | Makats, a place in Palestine | 1Kgs 4:9 |
| דַּרְדַּע *Dardaʻ* (H1862) | Darda, an Israelite | 1Kgs 5:11 |
| מָחוֹל *Mâchôwl* (H4235) | Machol, an Israelite | 1Kgs 5:11 |
| דֹּבְרָה *dôbᵉrâh* (H1702) | a raft | 1Kgs 5:23 |
| מַכֹּלֶת *makkôleth* (H4361) | nourishment | 1Kgs 5:25 |
| רְעִי *rᵉʻîy* (H7471) | pasture | 1Kgs 5:3 |
| בַּרְבֻּר *barbur* (H1257) | a fowl (as fattened on grain) | 1Kgs 5:3 |
| סִפֻּן *çippun* (H5604) | a wainscot | 1Kgs 6:15 |
| לִפְנַי *liphnay* (H3942) | anterior | 1Kgs 6:17 |
| בּוּל *Bûwl* (H945) | Bul, the eighth Hebrew month | 1Kgs 6:38 |
| מִגְרָעָה *migrâʻâh* (H4052) | a ledge or offset | 1Kgs 6:6 |
| לוּל *lûwl* (H3883) | a spiral step | 1Kgs 6:8 |
| שָׂבָךְ *sâbâk* (H7638) | a netting (ornament to the capital of a column) | 1Kgs 7:17 |
| חִשֻּׁק *chishshuq* (H2839) | conjoined, i.e. a wheel-spoke or rod connecting the hub with the rim | 1Kgs 7:33 |
| חִשֻּׁר *chishshur* (H2840) | combined, i.e. the nave or hub of awheel (as holding the spokes together) | 1Kgs 7:33 |
| מַעֲבֶה *maʻăbeh* (H4568) | properly, compact (part of soil), i.e. loam | 1Kgs 7:46 |
| שֶׁקֶף *sheqeph* (H8260) | a loophole (for looking out), to admit light and air | 1Kgs 7:5 |
| מַסַּד *maççad* (H4527) | a foundation | 1Kgs 7:9 |
| אֵיתָנִים *ʼÊythânîym* (H388) | Ethanim, the name of a month | 1Kgs 8:2 |
| צֶלְצַח *Tseltsach* (H6766) | Tseltsach, a place in Palestine | 1Sam 10:2 |
| מַטְרִי *Maṭrîy* (H4309) | Matri, an Israelite | 1Sam 10:21 |
| מַחֲרֶשֶׁת *machăresheth* (H4282) | probably a hoe | 1Sam 13:20 |
| פְּצִירָה *pᵉtsîyrâh* (H6477) | bluntness | 1Sam 13:21 |
| קִלְּשׁוֹן *qillᵉshôwn* (H7053) | a prong, i.e. hay-fork | 1Sam 13:21 |
| חָוָח *châvâch* (H2337) | a dell or crevice (as if pierced in the earth) | 1Sam 13:6 |
| יַעֲרָה *yaʻărâh* (H3295) | a copse of bushes; hence, a forest; hence, honey in the comb (as hived in trees) | 1Sam 14:27 |
| בּוֹצֵץ *Bôwtsêts* (H949) | Botsets, a rock near Michmash | 1Sam 14:4 |
| סֶנֶה *Çeneh* (H5573) | Seneh, a crag in Palestine | 1Sam 14:4 |
| מַעְצוֹר *maʻtsôwr* (H4622) | objectively, a hindrance | 1Sam 14:6 |
| שָׁסַף *shâçaph* (H8158) | to cut in pieces, i.e. slaughter | 1Sam 15:33 |
| טְלָאִים *Ṭᵉlâʼîym* (H2923) | Telaim, a place in Palestine | 1Sam 15:4 |
| נְמִבְזֶה *nᵉmibzeh* (H5240) | despised | 1Sam 15:9 |
| מַעֲרָה *maʻărâh* (H4630) | an open spot | 1Sam 17:23 |
| חַלֻּק *challuq* (H2512) | smooth | 1Sam 17:40 |
| יַלְקוּט *yalqûwṭ* (H3219) | a travelling pouch (as if for gleanings) | 1Sam 17:40 |
| מִצְחָה *mitschâh* (H4697) | a shinpiece of armor (as prominent), only plural | 1Sam 17:6 |
| עָוַן *ʻâvan* (H5770) | to watch (with jealosy) | 1Sam 18:9 |
| לַהֲקָה *lahăqâh* (H3862) | an assembly | 1Sam 19:20 |
| שֵׂכוּ *Sêkûw* (H7906) | Seku, a place in Palestine | 1Sam 19:22 |
| תֹּחוּ *Tôchûw* (H8459) | Tochu, an Israelite | 1Sam 1:1 |
| אֶזֶל *ʼezel* (H237) | Ezel, a memorial stone in Palestine | 1Sam 20:19 |
| פֶּשַׂע *pesaʻ* (H6587) | a stride | 1Sam 20:3 |
| מַרְדּוּת *mardûwth* (H4780) | rebelliousness | 1Sam 20:30 |
| אִין *ʼîyn* (H371) | is it not? | 1Sam 21:9 |
| נָחַץ *nâchats* (H5169) | to be urgent | 1Sam 21:9 |
| חֶרֶת *Chereth* (H2802) | Chereth, a thicket in Palestine | 1Sam 22:5 |
| כָּלִבּוֹ *Kâlibbôw* (H3614) | a Calebite or descendant of Caleb | 1Sam 25:3 |
| פּוּקָה *pûwqâh* (H6330) | a stumbling-block | 1Sam 25:31 |
| רַאֲשֹׁת *raʼăshôth* (H7226) | a pillow (being for the head) | 1Sam 26:12 |
| מָעוֹךְ *Mâʻôwk* (H4582) | Maok, a Philistine | 1Sam 27:2 |
| אָדַב *ʼâdab* (H109) | to languish | 1Sam 2:33 |
| אֲגוֹרָה *ʼăgôwrâh* (H95) | properly, something gathered, i.e. perhaps a grain or berry; used only of a small (silver) coin | 1Sam 2:36 |
| שִׂפְמוֹת *Siphmôwth* (H8224) | Siphmoth, a place in Palestine | 1Sam 30:28 |
| רָכָל *Râkâl* (H7403) | Rakal, a place in Palestine | 1Sam 30:29 |
| עֲתָךְ *ʻĂthâk* (H6269) | Athak, a place in Palestine | 1Sam 30:30 |
| מִפְרֶקֶת *miphreqeth* (H4665) | properly, a fracture, i.e. joint (vertebrae) of the neck | 1Sam 4:18 |
| שָׂתַר *sâthar* (H8368) | to break out (as an eruption) | 1Sam 5:9 |
| שֵׁן *Shên* (H8129) | Shen, a place in Palestine | 1Sam 7:12 |
| רַקָּחָה *raqqâchâh* (H7548) | a female perfumer | 1Sam 8:13 |
| טַבָּחָה *ṭabbâchâh* (H2879) | a female cook | 1Sam 8:13 |
| בְּכוֹרַת *Bᵉkôwrath* (H1064) | Bekorath, an Israelite | 1Sam 9:1 |
| אֲפִיחַ *ʼĂphîyach* (H647) | Aphiach, an Israelite | 1Sam 9:1 |
| שָׁלִשָׁה *Shâlishâh* (H8031) | Shalishah, a place in Palestine | 1Sam 9:4 |
| שַׁעֲלִים *Shaʻălîym* (H8171) | Shaalim, a place in Palestine | 1Sam 9:4 |
| תְּשׁוּרָה *tᵉshûwrâh* (H8670) | a gift | 1Sam 9:7 |
| נְסִבָּה *nᵉçibbâh* (H5252) | properly, an environment, i.e. circumstance or turn of affairs | 2Chr 10:15 |
| זַהַם *Zaham* (H2093) | Zaham, an Israelite | 2Chr 11:19 |
| אֲדוֹרַיִם *ʼĂdôwrayim* (H115) | Adorajim, a place in Palestine | 2Chr 11:9 |
| סֻכִּי *Çukkîy* (H5525) | a Sukkite, or inhabitant of some place near Egypt (i.e. hut-dwellers) | 2Chr 12:3 |
| צְפָתָה *Tsᵉphâthâh* (H6859) | Tsephathah, a place in Palestine | 2Chr 14:9 |
| חָלָא *châlâʼ* (H2456) | to be sick | 2Chr 16:12 |
| עֲמַסְיָה *ʻĂmaçyâh* (H6007) | Amasjah, an Israelite | 2Chr 17:16 |
| מַשֹּׂא *massôʼ* (H4856) | partiality (as a lifting up) | 2Chr 19:7 |
| מִקָּח *miqqâch* (H4727) | reception | 2Chr 19:7 |
| צִיץ *Tsîyts* (H6732) | Tsits, a place in Palestine | 2Chr 20:16 |
| יְרוּאֵל *Yᵉrûwʼêl* (H3385) | Jeruel, a place in Palestine | 2Chr 20:16 |
| דּוֹדָוָהוּ *Dôwdâvâhûw* (H1735) | Dodavah, an Israelite | 2Chr 20:37 |
| רַמִּי *rammîy* (H7421) | a Ramite, i.e. Aramaean | 2Chr 22:5 |
| תְּבוּסָה *tᵉbûwçâh* (H8395) | a treading down, i.e. ruin | 2Chr 22:7 |
| אֱלִישָׁפָט *ʼĔlîyshâphâṭ* (H478) | Elishaphat, an Israelite | 2Chr 23:1 |
| שִׁמְרִית *Shimrîyth* (H8116) | Shimrith, a Moabitess | 2Chr 24:26 |
| מִרְשַׁעַת *mirshaʻath* (H4849) | a female wicked doer | 2Chr 24:7 |
| יַבְנֶה *Yabneh* (H2996) | Jabneh, a place in Palestine | 2Chr 26:6 |
| יְחִזְקִיָּה *Yᵉchizqîyâh* (H3169) | Jechizkijah, the name of five Israelites | 2Chr 28:12 |
| חַדְלַי *Chadlay* (H2311) | Chadlai, an Israelite | 2Chr 28:12 |
| מַעֲרֹם *maʻărôm* (H4636) | bare | 2Chr 28:15 |
| גִּמְזוֹ *Gimzôw* (H1579) | Gimzo, a place in Palestine | 2Chr 28:18 |
| צֹרֶךְ *tsôrek* (H6878) | need | 2Chr 2:15 |
| רַפְסֹדָה *raphçôdâh* (H7513) | a raft (as flat on the water) | 2Chr 2:15 |
| סְפָר *çᵉphâr* (H5610) | a census | 2Chr 2:16 |
| אַרְגְּוָן *ʼargᵉvân* (H710) | purple | 2Chr 2:6 |
| שְׁחִיטָה *shᵉchîyṭâh* (H7821) | slaughter | 2Chr 30:17 |
| יִסְמַכְיָהוּ *Yiçmakyâhûw* (H3253) | Jismakjah, an Israelite | 2Chr 31:13 |
| אֲוֵרָה *ʼăvêrâh* (H220) | a stall | 2Chr 32:28 |
| חוֹזַי *Chôwzay* (H2335) | Chozai, an Israelite | 2Chr 33:19 |
| עֵילוֹם *ʻêylôwm* (H5865) | concealed, i.e. the vanishing point; generally, time out of mind (past or future), i.e. (practically | 2Chr 33:7 |
| בָּדַק *bâdaq* (H918) | to mend a breach | 2Chr 34:10 |
| חַסְרָה *Chaçrâh* (H2641) | Chasrah, an Israelite | 2Chr 34:22 |
| מִפְלַגָּה *miphlaggâh* (H4653) | a classification | 2Chr 35:12 |
| צֵלָחָה *tsêlâchâh* (H6745) | something protracted or flattened out, i.e. a platter | 2Chr 35:13 |
| חֲלֻקָּה *chăluqqâh* (H2515) | a distribution | 2Chr 35:5 |
| לָעַב *lâʻab* (H3931) | to deride | 2Chr 36:16 |
| יָשֵׁשׁ *yâshêsh* (H3486) | gray-haired, i.e. an aged man | 2Chr 36:17 |
| צַעְצֻעַ *tsaʻtsuaʻ* (H6816) | sculpture | 2Chr 3:10 |
| צֶפֶת *tsepheth* (H6858) | a capital of a column | 2Chr 3:15 |
| פַּרְוַיִם *Parvayim* (H6516) | Parvajim, an Oriental region | 2Chr 3:6 |
| מִכְלָה *miklâh* (H4357) | completion (in plural concrete adverbial, wholly) | 2Chr 4:21 |
| כֶּבֶשׁ *kebesh* (H3534) | a footstool (as trodden upon) | 2Chr 9:18 |
| חָזוֹת *châzôwth* (H2378) | a revelation | 2Chr 9:29 |
| עׇקְבָה *ʻoqbâh* (H6122) | trickery | 2Kgs 10:19 |
| מֶלְתָּחָה *meltâchâh* (H4458) | a wardrobe (i.e. room where clothing is spread) | 2Kgs 10:22 |
| מַחֲרָאָה *machărâʼâh* (H4280) | a sink | 2Kgs 10:27 |
| צִבֻּר *tsibbur* (H6652) | a pile | 2Kgs 10:8 |
| יְהוֹשֶׁבַע *Yᵉhôwshebaʻ* (H3089) | Jehosheba, an Israelitess | 2Kgs 11:2 |
| סוּר *Çûwr* (H5495) | Sur, a gate of the temple | 2Kgs 11:6 |
| מַסָּח *maççâch* (H4535) | a cordon, (adverbially) or (as a) military barrier | 2Kgs 11:6 |
| סִלָּא *Çillâʼ* (H5538) | Silla, a place in Jerusalem | 2Kgs 12:21 |
| יוֹזָכָר *Yôwzâkâr* (H3108) | Jozacar, an Israelite | 2Kgs 12:22 |
| קָבָל *qâbâl* (H6905) | the presence, i.e. (adverbially) in front of | 2Kgs 15:10 |
| אַרְיֵה *ʼAryêh* (H745) | Arjeh, an Israelite | 2Kgs 15:25 |
| מַרְצֶפֶת *martsepheth* (H4837) | a pavement | 2Kgs 16:17 |
| אֲרוֹמִי *ʼĂrôwmîy* (H726) | an Edomite (as in the margin) | 2Kgs 16:6 |
| שֹׁמרֹנִי *Shômrônîy* (H8118) | a Shomeronite (collectively) or inhabitants of Shomeron | 2Kgs 17:29 |
| נֵרְגַּל *Nêrᵉgal* (H5370) | Nergal, a Cuthite deity | 2Kgs 17:30 |
| אַשִׁימָא *ʼAshîymâʼ* (H807) | Ashima, a deity of Hamath | 2Kgs 17:30 |
| נִבְחַז *Nibchaz* (H5026) | Nibchaz, a deity of the Avites | 2Kgs 17:31 |
| תַּרְתָּק *Tartâq* (H8662) | Tartak, a deity of the Avvites | 2Kgs 17:31 |
| סְפַרְוִי *Çᵉpharvîy* (H5616) | a Sepharvite or inhabitant of Sepharvain | 2Kgs 17:31 |
| עֲנַמֶּלֶךְ *ʻĂnammelek* (H6048) | Anammelek, an Assyrian deity | 2Kgs 17:31 |
| סוֹא *Çôwʼ* (H5471) | So, an Egyptian king | 2Kgs 17:4 |
| חָפָא *châphâʼ* (H2644) | properly, to cover, i.e. (in a sinister sense) to act covertly | 2Kgs 17:9 |
| אֹמְנָה *ʼômᵉnâh* (H547) | a column | 2Kgs 18:16 |
| אֲבִי *ʼĂbîy* (H21) | Abi, Hezekiah's mother | 2Kgs 18:2 |
| נְחֻשְׁתָּן *Nᵉchushtân* (H5180) | something made of copper, i.e. the copper serpent of the Desert | 2Kgs 18:4 |
| מְשֻׁלֶּמֶת *Mᵉshullemeth* (H4922) | Meshullemeth, an Israelitess | 2Kgs 21:19 |
| חָרוּץ *Chârûwts* (H2743) | Charuts, an Israelite | 2Kgs 21:19 |
| יׇטְבָה *Yoṭbâh* (H3192) | Jotbah, a place in Palestine | 2Kgs 21:19 |
| יְדִידָה *Yᵉdîydâh* (H3040) | Jedidah, an Israelitess | 2Kgs 22:1 |
| חַרְחַס *Charchaç* (H2745) | Charchas, an Israelite | 2Kgs 22:14 |
| רוּמָה *Rûwmâh* (H7316) | Rumah, a place in Palestine | 2Kgs 23:36 |
| מַזָּלָה *mazzâlâh* (H4208) | a constellation, i.e. Zodiacal sign (perhaps as affecting the weather) | 2Kgs 23:5 |
| נְחֻשְׁתָּא *Nᵉchushtâʼ* (H5179) | Nechushta, an Israelitess | 2Kgs 24:8 |
| גּוּב *gûwb* (H1461) | to dig | 2Kgs 25:12 |
| צְלֹחִית *tsᵉlôchîyth* (H6746) | something prolonged or tall, i.e. a vial or salt-cellar | 2Kgs 2:20 |
| גָּלַם *gâlam* (H1563) | to fold | 2Kgs 2:8 |
| מִבְחוֹר *mibchôwr* (H4004) | select, i.e. well fortified | 2Kgs 3:19 |
| קַלָּע *qallâʻ* (H7051) | a slinger | 2Kgs 3:25 |
| מֵישַׁע *Mêyshaʻ* (H4338) | Mesha, a Moabite | 2Kgs 3:4 |
| אָסוּךְ *ʼâçûwk* (H610) | anointed, i.e. an oil-flask | 2Kgs 4:2 |
| זָרַר *zârar* (H2237) | perhaps to diffuse, i.e. (specifically) to sneeze | 2Kgs 4:35 |
| פַּקֻּעָה *paqquʻâh* (H6498) | the wild cucumber (from splitting open to shed its seeds) | 2Kgs 4:39 |
| צִקְלֹן *tsiqlôn* (H6861) | a sack (as tied at the mouth) | 2Kgs 4:42 |
| אֲבָנָה *ʼĂbânâh* (H71) | Abanah, a river near Damascus | 2Kgs 5:12 |
| פַּרְפַּר *Parpar* (H6554) | Parpar, a river of Syria | 2Kgs 5:12 |
| אֵיכֹה *ʼêykôh* (H351) | where | 2Kgs 6:13 |
| כֵּרָה *kêrâh* (H3740) | a purchase | 2Kgs 6:23 |
| קַב *qab* (H6894) | a hollow, i.e. vessel used as a (dry) measure | 2Kgs 6:25 |
| דִּבְיוֹן *dibyôwn* (H1686) | probably some cheap vegetable, perhaps a bulbous root | 2Kgs 6:25 |
| תַּחֲנָה *tachănâh* (H8466) | (only plural collectively) an encampment | 2Kgs 6:8 |
| נָחֵת *nâchêth* (H5185) | descending | 2Kgs 6:9 |
| מַכְבָּר *makbâr* (H4346) | a cloth (as netted) | 2Kgs 8:15 |
| צָעִיר *Tsâʻîyr* (H6811) | Tsair, a place in Idumaea | 2Kgs 8:21 |
| בִּדְקַר *Bidqar* (H920) | Bidkar, an Israelite | 2Kgs 9:25 |
| גּוּר *Gûwr* (H1483) | Gur, a place in Palestine | 2Kgs 9:27 |
| יְרֻבֶּשֶׁת *Yᵉrubbesheth* (H3380) | Jerubbesheth, a symbolic name for Gideon | 2Sam 11:21 |
| יְדִידְיָה *Yᵉdîydᵉyâh* (H3041) | Jedidejah, a name of Solomon | 2Sam 12:25 |
| מַגְזֵרָה *magzêrâh* (H4037) | a cutting implement, i.e. a blade | 2Sam 12:31 |
| אַרְבַּעְתַּיִם *ʼarbaʻtayim* (H706) | fourfold | 2Sam 12:6 |
| עַמִּיחוּר *ʻAmmîychûwr* (H5991) | Ammichur, a Syrian prince | 2Sam 13:37 |
| מַשְׂרֵת *masrêth* (H4958) | a pan | 2Sam 13:9 |
| עָפַר *ʻâphar* (H6080) | to be dust | 2Sam 16:13 |
| מִיכָל *mîykâl* (H4323) | properly, a container, i.e. a streamlet | 2Sam 17:20 |
| יִתְרָא *Yithrâʼ* (H3501) | Jithra, an Israelite (or Ishmaelite) | 2Sam 17:25 |
| שֹׁבִי *Shôbîy* (H7629) | Shobi, an Ammonite | 2Sam 17:27 |
| שָׁפָה *shâphâh* (H8194) | a cheese (as strained from the whey) | 2Sam 17:29 |
| שׂוֹבֶךְ *sôwbek* (H7730) | a thicket, i.e. interlaced branches | 2Sam 18:9 |
| שִׁיבָה *shîybâh* (H7871) | residence | 2Sam 19:33 |
| נִשֵּׂאת *nissêʼth* (H5379) | something taken, i.e. a present | 2Sam 19:43 |
| לָאַט *lâʼaṭ* (H3813) | to muffle | 2Sam 19:5 |
| שׂוּג *sûwg* (H7734) | to retreat | 2Sam 1:22 |
| שָׁבָץ *shâbâts* (H7661) | entanglement, i.e. (figuratively) perplexity | 2Sam 1:9 |
| יָגָה *yâgâh* (H3014) | to push away | 2Sam 20:13 |
| בֵּרִי *Bêrîy* (H1276) | (only in the plural and with the article) the Berites, a place in Palestine | 2Sam 20:14 |
| קָלַהּ *qâlahh* (H7035) | to assemble | 2Sam 20:14 |
| שְׁיָא *Shᵉyâʼ* (H7864) | Sheja, an Israelite | 2Sam 20:25 |
| יָאִרִי *Yâʼirîy* (H2972) | a Jairite or descendant of Jair | 2Sam 20:26 |
| חַיּוּת *chayûwth* (H2424) | life | 2Sam 20:3 |
| יָחַר *yâchar* (H3186) | to delay | 2Sam 20:5 |
| קַיִן *qayin* (H7013) | a lance (as striking fast) | 2Sam 21:16 |
| סַף *Çaph* (H5593) | Saph, a Philistine | 2Sam 21:18 |
| אַרְמֹנִי *ʼArmônîy* (H764) | Armoni, an Israelite | 2Sam 21:8 |
| חַשְׁרָה *chashrâh* (H2841) | properly, a combination or gathering, i.e. of watery clouds | 2Sam 22:12 |
| אָגֵא *ʼÂgêʼ* (H89) | Age, an Israelite | 2Sam 23:11 |
| אֱלִיקָא *ʼĔlîyqâʼ* (H470) | Elika, an Israelite | 2Sam 23:25 |
| פַּלְטִי *Palṭîy* (H6407) | a Paltite or descendant of Palti | 2Sam 23:26 |
| מְבֻנַּי *Mᵉbunnay* (H4012) | Mebunnai, an Israelite | 2Sam 23:27 |
| חֵלֶב *Chêleb* (H2460) | Cheleb, an Israelite | 2Sam 23:29 |
| הִדַּי *Hidday* (H1914) | Hiddai, an Israelite | 2Sam 23:30 |
| בַּרְחֻמִי *Barchumîy* (H1273) | a Barchumite, or native of Bachurim | 2Sam 23:31 |
| יָשֵׁן *Yâshên* (H3464) | Jashen, an Israelite | 2Sam 23:32 |
| שָׁרַר *Shârar* (H8325) | Sharar, an Israelite | 2Sam 23:33 |
| אֲחַסְבַּי *ʼĂchaçbay* (H308) | Achasbai, an Israelite | 2Sam 23:34 |
| פַּעֲרַי *Paʻăray* (H6474) | Paarai, an Israelite | 2Sam 23:35 |
| אַרְבִּי *ʼArbîy* (H701) | an Arbite or native of Arab | 2Sam 23:35 |
| תַּחְכְּמֹנִי *Tachkᵉmônîy* (H8461) | Tachkemoni, an Israelite | 2Sam 23:8 |
| עֲדִינוֹ *ʻădîynôw* (H5722) | his spear | 2Sam 23:8 |
| אַמָּה *ʼAmmâh* (H522) | Ammah, a hill in Palestine | 2Sam 2:24 |
| גִּיחַ *Gîyach* (H1520) | Giach, a place in Palestine | 2Sam 2:24 |
| בִּתְרוֹן *Bithrôwn* (H1338) | Bithron, a place East of the Jordan | 2Sam 2:29 |
| לוּשׁ *Lûwsh* (H3889) | Lush, a place in Palestine | 2Sam 3:15 |
| סִרָה *Çirâh* (H5626) | Sirah, a cistern so-called | 2Sam 3:26 |
| שְׁלִי *shᵉlîy* (H7987) | privacy | 2Sam 3:27 |
| כִּלְאָב *Kilʼâb* (H3609) | Kilab, an Israelite | 2Sam 3:3 |
| מְנַעְנַע *mᵉnaʻnaʻ* (H4517) | a sistrum (so called from its rattling sound) | 2Sam 6:5 |
| נָכוֹן *Nâkôwn* (H5225) | Nakon, probably an Israelite | 2Sam 6:6 |
| שַׁל *shal* (H7944) | a fault | 2Sam 6:7 |
| תּוֹרָה *tôwrâh* (H8452) | a custom | 2Sam 7:19 |
| בֶּטַח *Beṭach* (H984) | Betach, a place in Syria | 2Sam 8:8 |
| בָּדָל *bâdâl* (H915) | a part | Amos 3:12 |
| דְּמֶשֶׁק *dᵉmesheq* (H1833) | damask (as a fabric of Damascus) | Amos 3:12 |
| שֵׂחַ *sêach* (H7808) | communion, i.e. (reflexively) meditation | Amos 4:13 |
| דּוּגָה *dûwgâh* (H1729) | properly, fishery, i.e. a hook forfishing | Amos 4:2 |
| הַרְמוֹן *harmôwn* (H2038) | a castle (from its height) | Amos 4:3 |
| בָּשַׁס *bâshaç* (H1318) | to trample down | Amos 5:11 |
| אָפֵל *ʼâphêl* (H651) | dusky | Amos 5:20 |
| סִכּוּת *çikkûwth* (H5522) | an (idolatrous) booth | Amos 5:26 |
| כִּיּוּן *Kîyûwn* (H3594) | properly, a statue, i.e. idol; but used (by euphemism) forsome heathen deity (perhaps corresponding  | Amos 5:26 |
| סָרַף *çâraph* (H5635) | to cremate, i.e. to be (near) of kin (such being privileged to kindle the pyre) | Amos 6:10 |
| פָּרַט *pâraṭ* (H6527) | to scatter words, i.e. prate (or hum) | Amos 6:5 |
| מִרְזַח *mirzach* (H4797) | a cry, i.e. (of job), a revel | Amos 6:7 |
| תָּאַב *tâʼab* (H8374) | to loathe (morally) | Amos 6:8 |
| בּוֹקֵר *bôwqêr* (H951) | a cattle-tender | Amos 7:14 |
| בָּלַס *bâlaç* (H1103) | to pinch sycamore figs (a process necessary to ripen them) | Amos 7:14 |
| הֲרִיסָה *hărîyçâh* (H2034) | something demolished | Amos 9:11 |
| כְּבָרָה *kᵉbârâh* (H3531) | a sieve (as netted) | Amos 9:9 |
| רָשַׁם *râsham* (H7559) | to record | Dan 10:21 |
| מָדַי *Mâday* (H4075) | a Madian or native of Madai | Dan 11:1 |
| הֶדֶר *heder* (H1925) | honour; used (figuratively) for the capital city (Jerusalem) | Dan 11:20 |
| מֵרַע *mêraʻ* (H4827) | used as (abstract) noun, wickedness | Dan 11:27 |
| חֲלַקָּה *chălaqqâh* (H2514) | flattery | Dan 11:32 |
| מִכְמַן *mikman* (H4362) | treasure (as hidden) | Dan 11:43 |
| אַפֶּדֶן *ʼappeden* (H643) | a pavilion or palace-tent | Dan 11:45 |
| חוּב *chûwb* (H2325) | properly, perhaps to tie, i.e. (figuratively and reflexively) to owe, or (by implication) to forfeit | Dan 1:10 |
| אַשְׁפְּנַז *ʼAshpᵉnaz* (H828) | Ashpenaz, a Babylonian eunuch | Dan 1:3 |
| שַׁדְרַךְ *Shadrak* (H7714) | Shadrak, the Babylonian name of one of Daniel's companions | Dan 1:7 |
| מֵישַׁךְ *Mêyshak* (H4335) | Meshak, an Israelite | Dan 1:7 |
| יַבֶּשֶׁת *yabbesheth* (H3007, Aram.) | dry land | Dan 2:10 |
| בְּנַס *bᵉnaç* (H1149, Aram.) | to be enraged | Dan 2:12 |
| קְצַף *qᵉtsaph* (H7108, Aram.) | to become enraged | Dan 2:12 |
| עֵטָא *ʻêṭâʼ* (H5843, Aram.) | prudence | Dan 2:14 |
| טַבָּח *ṭabbâch* (H2877, Aram.) | a lifeguardsman | Dan 2:14 |
| מִישָׁאֵל *Mîyshâʼêl* (H4333, Aram.) | Mishael, an Israelite | Dan 2:17 |
| עֲזַרְיָה *ʻĂzaryâh* (H5839, Aram.) | Azarjah, one of Daniel's companions | Dan 2:17 |
| רְחֵם *rᵉchêm* (H7359, Aram.) | (plural) pity | Dan 2:18 |
| בִּינָה *bîynâh* (H999, Aram.) | understanding | Dan 2:21 |
| עֲמִיק *ʻămîyq* (H5994, Aram.) | profound, i.e. unsearchable | Dan 2:22 |
| חֲשׁוֹךְ *chăshôwk* (H2816, Aram.) | the dark | Dan 2:22 |
| אַחֲרִית *ʼachărîyth* (H320, Aram.) | later | Dan 2:28 |
| חֲדִי *chădîy* (H2306, Aram.) | a breast | Dan 2:32 |
| דְּרַע *dᵉraʻ* (H1872, Aram.) | an arm | Dan 2:32 |
| מְעָה *mᵉʻâh* (H4577, Aram.) | only in plural the bowels | Dan 2:32 |
| יַרְכָא *yarkâʼ* (H3410, Aram.) | a thigh | Dan 2:32 |
| שָׁק *shâq* (H8243, Aram.) | the leg | Dan 2:33 |
| עוּר *ʻûwr* (H5784, Aram.) | chaff (as the naked husk) | Dan 2:35 |
| אִדַּר *ʼiddar* (H147, Aram.) | ample, i.e. a threshing-floor | Dan 2:35 |
| קַיִט *qayiṭ* (H7007, Aram.) | harvest | Dan 2:35 |
| חֲשַׁל *chăshal* (H2827, Aram.) | to weaken, i.e. crush | Dan 2:40 |
| פֶּחָר *pechâr* (H6353, Aram.) | a potter | Dan 2:41 |
| פְּלַג *pᵉlag* (H6386, Aram.) | to split (literally or figuratively) | Dan 2:41 |
| נִצְבָּה *nitsbâh* (H5326, Aram.) | fixedness, i.e. firmness | Dan 2:41 |
| תְּבַר *tᵉbar* (H8406, Aram.) | to be fragile (figuratively) | Dan 2:42 |
| זְרַע *zᵉraʻ* (H2234, Aram.) | posterity | Dan 2:43 |
| דְּבַק *dᵉbaq* (H1693, Aram.) | to stick to | Dan 2:43 |
| נְסַךְ *nᵉçak* (H5260, Aram.) | to pour out a libation | Dan 2:46 |
| תִּנְיָנוּת *tinyânûwth* (H8579, Aram.) | a second time | Dan 2:7 |
| אַנְתּוּן *ʼantûwn* (H608, Aram.) | ye | Dan 2:8 |
| זְבַן *zᵉban* (H2084, Aram.) | to acquire by purchase | Dan 2:8 |
| כְּדַב *kᵉdab* (H3538, Aram.) | false | Dan 2:9 |
| בִּקְעָא *biqʻâʼ* (H1236, Aram.) | properly, a split, i.e. a wide level valley between mountains | Dan 3:1 |
| דּוּרָא *Dûwrâʼ* (H1757, Aram.) | Dura, a place in Babylonia | Dan 3:1 |
| יַת *yath* (H3487, Aram.) | a sign of the object of a verb | Dan 3:12 |
| רְגַז *rᵉgaz* (H7266, Aram.) | violent anger | Dan 3:13 |
| צְדָא *tsᵉdâʼ* (H6656, Aram.) | a (sinister) design | Dan 3:14 |
| עֲתִיד *ʻăthîyd* (H6263, Aram.) | prepared | Dan 3:15 |
| גִּבָּר *gibbâr* (H1401, Aram.) | valiant, or warrior | Dan 3:20 |
| כַּרְבְּלָא *karbᵉlâʼ* (H3737, Aram.) | a mantle | Dan 3:21 |
| תְּוַהּ *tᵉvahh* (H8429, Aram.) | to amaze, i.e. (reflex. by implication) take alarm | Dan 3:24 |
| חֲרַךְ *chărak* (H2761, Aram.) | to scorch | Dan 3:27 |
| רֵיחַ *rêyach* (H7382, Aram.) | odor (as if blown) | Dan 3:27 |
| רְחַץ *rᵉchats* (H7365, Aram.) | to attend upon | Dan 3:28 |
| שָׁלָה *shâlâh* (H7955, Aram.) | a wrong | Dan 3:29 |
| כָּרוֹז *kârôwz* (H3744, Aram.) | a herald | Dan 3:4 |
| שְׁלָה *shᵉlâh* (H7954, Aram.) | to be secure | Dan 4:1 |
| רַעֲנַן *raʻănan* (H7487, Aram.) | green, i.e. (figuratively) prosperous | Dan 4:1 |
| קְצַץ *qᵉtsats* (H7113, Aram.) | to chop off (literally or figuratively) | Dan 4:11 |
| נְתַר *nᵉthar* (H5426, Aram.) | to jump, i.e. be violently agitated; causatively, to terrify, shake off, untie | Dan 4:11 |
| בְּדַר *bᵉdar* (H921, Aram.) | to scatter | Dan 4:11 |
| נוּד *nûwd* (H5111, Aram.) | to flee | Dan 4:11 |
| תַּחַת *tachath* (H8479, Aram.) | the bottom (as depressed); only adverbially, below (often with prepositional prefix underneath), in  | Dan 4:11 |
| שְׁאֵלָא *shᵉʼêlâʼ* (H7595, Aram.) | properly, a question (at law), i.e. judicial decision or mandate | Dan 4:14 |
| שְׁפַל *shᵉphal* (H8215, Aram.) | low | Dan 4:14 |
| שְׁמַם *shᵉmam* (H8075, Aram.) | to stun (or intransitively, grow numb), i.e. devastate or (figuratively) stupefy (both usually in a  | Dan 4:16 |
| הַרְהֹר *harhôr* (H2031, Aram.) | a mental conception | Dan 4:2 |
| מְלַךְ *mᵉlak* (H4431, Aram.) | advice | Dan 4:24 |
| צִדְקָה *tsidqâh* (H6665, Aram.) | beneficence | Dan 4:24 |
| פְּרַק *pᵉraq* (H6562, Aram.) | to discontinue | Dan 4:24 |
| עִוְיָא *ʻivyâʼ* (H5758, Aram.) | perverseness | Dan 4:24 |
| עֲנָה *ʻănâh* (H6033, Aram.) | to depress literally or figuratively, transitive or intransitive (in various applications, as follow | Dan 4:24 |
| שְׁלֵוָה *shᵉlêvâh* (H7963, Aram.) | safety | Dan 4:24 |
| עוֹד *ʻôwd* (H5751, Aram.) | properly, iteration or continuance; used only adverbially (with or without preposition), again, repe | Dan 4:28 |
| חֲשַׁב *chăshab* (H2804, Aram.) | to regard | Dan 4:32 |
| תְּקַן *tᵉqan* (H8627, Aram.) | to straighten up, i.e. confirm | Dan 4:33 |
| יְסַף *yᵉçaph* (H3255, Aram.) | to add or augment (often adverbial, to continue to do a thing) | Dan 4:33 |
| מַעְבָד *maʻbâd* (H4567, Aram.) | an act | Dan 4:34 |
| גֵּוָה *gêvâh* (H1467, Aram.) | exaltation; (figuratively) arrogance | Dan 4:34 |
| אׇחֳרֵין *ʼochŏrêyn* (H318, Aram.) | last | Dan 4:5 |
| אֲנַס *ʼănaç* (H598, Aram.) | figuratively, to distress | Dan 4:6 |
| טְלַל *ṭᵉlal* (H2927, Aram.) | to cover with shade | Dan 4:9 |
| זוּן *zûwn* (H2110, Aram.) | perhaps properly, to be plump, i.e. (transitively) to nourish | Dan 4:9 |
| לְחֶם *lᵉchem* (H3900, Aram.) | (for man or beast), especially bread, or grain (for making it) | Dan 5:1 |
| מִשְׁתֶּה *mishteh* (H4961, Aram.) | a banquet | Dan 5:10 |
| אַחֲוָה *ʼachăvâh* (H263, Aram.) | solution (of riddles) | Dan 5:12 |
| אֲחִידָה *ʼăchîydâh* (H280, Aram.) | an enigma | Dan 5:12 |
| זוּד *zûwd* (H2103, Aram.) | to be proud | Dan 5:20 |
| עֲרָד *ʻărâd* (H6167, Aram.) | an onager | Dan 5:21 |
| נִשְׁמָא *nishmâʼ* (H5396, Aram.) | vital breath | Dan 5:23 |
| מֹאזֵן *môʼzên* (H3977, Aram.) | (only in the dual) a pair of scales | Dan 5:27 |
| חַסִּיר *chaççîyr* (H2627, Aram.) | deficient | Dan 5:27 |
| כְּרַז *kᵉraz* (H3745, Aram.) | to proclaim | Dan 5:29 |
| נֶבְרְשָׁא *nebrᵉshâʼ* (H5043, Aram.) | a light; plural (collectively) a chandelier | Dan 5:5 |
| גִּיר *gîyr* (H1528, Aram.) | lime | Dan 5:5 |
| חֲרַץ *chărats* (H2783, Aram.) | the loin (as the seat of strength) | Dan 5:6 |
| אַרְכֻבָה *ʼarkubâh* (H755, Aram.) | the knee | Dan 5:6 |
| נְקַשׁ *nᵉqash* (H5368, Aram.) | to knock | Dan 5:6 |
| שְׁבַשׁ *shᵉbash* (H7672, Aram.) | to entangle, i.e. perplex | Dan 5:9 |
| מָדַי *Mâday* (H4077, Aram.) | a Madian or native of Madai | Dan 6:1 |
| כַּו *kav* (H3551, Aram.) | a window (as a perforation) | Dan 6:11 |
| עַלִּית *ʻallîyth* (H5952, Aram.) | a second-story room | Dan 6:11 |
| נֶגֶד *neged* (H5049, Aram.) | opposite | Dan 6:11 |
| בֶּרֶךְ *berek* (H1291, Aram.) | a knee | Dan 6:11 |
| בְּאֵשׁ *bᵉʼêsh* (H888, Aram.) | to smell bad; figuratively, to be offensive morally | Dan 6:15 |
| בָּל *bâl* (H1079, Aram.) | properly, anxiety, i.e. (by implication) the heart (as its seat) | Dan 6:15 |
| מֵעָל *mêʻâl* (H4606, Aram.) | (only in plural as singular) the setting (of the sun) | Dan 6:15 |
| שֶׁמֶשׁ *shemesh* (H8122, Aram.) | the sun | Dan 6:15 |
| שְׁדַר *shᵉdar* (H7712, Aram.) | to endeavor | Dan 6:15 |
| חֲתַם *chătham* (H2857, Aram.) | to seal | Dan 6:18 |
| צְבוּ *tsᵉbûw* (H6640, Aram.) | properly, will; concretely, an affair (as a matter of determination) | Dan 6:18 |
| בּוּת *bûwth* (H956, Aram.) | to lodge over night | Dan 6:19 |
| טְוָת *ṭᵉvâth* (H2908, Aram.) | hunger (as twisting) | Dan 6:19 |
| דַּחֲוָה *dachăvâh* (H1761, Aram.) | probably a musical instrument (as being struck) | Dan 6:19 |
| שְׁנָה *shᵉnâh* (H8139, Aram.) | sleep | Dan 6:19 |
| נְדַד *nᵉdad* (H5075, Aram.) | to depart | Dan 6:19 |
| עֶשְׂרִין *ʻesrîyn* (H6243, Aram.) | twenty; also (ordinal) twentieth | Dan 6:2 |
| שְׁפַרְפַר *shᵉpharphar* (H8238, Aram.) | the dawn (as brilliant with aurora) | Dan 6:20 |
| נֹגַהּ *nôgahh* (H5053, Aram.) | dawn | Dan 6:20 |
| עֲצַב *ʻătsab* (H6088, Aram.) | to afflict | Dan 6:21 |
| זְעִק *zᵉʻiq* (H2200, Aram.) | to make an outcry | Dan 6:21 |
| סְגַר *çᵉgar* (H5463, Aram.) | to shut up; figuratively, to surrender | Dan 6:23 |
| זָכוּ *zâkûw* (H2136, Aram.) | purity | Dan 6:23 |
| חֲבוּלָה *chăbûwlâh* (H2248, Aram.) | properly, overthrown, i.e. (morally) crime | Dan 6:23 |
| טְאֵב *ṭᵉʼêb* (H2868, Aram.) | to rejoice | Dan 6:24 |
| נָשִׁין *nâshîyn* (H5389, Aram.) | a man | Dan 6:25 |
| אַרְעִית *ʼarʻîyth* (H773, Aram.) | the bottom | Dan 6:25 |
| גֶּרֶם *gerem* (H1635, Aram.) | a bone | Dan 6:25 |
| עֵלָּא *ʻêllâʼ* (H5924, Aram.) | above | Dan 6:3 |
| נְצַח *nᵉtsach* (H5330, Aram.) | to become chief | Dan 6:4 |
| עֲשִׁת *ʻăshith* (H6246, Aram.) | to purpose | Dan 6:4 |
| נְגַד *nᵉgad* (H5047, Aram.) | to flow (through the idea of clearing the way) | Dan 7:10 |
| שְׁמַשׁ *shᵉmash* (H8120, Aram.) | to serve | Dan 7:10 |
| יְקֵדָא *yᵉqêdâʼ* (H3346, Aram.) | a conflagration | Dan 7:11 |
| אֵשׁ *ʼêsh* (H785, Aram.) | fire (literally or figuratively) | Dan 7:11 |
| עֲנַן *ʻănan* (H6050, Aram.) | a cloud (as covering the sky), i.e. the nimbus or thunder-cloud | Dan 7:13 |
| כָּרָא *Kârâʼ* (H3735, Aram.) | to grieve | Dan 7:15 |
| נִדְנֶה *nidneh* (H5085, Aram.) | a sheath; figuratively, the body (as the receptacle of the soul) | Dan 7:15 |
| יְצַב *yᵉtsab* (H3321, Aram.) | to be firm; hence, to speak surely | Dan 7:19 |
| גִּיחַ *gîyach* (H1519, Aram.) | to rush forth | Dan 7:2 |
| חַבְרָה *chabrâh* (H2273, Aram.) | an associate | Dan 7:20 |
| קְרָב *qᵉrâb* (H7129, Aram.) | hostile encounter | Dan 7:21 |
| דּוּשׁ *dûwsh* (H1759, Aram.) | to trample | Dan 7:23 |
| בְּלָא *bᵉlâʼ* (H1080, Aram.) | to afflict | Dan 7:25 |
| סְבַר *çᵉbar* (H5452, Aram.) | to bear in mind, i.e. hope | Dan 7:25 |
| פְּלַג *pᵉlag* (H6387, Aram.) | a half | Dan 7:25 |
| שְׁמַד *shᵉmad* (H8046, Aram.) | to desolate | Dan 7:26 |
| כָּה *kâh* (H3542, Aram.) | properly, like this, i.e. by implication, (of manner) thus (or so); also (of place) here (or hither) | Dan 7:28 |
| לֵב *lêb* (H3821, Aram.) | the heart; also used (figuratively) very widely for the feelings, the will and even the intellect; l | Dan 7:28 |
| נְטַר *nᵉṭar* (H5202, Aram.) | to retain | Dan 7:28 |
| מְרַט *mᵉraṭ* (H4804, Aram.) | to pull off | Dan 7:4 |
| תִּנְיָן *tinyân* (H8578, Aram.) | second | Dan 7:5 |
| דֹּב *dôb* (H1678, Aram.) | the bear (as slow) | Dan 7:5 |
| שְׁטַר *shᵉṭar* (H7859, Aram.) | a side | Dan 7:5 |
| עֲלַע *ʻălaʻ* (H5967, Aram.) | a rib | Dan 7:5 |
| נְמַר *nᵉmar* (H5245, Aram.) | a leopard (from its stripes) | Dan 7:6 |
| אֵמְתָּנִי *ʼêmᵉtânîy* (H574, Aram.) | well-loined (i.e. burly) or mighty | Dan 7:7 |
| שְׂכַל *sᵉkal* (H7920, Aram.) | to be (causatively, make or act) circumspect and hence, intelligent | Dan 7:8 |
| זְעֵיר *zᵉʻêyr* (H2192, Aram.) | small | Dan 7:8 |
| תְּלַג *tᵉlag* (H8517, Aram.) | snow | Dan 7:9 |
| חִוָּר *chivvâr* (H2358, Aram.) | white | Dan 7:9 |
| עֲמַר *ʻămar* (H6015, Aram.) | wool | Dan 7:9 |
| נְקֵא *nᵉqêʼ* (H5343, Aram.) | clean | Dan 7:9 |
| גַּלְגַּל *galgal* (H1535, Aram.) | a wheel | Dan 7:9 |
| דְּלַק *dᵉlaq* (H1815, Aram.) | to flame (literally or figuratively) | Dan 7:9 |
| בֵּלְשַׁאצַּר *Bêlshaʼtstsar* (H1112) | Belshatstsar, a Babylonian king | Dan 8:1 |
| פַּלְמוֹנִי *palmôwnîy* (H6422) | a certain one, i.e. so-and-so | Dan 8:13 |
| מִצְּעִירָה *mitstsᵉʻîyrâh* (H4704) | properly, littleness; concretely, diminutive | Dan 8:9 |
| יְעָף *yᵉʻâph* (H3288) | fatigue (adverb, utterly exhausted) | Dan 9:21 |
| חָתַךְ *châthak* (H2852) | properly, to cut off, i.e. (figuratively) to decree | Dan 9:24 |
| שֶׁכֶן *sheken* (H7933) | a residence | Deut 12:5 |
| רָאָה *râʼâh* (H7201) | a bird of prey (probably the vulture, from its sharp sight) | Deut 14:13 |
| אַקּוֹ *ʼaqqôw* (H689) | slender, i.e. the ibex | Deut 14:5 |
| דִּישֹׁן *dîyshôn* (H1788) | the leaper, i.e. an antelope | Deut 14:5 |
| זֶמֶר *zemer* (H2169) | a gazelle (from its lightly touching the ground) | Deut 14:5 |
| מַשֶּׁה *mashsheh* (H4874) | a debt | Deut 15:2 |
| מִסָּה *miççâh* (H4530) | abundance, i.e. (adverbially) liberally | Deut 16:10 |
| קֵבָה *qêbâh* (H6896) | the paunch (as a cavity) or first stomach of ruminants | Deut 18:3 |
| סוּף *Çûwph* (H5489) | the Reed (Sea) | Deut 1:1 |
| תֹּפֶל *Tôphel* (H8603) | Tophel, a place near the Desert | Deut 1:1 |
| הוּן *hûwn* (H1951) | properly, to be naught, i.e. (figuratively) to be (causatively, act) light | Deut 1:41 |
| שָׂנִיא *sânîyʼ* (H8146) | hated | Deut 21:15 |
| מַעֲקֶה *maʻăqeh* (H4624) | a parapet | Deut 22:8 |
| קָרֶה *qâreh* (H7137) | an (unfortunate) occurrence, i.e. some accidental (ceremonial) disqualification | Deut 23:11 |
| אָזֵן *ʼâzên* (H240) | a spade or paddle (as having a broad end) | Deut 23:14 |
| דַּכָּה *dakkâh* (H1795) | mutilated | Deut 23:2 |
| שׇׁפְכָה *shophkâh* (H8212) | a pipe (for pouring forth, e.g. wine), i.e. the penis | Deut 23:2 |
| מְלִילָה *mᵉlîylâh* (H4425) | a head of grain (as cut off) | Deut 23:26 |
| מָבֻשׁ *mâbush* (H4016) | (plural) the (male) pudenda | Deut 25:11 |
| חָשַׁל *châshal* (H2826) | to make (intrans. be) unsteady, i.e. weak | Deut 25:18 |
| סָכַת *çâkath* (H5535) | by implication, to observe quietly | Deut 27:9 |
| מִגְעֶרֶת *migʻereth* (H4045) | reproof (i.e. curse) | Deut 28:20 |
| דַּלֶּקֶת *dalleqeth* (H1816) | a burning fever | Deut 28:22 |
| חַרְחֻר *charchur* (H2746) | fever (as hot) | Deut 28:22 |
| כָּלֶה *kâleh* (H3616) | pining | Deut 28:32 |
| חָסַל *châçal* (H2628) | to eat off | Deut 28:38 |
| רֹךְ *rôk* (H7391) | softness (figuratively) | Deut 28:56 |
| שִׁלְיָה *shilyâh* (H7988) | a fetus or babe (as extruded in birth) | Deut 28:57 |
| רַגָּז *raggâz* (H7268) | timid | Deut 28:65 |
| דְּאָבוֹן *dᵉʼâbôwn* (H1671) | pining | Deut 28:65 |
| זַמְזֹם *Zamzôm* (H2157) | a Zamzumite, or native tribe of Palestine | Deut 2:20 |
| חֲצֵרִים *Chătsêrîym* (H2699) | Chatserim, a place in Palestine | Deut 2:23 |
| מִדְרָךְ *midrâk* (H4096) | a treading, i.e. a place for stepping on | Deut 2:5 |
| יְלֵל *yᵉlêl* (H3214) | a howl | Deut 32:10 |
| חֶמֶר *chemer* (H2561) | wine (as fermenting) | Deut 32:14 |
| כָּשָׂה *kâsâh* (H3780) | to grow fat (i.e. be covered with flesh) | Deut 32:15 |
| שָׁיָה *shâyâh* (H7876) | to keep in memory | Deut 32:18 |
| שָׂעִיר *sâʻîyr* (H8164) | a shower (as tempestuous) | Deut 32:2 |
| מָזֶה *mâzeh* (H4198) | exhausted | Deut 32:24 |
| מְרִירִי *mᵉrîyrîy* (H4815) | bitter, i.e. poisonous | Deut 32:24 |
| פָּאָה *pâʼâh* (H6284) | to puff, i.e. blow away | Deut 32:26 |
| כָּמַס *kâmaç* (H3647) | to store away, i.e. (figuratively) in the memory | Deut 32:34 |
| שִׁלֵּם *shillêm* (H8005) | requital | Deut 32:35 |
| פְּתַלְתֹּל *pᵉthaltôl* (H6618) | tortuous (i.e. crafty) | Deut 32:5 |
| קְטוֹרָה *qᵉṭôwrâh* (H6988) | perfume | Deut 33:10 |
| חׇפַף *chophaph* (H2653) | to cover (in protection) | Deut 33:12 |
| גֶּרֶשׁ *geresh* (H1645) | produce (as if expelled) | Deut 33:14 |
| שֶׁפַע *shephaʻ* (H8228) | resources | Deut 33:19 |
| שָׂפַן *sâphan* (H8226) | to conceal (as a valuable) | Deut 33:19 |
| אֶשְׁדָּת *ʼeshdâth* (H799) | a fire-law | Deut 33:2 |
| זָנַק *zânaq* (H2187) | properly, to draw together the feet (as an animal about to dart upon its prey), i.e. to spring forwa | Deut 33:22 |
| מִנְעָל *minʻâl* (H4515) | a bolt | Deut 33:25 |
| דֹּבֶא *dôbeʼ* (H1679) | quiet | Deut 33:25 |
| חָבַב *châbab* (H2245) | properly, to hide (as in the bosom), i.e. to cherish (with affection) | Deut 33:3 |
| תָּכָה *tâkâh* (H8497) | to strew, i.e. encamp | Deut 33:3 |
| דַּבָּרָה *dabbârâh* (H1703) | a word | Deut 33:3 |
| לֵחַ *lêach* (H3893) | freshness, i.e. vigor | Deut 34:7 |
| שִׂיאֹן *Sîyʼôn* (H7865) | Sion, the summit of Mount Hermon | Deut 4:48 |
| מִסְכֵּנֻת *miçkênuth* (H4544) | indigence | Deut 8:9 |
| קְשִׁי *qᵉshîy* (H7190) | obstinacy | Deut 9:27 |
| הוֹלֵלוּת *hôwlêlûwth* (H1948) | folly | Eccl 10:13 |
| שְׁתִי *shᵉthîy* (H8358) | intoxicaion | Eccl 10:17 |
| מְקָרֶה *mᵉqâreh* (H4746) | properly, something meeting, i.e. a frame (of timbers) | Eccl 10:18 |
| שִׁפְלוּת *shiphlûwth* (H8220) | remissness | Eccl 10:18 |
| סֶכֶל *çekel* (H5529) | silliness; concretely and collectively, dolts | Eccl 10:6 |
| גּוּמָּץ *gûwmmâts* (H1475) | a pit | Eccl 10:8 |
| שַׁחֲרוּת *shachărûwth* (H7839) | a dawning, i.e. (figuratively) juvenescence | Eccl 11:10 |
| מַשְׂמְרָה *masmᵉrâh* (H4930) | a peg | Eccl 12:11 |
| אֲסֻפָּה *ʼăçuppâh* (H627) | a collection of (learned) men (only in the plural) | Eccl 12:11 |
| לַהַג *lahag* (H3854) | intense mental application | Eccl 12:12 |
| יְגִעָה *yᵉgiʻâh* (H3024) | fatigue | Eccl 12:12 |
| בָּטֵל *bâṭêl* (H988) | to desist from labor | Eccl 12:3 |
| טַחֲנָה *ṭachănâh* (H2913) | a hand mill; hence (figuratively) chewing | Eccl 12:4 |
| חַתְחַת *chathchath* (H2849) | terror | Eccl 12:5 |
| אֲבִיּוֹנָה *ʼăbîyôwnâh* (H35) | provocative of desire; the caper berry (from its stimulative taste) | Eccl 12:5 |
| אָזַן *ʼâzan* (H239) | to weigh, i.e. (figuratively) ponder | Eccl 12:9 |
| חֶסְרוֹן *cheçrôwn* (H2642) | deficiency | Eccl 1:15 |
| רְאִית *rᵉʼîyth* (H7212) | sight | Eccl 5:10 |
| רַאֲוָה *raʼăvâh* (H7207) | sight, i.e. satisfaction | Eccl 5:10 |
| תַּקִּיף *taqqîyph* (H8623) | powerful | Eccl 6:10 |
| פֵּשֶׁר *pêsher* (H6592) | an interpretation | Eccl 8:1 |
| בּוּר *bûwr* (H952) | to bore, i.e. (figuratively) examine | Eccl 9:1 |
| עֲבָד *ʻăbâd* (H5652) | a deed | Eccl 9:1 |
| מֵרוֹץ *mêrôwts* (H4793) | a run (the trial of speed) | Eccl 9:11 |
| מְהוּמָן *Mᵉhûwmân* (H4104) | Mehuman, a eunuch of Xerxes | Esth 1:10 |
| בִּזְתָא *Bizthâʼ* (H968) | Biztha, a eunuch of Xerxes | Esth 1:10 |
| בִּגְתָא *Bigthâʼ* (H903) | Bigtha, a eunuch of Xerxes | Esth 1:10 |
| אֲבַגְתָא *ʼĂbagthâʼ* (H5) | Abagtha, a eunuch of Xerxes | Esth 1:10 |
| זֵתַר *Zêthar* (H2242) | Zethar, a eunuch of Xerxes | Esth 1:10 |
| כַּרְכַּס *Karkaç* (H3752) | Karkas, a eunuch of Xerxes | Esth 1:10 |
| כַּרְשְׁנָא *Karshᵉnâʼ* (H3771) | Karshena, a courtier of Xerxes | Esth 1:14 |
| שֵׁתָר *Shêthâr* (H8369) | Shethar, a Persian satrap | Esth 1:14 |
| אַדְמָתָא *ʼAdmâthâʼ* (H133) | Admatha, a Persian nobleman | Esth 1:14 |
| מֶרֶס *Mereç* (H4825) | Meres, a Persian | Esth 1:14 |
| מַרְסְנָא *Marçᵉnâʼ* (H4826) | Marsena, a Persian | Esth 1:14 |
| בִּזָּיוֹן *bizzâyôwn* (H963) | disesteem | Esth 1:18 |
| כַּרְפַּס *karpaç* (H3768) | byssus or fine vegetable wool | Esth 1:6 |
| בַּהַט *bahaṭ* (H923) | white marble or perhaps alabaster | Esth 1:6 |
| דַּר *dar* (H1858) | properly, a pearl (from its sheen as rapidly turned); by analogy, pearl-stone, i.e. mother-of-pearl  | Esth 1:6 |
| סֹחֵרֶת *çôchêreth* (H5508) | probably a (black) tile (or tessara) forlaying borders with | Esth 1:6 |
| שְׁתִיָּה *shᵉthîyâh* (H8360) | potation | Esth 1:8 |
| אָנַס *ʼânaç* (H597) | to insist | Esth 1:8 |
| מָרוּק *mârûwq* (H4795) | properly, rubbed; but used abstractly, a rubbing (with perfumery) | Esth 2:12 |
| שַׁעַשְׁגַּז *Shaʻashgaz* (H8190) | Shaashgaz, a eunuch of Xerxes | Esth 2:14 |
| טֵבֶת *Ṭêbeth* (H2887) | Tebeth, the tenth Hebrew month | Esth 2:16 |
| הֲנָחָה *hănâchâh* (H2010) | permission of rest, i.e. quiet | Esth 2:18 |
| אׇמְנָה *ʼomnâh* (H545) | tutelage | Esth 2:20 |
| הֲדַסָּה *Hădaççâh* (H1919) | Hadassah (or Esther) | Esth 2:7 |
| הַצָּלָה *hatstsâlâh* (H2020) | rescue | Esth 4:14 |
| נֵזֶק *nêzeq* (H5143) | loss | Esth 7:4 |
| רַמָּךְ *rammâk* (H7424) | a brood mare | Esth 8:10 |
| עָתוּד *ʻâthûwd* (H6259) | prepared | Esth 8:13 |
| תַּכְרִיךְ *takrîyk* (H8509) | a wrapper or robe | Esth 8:15 |
| יָהַד *yâhad* (H3054) | to Judaize, i.e. become Jewish | Esth 8:17 |
| אׇבְדַן *ʼobdan* (H13) | a perishing | Esth 8:6 |
| סִיוָן *Çîyvân* (H5510) | Sivan, the third Hebrew month | Esth 8:9 |
| אַבְדָן *ʼabdân* (H12) | a perishing | Esth 9:5 |
| פַּרְשַׁנְדָּתָא *Parshandâthâʼ* (H6577) | Parshandatha, a son of Haman | Esth 9:7 |
| דַּלְפוֹן *Dalphôwn* (H1813) | Dalphon, a son of Haman | Esth 9:7 |
| אַסְפָּתָא *ʼAçpâthâʼ* (H630) | Aspatha, a son of Haman | Esth 9:7 |
| פּוֹרָתָא *Pôwrâthâʼ* (H6334) | Poratha, a son of Haman | Esth 9:8 |
| אֲדַלְיָא *ʼĂdalyâʼ* (H118) | Adalja, a son of Haman | Esth 9:8 |
| אֲרִידָתָא *ʼĂrîydâthâʼ* (H743) | Aridatha, a son of Haman | Esth 9:8 |
| פַּרְמַשְׁתָּא *Parmashtâʼ* (H6534) | Parmashta, a son of Haman | Esth 9:9 |
| אֲרִיסַי *ʼĂrîyçay* (H747) | Arisai, a son of Haman | Esth 9:9 |
| אֲרִידַי *ʼĂrîyday* (H742) | Aridai, a son of Haman | Esth 9:9 |
| וַיְזָתָא *Vayzâthâʼ* (H2055) | Vajezatha, a son of Haman | Esth 9:9 |
| כָּסַס *kâçaç* (H3699) | to estimate | Exod 12:4 |
| נָא *nâʼ* (H4995) | properly, tough, i.e. uncooked (flesh) | Exod 12:9 |
| כְּבֵדֻת *kᵉbêduth* (H3517) | difficulty | Exod 14:25 |
| צָלַל *tsâlal* (H6749) | properly, to tumble down, i.e. settle by awaving motion | Exod 15:10 |
| עָרַם *ʻâram* (H6192) | to pile up | Exod 15:8 |
| חַסְפַּס *chaçpaç* (H2636) | a shred or scale | Exod 16:14 |
| צַפִּיחִת *tsappîychith* (H6838) | a flat thin cake | Exod 16:31 |
| צִנְצֶנֶת *tsintseneth* (H6803) | a vase (probably a vial tapering at the top) | Exod 16:33 |
| כֵּס *kêç* (H3676) | a flag; also a sail; by implication, a flagstaff; generally a signal; figuratively, a token | Exod 17:16 |
| פִּתֹם *Pithôm* (H6619) | Pithom, a place in Egypt | Exod 1:11 |
| שִׁפְרָה *Shiphrâh* (H8236) | Shiphrah, an Israelitess | Exod 1:15 |
| פּוּעָה *Pûwʻâh* (H6326) | Puah, an Israelitess | Exod 1:15 |
| חָיֶה *châyeh* (H2422) | vigorous | Exod 1:19 |
| עוֹנָה *ʻôwnâh* (H5772) | sexual (cohabitation) | Exod 21:10 |
| רָצַע *râtsaʻ* (H7527) | to pierce | Exod 21:6 |
| דֶּמַע *demaʻ* (H1831) | a tear; figuratively, juice | Exod 22:28 |
| בְּעֵרָה *bᵉʻêrâh* (H1200) | a burning | Exod 22:5 |
| אָיַב *ʼâyab* (H340) | to hate (as one of an opposite tribe or party); hence to be hostile | Exod 23:22 |
| לִבְנָה *libnâh* (H3840) | properly, whiteness, i.e. (by implication) transparency | Exod 24:10 |
| סֶרַח *çerach* (H5629) | a redundancy | Exod 26:12 |
| מִגְבָּלָה *migbâlâh* (H4020) | a border | Exod 28:14 |
| שַׁרְשָׁה *sharshâh* (H8331) | a chain (as rooted, i.e. linked) | Exod 28:22 |
| תַּשְׁבֵּץ *tashbêts* (H8665) | checkered stuff (as reticulated) | Exod 28:4 |
| נוּק *nûwq* (H5134) | to suckle | Exod 2:9 |
| מִקְטָר *miqṭâr* (H4729) | something to fume (incense) on i.e. a hearth place | Exod 30:1 |
| יָסַךְ *yâçak* (H3251) | to pour (intransitive) | Exod 30:32 |
| שְׁחֵלֶת *shᵉchêleth* (H7827) | a scale or shell, i.e. the aromatic mussel. | Exod 30:34 |
| חֶלְבְּנָה *chelbᵉnâh* (H2464) | galbanam, an odorous gum (as if fatty) | Exod 30:34 |
| חָרַת *chârath* (H2801) | to engrave | Exod 32:16 |
| חֲלוּשָׁה *chălûwshâh* (H2476) | defeat | Exod 32:18 |
| שִׁמְצָה *shimtsâh* (H8103) | scornful whispering (of hostile spectators) | Exod 32:25 |
| מַטְוֶה *maṭveh* (H4299) | something spun | Exod 35:25 |
| לַבָּה *labbâh* (H3827) | flame | Exod 3:2 |
| מוּלָה *mûwlâh* (H4139) | circumcision | Exod 4:26 |
| סִתְרִי *Çithrîy* (H5644) | Sithri, an Israelite, | Exod 6:22 |
| אֱלִישֶׁבַע *ʼĔlîyshebaʻ* (H472) | Elisheba, the wife of Aaron | Exod 6:23 |
| אֲבִיאָסָף *ʼĂbîyʼâçâph* (H23) | Abiasaph, an Israelite | Exod 6:24 |
| פּוּטִיאֵל *Pûwṭîyʼêl* (H6317) | Putiel, an Israelite | Exod 6:25 |
| קֹצֶר *qôtser* (H7115) | shortness (of spirit), i.e. impatience | Exod 6:9 |
| גִּבְעֹל *gibʻôl* (H1392) | the calyx of a flower | Exod 9:31 |
| אָפִיל *ʼâphîyl* (H648) | unripe | Exod 9:32 |
| רׇגְזָה *rogzâh* (H7269) | trepidation | Ezek 12:18 |
| טָעָה *ṭâʻâh* (H2937) | to wander; causatively to lead astray | Ezek 13:10 |
| חַיִץ *chayits* (H2434) | a wall | Ezek 13:10 |
| טִיחַ *ṭîyach* (H2915) | mortar or plaster | Ezek 13:12 |
| שַׁלֶּטֶת *shalleṭeth* (H7986) | a vixen | Ezek 16:30 |
| נֵדֶה *nêdeh* (H5078) | a bounty (for prostitution) | Ezek 16:33 |
| נָדָן *nâdân* (H5083) | a present (for prostitution) | Ezek 16:33 |
| מִשְׁעִי *mishʻîy* (H4935) | inspection | Ezek 16:4 |
| בָּתַק *bâthaq* (H1333) | to cut in pieces | Ezek 16:40 |
| קַט *qaṭ* (H6985) | a little, i.e. (adverbially) merely | Ezek 16:47 |
| שִׂבְעָה *sibʻâh* (H7653) | satiety | Ezek 16:49 |
| גֹּעַל *gôʻal* (H1604) | abhorrence | Ezek 16:5 |
| תָּלַל *tâlal* (H8524) | to pile up, i.e. elevate | Ezek 17:22 |
| יְנִיקָה *yᵉnîyqâh* (H3242) | a sucker or sapling | Ezek 17:4 |
| צַפְצָפָה *tsaphtsâphâh* (H6851) | a willow (as growing in overflowed places) | Ezek 17:5 |
| כָּפַן *kâphan* (H3719) | to bend | Ezek 17:7 |
| קָסַס *qâçaç* (H7082) | to lop off | Ezek 17:9 |
| חוֹב *chôwb* (H2326) | debt | Ezek 18:7 |
| עָנֵף *ʻânêph* (H6058) | branching | Ezek 19:10 |
| סוּגַר *çûwgar* (H5474) | an inclosure, i.e. cage (for an animal) | Ezek 19:9 |
| רָצָא *râtsâʼ* (H7519) | to run; also to delight in | Ezek 1:14 |
| בָּזָק *bâzâq* (H965) | a flash of lightning | Ezek 1:14 |
| יוֹיָכִין *Yôwyâkîyn* (H3112) | Jojakin, an Israelite king | Ezek 1:2 |
| בּוּזִי *Bûwzîy* (H941) | Buzi, an Israelite | Ezek 1:3 |
| נָצַץ *nâtsats* (H5340) | to glare, i.e. be bright-colored | Ezek 1:7 |
| בָּמָה *Bâmâh* (H1117) | Bamah, a place in Palestine | Ezek 20:29 |
| מָסֹרֶת *mâçôreth* (H4562) | a band | Ezek 20:37 |
| מְרִירוּת *mᵉrîyrûwth* (H4814) | bitterness, i.e. (figuratively) grief | Ezek 21:11 |
| חָדַר *châdar* (H2314) | properly, to inclose (as a room), i.e. (by analogy,) to beset (as in a siege) | Ezek 21:19 |
| אִבְחָה *ʼibchâh* (H19) | brandishing of a sword | Ezek 21:20 |
| מָעֹט *mâʻôṭ* (H4593) | thinned (as to the edge), i.e. sharp | Ezek 21:20 |
| אָחַד *ʼâchad* (H258) | to unify, i.e. (figuratively) collect (one's thoughts) | Ezek 21:21 |
| צָרַב *tsârab* (H6866) | to burn | Ezek 21:3 |
| קְבֻצָה *qᵉbutsâh* (H6910) | a hoard | Ezek 22:20 |
| הִתּוּךְ *hittûwk* (H2046) | a melting | Ezek 22:22 |
| גֹּשֶׁם *gôshem* (H1656) | a shower | Ezek 22:24 |
| קַלָּסָה *qallâçâh* (H7048) | ridicule | Ezek 22:4 |
| עֲגָבָה *ʻăgâbâh* (H5691) | love (abstractly), i.e. amorousness | Ezek 23:11 |
| טָבוּל *ṭâbûwl* (H2871) | properly, dyed, i.e. a turban (probably as of colored stuff) | Ezek 23:15 |
| שׁוֹעַ *Shôwaʻ* (H7772) | Shoa, an Oriental people | Ezek 23:23 |
| קוֹעַ *Qôwaʻ* (H6970) | Koa, a region of Babylon | Ezek 23:23 |
| הֹצֶן *hôtsen* (H2021) | a weapon of war | Ezek 23:24 |
| מִרְבָּה *mirbâh* (H4767) | abundance, i.e. a great quantity | Ezek 23:32 |
| כָּחַל *kâchal* (H3583) | to paint (with stibium) | Ezek 23:40 |
| תְּאֻן *tᵉʼun* (H8383) | naughtiness, i.e. toil | Ezek 24:12 |
| מַחְמָל *machmâl* (H4263) | properly, sympathy; | Ezek 24:21 |
| הַשְׁמָעוּת *hashmâʻûwth* (H2045) | announcement | Ezek 24:26 |
| רֶתַח *rethach* (H7571) | a boiling | Ezek 24:5 |
| בַּג *bag* (H897) | food | Ezek 25:7 |
| סָחָה *çâchâh* (H5500) | to sweep away | Ezek 26:4 |
| מְחִי *mᵉchîy* (H4239) | a stroke, i.e. battering-ram | Ezek 26:9 |
| קֹבֶל *qôbel* (H6904) | a battering-ram | Ezek 26:9 |
| גַּמָּד *gammâd* (H1575) | a warrior (as grasping weapons) | Ezek 27:11 |
| סְחֹרָה *çᵉchôrâh* (H5506) | traffic | Ezek 27:15 |
| פַּנַּג *pannag* (H6436) | probably pastry | Ezek 27:17 |
| חֶלְבּוֹן *Chelbôwn* (H2463) | Chelbon, a place in Syria | Ezek 27:18 |
| צַחַר *tsachar* (H6713) | sheen, i.e. whiteness | Ezek 27:18 |
| וְדָן *Vᵉdân* (H2051) | Vedan (or Aden), a place in Arabia | Ezek 27:19 |
| עָשׁוֹת *ʻâshôwth* (H6219) | shining, i.e. polished | Ezek 27:19 |
| חֹפֶשׁ *Chôphesh* (H2667) | something spread loosely, i.e. a carpet | Ezek 27:20 |
| רִכְבָּה *rikbâh* (H7396) | a chariot (collectively) | Ezek 27:20 |
| כַּנֶּה *Kanneh* (H3656) | Canneh, a place in Assyria | Ezek 27:23 |
| כִּלְמָד *Kilmâd* (H3638) | Kilmad, a place apparently in the Assyrian empire | Ezek 27:23 |
| מִכְלֻל *miklul* (H4360) | something perfect, i.e. a splendid garment | Ezek 27:24 |
| גְּלוֹם *gᵉlôwm* (H1545) | clothing (as wrapped) | Ezek 27:24 |
| בְּרוֹם *bᵉrôwm* (H1264) | damask (stuff of variegated thread) | Ezek 27:24 |
| אָרַז *ʼâraz* (H729) | of cedar | Ezek 27:24 |
| מַרְכֹּלֶת *markôleth* (H4819) | a mart | Ezek 27:24 |
| מְבוֹאָה *mᵉbôwʼâh* (H3997) | a haven | Ezek 27:3 |
| נִי *nîy* (H5204) | lamentation | Ezek 27:32 |
| דֻּמָּה *dummâh* (H1822) | desolation; concretely, desolate | Ezek 27:32 |
| אֲשֻׁר *ʼăshur* (H839) | the cedar tree or some other light elastic wood | Ezek 27:6 |
| גְּבַל *Gᵉbal* (H1380) | Gebal, a place in Phoenicia | Ezek 27:9 |
| מְסֻכָּה *mᵉçukkâh* (H4540) | a covering, i.e. garniture | Ezek 28:13 |
| נֶקֶב *neqeb* (H5345) | a bezel (for a gem) | Ezek 28:13 |
| מִמְשַׁח *mimshach* (H4473) | outspread (i.e. with outstretched wings) | Ezek 28:14 |
| עָמַד *ʻâmad* (H5976) | to shake | Ezek 29:7 |
| הִי *hîy* (H1958) | lamentation | Ezek 2:10 |
| סָרָב *çârâb* (H5621) | a thistle | Ezek 2:6 |
| הָהּ *hâhh* (H1929) | ah! expressing grief | Ezek 30:2 |
| חִתּוּל *chittûwl* (H2848) | swathed, i.e. a bandage | Ezek 30:21 |
| כּוּב *Kûwb* (H3552) | Kub, a country near Egypt | Ezek 30:5 |
| עֻלְפֶּה *ʻulpeh* (H5969) | an envelope, i.e. (figuratively) mourning | Ezek 31:15 |
| סַרְעַפָּה *çarʻappâh* (H5634) | a twig | Ezek 31:5 |
| תַּן *tan* (H8565) | a monster (as preternaturally formed), i.e. a sea-serpent (or other huge marine animal); also a jack | Ezek 32:2 |
| רָמוּת *râmûwth* (H7419) | a heap (of carcases) | Ezek 32:5 |
| צָפָה *tsâphâh* (H6824) | an inundation (as covering) | Ezek 32:6 |
| חַד *chad* (H2297) | one | Ezek 33:30 |
| בַּקָּרָה *baqqârâh* (H1243) | a looking after | Ezek 34:12 |
| מִשְׁקָע *mishqâʻ* (H4950) | a settling place (of water), i.e. a pond | Ezek 34:18 |
| מִרְפָּשׂ *mirpâs* (H4833) | muddled water | Ezek 34:19 |
| בְּרִי *bᵉrîy* (H1274) | fat | Ezek 34:20 |
| רִאשָׁה *riʼshâh* (H7221) | a beginning | Ezek 36:11 |
| הַלֵּזוּ *hallêzûw* (H1977) | that | Ezek 36:35 |
| הֲמוֹנָה *Hămôwnâh* (H1997) | Hamonah | Ezek 39:16 |
| שָׁשָׁא *shâshâʼ* (H8338) | to annihilate | Ezek 39:2 |
| מִבְנֶה *mibneh* (H4011) | a building | Ezek 40:2 |
| בִּנְיָה *binyâh* (H1140) | a structure | Ezek 41:13 |
| שָׁחִיף *shâchîyph* (H7824) | a board (as chipped thin) | Ezek 41:16 |
| מוּסָב *mûwçâb* (H4141) | a turn, i.e. circuit (of a building) | Ezek 41:7 |
| מְיֻסָּדָה *mᵉyuççâdâh* (H4328) | something founded, i.e. a foundation | Ezek 41:8 |
| הָגִין *hâgîyn* (H1903) | perhaps suitable or turning | Ezek 42:12 |
| הַרְאֵל *harʼêl* (H2025) | mount of God; figuratively, the altar of burnt-offering | Ezek 43:15 |
| יֶזַע *yezaʻ* (H3154) | sweat, i.e. (by implication) a sweating dress | Ezek 44:18 |
| שָׁשָׁה *shâshâh* (H8341) | to sixth or divide into sixths | Ezek 45:13 |
| גְרֻשָׁה *gᵉrushâh* (H1646) | (abstractly) dispossession | Ezek 45:9 |
| רָסַס *râçaç* (H7450) | to moisten (with drops) | Ezek 46:14 |
| קָטַר *qâṭar* (H7000) | to inclose | Ezek 46:22 |
| מְבַשְּׁלָה *mᵉbashshᵉlâh* (H4018) | a cooking hearth | Ezek 46:23 |
| תְּרוּפָה *tᵉrûwphâh* (H8644) | a remedy | Ezek 47:12 |
| גֵּה *gêh* (H1454) | this | Ezek 47:13 |
| סִבְרַיִם *Çibrayim* (H5453) | Sibrajim, a place in Syria | Ezek 47:16 |
| פָּכָה *pâkâh* (H6379) | to pour | Ezek 47:2 |
| שָׂחוּ *sâchûw* (H7813) | a pond (for swimming) | Ezek 47:5 |
| קַדְמוֹן *qadmôwn* (H6930) | eastern | Ezek 47:8 |
| תְּרוּמִיָּה *tᵉrûwmîyâh* (H8642) | a sacrificial offering | Ezek 48:12 |
| מִשְׁקוֹל *mishqôwl* (H4946) | weight | Ezek 4:10 |
| עוּג *ʻûwg* (H5746) | to bake (round cakes on the hearth) | Ezek 4:12 |
| דֹּחַן *dôchan* (H1764) | millet | Ezek 4:9 |
| גַּלָּב *gallâb* (H1532) | a barber | Ezek 5:1 |
| גְּדוּפָה *gᵉdûwphâh* (H1422) | a revilement | Ezek 5:15 |
| דִּבְלָה *Diblâh* (H1689) | Diblah, a place in Syria | Ezek 6:14 |
| הֵם *hêm* (H1991) | abundance, i.e. wealth | Ezek 7:11 |
| נֹהַּ *nôahh* (H5089) | lamentation | Ezek 7:11 |
| תָּקוֹעַ *tâqôwaʻ* (H8619) | a trumpet | Ezek 7:14 |
| רַתּוֹק *rattôwq* (H7569) | a chain | Ezek 7:23 |
| קְפָדָה *qᵉphâdâh* (H7089) | shrinking, i.e., terror | Ezek 7:25 |
| הֵד *hêd* (H1906) | a shout | Ezek 7:7 |
| תַּמּוּז *Tammûwz* (H8542) | Tammuz, a Phoenician deity | Ezek 8:14 |
| בְּאָה *bᵉʼâh* (H872) | an entrance to a building | Ezek 8:5 |
| מַשְׁחֵת *mashchêth* (H4892) | destruction | Ezek 9:1 |
| מַפָּץ *mappâts* (H4660) | a smiting to pieces | Ezek 9:2 |
| מֻטֶּה *muṭṭeh* (H4297) | a stretching, i.e. distortion (figuratively, iniquity) | Ezek 9:9 |
| בֶּכֶה *bekeh* (H1059) | a weeping | Ezra 10:1 |
| יַחְזְיָה *Yachzᵉyâh* (H3167) | Jachzejah, an Israelite | Ezra 10:15 |
| קֵלָיָה *Qêlâyâh* (H7041) | Kelajah, an Israelite | Ezra 10:23 |
| רַמְיָה *Ramyâh* (H7422) | Ramjah, an Israelite | Ezra 10:25 |
| יִזִּיָּה *Yizzîyâh* (H3150) | Jizzijah, an Israelite | Ezra 10:25 |
| עֲזִיזָא *ʻĂzîyzâʼ* (H5819) | Aziza, an Israelite | Ezra 10:27 |
| עַתְלַי *ʻAthlay* (H6270) | Athlai, an Israelite | Ezra 10:28 |
| שְׁאָל *Shᵉʼâl* (H7594) | Sheal, an Israelite | Ezra 10:29 |
| כְּלָל *Kᵉlâl* (H3636) | Kelal, an Israelite | Ezra 10:30 |
| מַתַּתָּה *Mattattâh* (H4992) | Mattattah, an Israelite | Ezra 10:33 |
| יְרֵמַי *Yᵉrêmay* (H3413) | Jeremai, an Israelite | Ezra 10:33 |
| מַעֲדַי *Maʻăday* (H4572) | Maadai, an Israelite | Ezra 10:34 |
| אוּאֵל *ʼÛwʼêl* (H177) | Uel, and Israelite | Ezra 10:34 |
| בֵּדְיָה *Bêdᵉyâh* (H912) | Bedejah, an Israelite | Ezra 10:35 |
| וַנְיָה *Vanyâh* (H2057) | Vanjah, an Israelite | Ezra 10:36 |
| מַכְנַדְבַי *Maknadbay* (H4367) | Maknadbai, an Israelite | Ezra 10:40 |
| שָׁשַׁי *Shâshay* (H8343) | Shashai, an Israelite | Ezra 10:40 |
| שָׁרַי *Shâray* (H8298) | Sharay, an Israelite | Ezra 10:40 |
| זְבִינָא *Zᵉbîynâʼ* (H2081) | Zebina, an Israelite | Ezra 10:43 |
| גִּזְבָּר *gizbâr* (H1489) | treasurer | Ezra 1:8 |
| מַחֲלָף *machălâph* (H4252) | a (sacrificial) knife (as gliding through the flesh) | Ezra 1:9 |
| יוֹרָה *Yôwrâh* (H3139) | Jorah, an Israelite | Ezra 2:18 |
| רְעֵלָיָה *Rᵉʻêlâyâh* (H7480) | Reelajah, an Israelite | Ezra 2:2 |
| מִסְפָּר *Miçpâr* (H4558) | Mispar, an Israelite | Ezra 2:2 |
| גִּבָּר *Gibbâr* (H1402) | Gibbar, an Israelite | Ezra 2:20 |
| מַגְבִּישׁ *Magbîysh* (H4019) | Magbish, an Israelite, or a place in Palestine | Ezra 2:30 |
| חָגָב *Châgâb* (H2285) | Chagab, one of the Nethinim | Ezra 2:46 |
| שַׁמְלַי *Shamlay* (H8073) | Shamlai, one of the Nethinim | Ezra 2:46 |
| אַסְנָה *ʼAçnâh* (H619) | Asnah, one of the Nethinim | Ezra 2:50 |
| אָמִי *ʼÂmîy* (H532) | Ami, an Israelite | Ezra 2:57 |
| אַדָּן *ʼAddân* (H135) | Addan, an Israelite | Ezra 2:59 |
| רִשְׁיוֹן *rishyôwn* (H7558) | a permit | Ezra 3:7 |
| אׇסְנַפַּר *ʼOçnappar* (H620, Aram.) | Osnappar, an Assyrian king | Ezra 4:10 |
| לְוָת *lᵉvâth* (H3890, Aram.) | properly, adhesion, i.e. (as preposition) with | Ezra 4:12 |
| חוּט *chûwṭ* (H2338, Aram.) | to string together, i.e. (figuratively) to repair | Ezra 4:12 |
| אַפְּתֹם *ʼappᵉthôm* (H674, Aram.) | revenue; others at the last | Ezra 4:13 |
| מְלַח *mᵉlach* (H4415, Aram.) | to eat salt, i.e. (generally) subsist | Ezra 4:14 |
| עַרְוָה *ʻarvâh* (H6173, Aram.) | nakedness, i.e. (figuratively) impoverishment | Ezra 4:14 |
| אֲרַךְ *ʼărak* (H749, Aram.) | to suit | Ezra 4:14 |
| חֲרַב *chărab* (H2718, Aram.) | to demolish | Ezra 4:15 |
| פְּרַשׁ *pᵉrash* (H6568, Aram.) | to specify | Ezra 4:18 |
| מְרַד *mᵉrad* (H4776, Aram.) | rebellion | Ezra 4:19 |
| זְהַר *zᵉhar* (H2095, Aram.) | (passively) be admonished | Ezra 4:22 |
| בְּהִילוּ *bᵉhîylûw* (H924, Aram.) | a hurry; only adverb, hastily | Ezra 4:23 |
| אֶדְרָע *ʼedrâʻ* (H153, Aram.) | an arm, i.e. (figuratively) power | Ezra 4:23 |
| בָּלַהּ *bâlahh* (H1089) | to palpitate; hence, (causatively) to terrify | Ezra 4:4 |
| שִׂטְנָה *siṭnâh* (H7855) | opposition (by letter) | Ezra 4:6 |
| בִּשְׁלָם *Bishlâm* (H1312) | Bishlam, a Persian | Ezra 4:7 |
| תִּרְגַּם *tirgam* (H8638) | to transfer, i.e. translate | Ezra 4:7 |
| דִּינַי *Dîynay* (H1784, Aram.) | a Dinaite or inhabitant of some unknown Assyria province | Ezra 4:9 |
| טַרְפְּלַי *Ṭarpᵉlay* (H2967, Aram.) | a Tarpelite (collectively) or inhabitants of Tarpel, a place in Assyria | Ezra 4:9 |
| אֲפָרְסַי *ʼĂphârᵉçay* (H670, Aram.) | an Apherasite or inhabitant of an unknown region of Assyria | Ezra 4:9 |
| בַּבְלִי *Bablîy* (H896, Aram.) | a Babylonian | Ezra 4:9 |
| שׁוּשַׁנְכִי *Shûwshankîy* (H7801, Aram.) | a Shushankite (collectively) or inhabitants of some unknown place in Assyrian | Ezra 4:9 |
| דַּהֲוָא *Dahăvâʼ* (H1723, Aram.) | Dahava, a people colonized in Samaria | Ezra 4:9 |
| עַלְמִי *ʻAlmîy* (H5962, Aram.) | an Elamite or inhabitant of Elam | Ezra 4:9 |
| נְבָא *nᵉbâʼ* (H5013, Aram.) | to prophesy, i.e. speak (or sing) by inspiration (in prediction or simple discourse) to prophesy, i. | Ezra 5:1 |
| רְגַז *rᵉgaz* (H7265, Aram.) | to quiver (with any violent emotion, especially anger or fear) | Ezra 5:12 |
| זְרֻבָּבֶל *Zᵉrubbâbel* (H2217, Aram.) | Zerubbabel, an Israelite | Ezra 5:2 |
| שְׁאַלְתִּיאֵל *Shᵉʼaltîyʼêl* (H7598, Aram.) | Shealtiel, an Israelite | Ezra 5:2 |
| יֵשׁוּעַ *Yêshûwaʻ* (H3443, Aram.) | Jeshua, the name of ten Israelites, also of a place in Palestine | Ezra 5:2 |
| סְעַד *çᵉʻad* (H5583, Aram.) | to aid | Ezra 5:2 |
| בִּנְיָן *binyân* (H1147, Aram.) | an edifice | Ezra 5:4 |
| נְסַח *nᵉçach* (H5256, Aram.) | to tear away | Ezra 6:11 |
| זְקַף *zᵉqaph* (H2211, Aram.) | to hang, i.e. impale | Ezra 6:11 |
| מְגַר *mᵉgar* (H4049, Aram.) | to overthrow | Ezra 6:12 |
| נְבוּאָה *nᵉbûwʼâh* (H5017, Aram.) | inspired teaching | Ezra 6:14 |
| יְצָא *yᵉtsâʼ* (H3319, Aram.) | to go (causatively, bring) out, in a great variety of applications, literally and figuratively, dire | Ezra 6:15 |
| אֲדָר *ʼĂdâr* (H144, Aram.) | Adar, the 12th Hebrew month | Ezra 6:15 |
| חֶדְוָה *chedvâh* (H2305, Aram.) | rejoicing | Ezra 6:16 |
| צְפִיר *tsᵉphîyr* (H6841, Aram.) | a he-goat | Ezra 6:17 |
| עֵז *ʻêz* (H5796, Aram.) | a she-goat (as strong), but masculine in plural (which also is used elliptically for goat's hair) | Ezra 6:17 |
| חֲטָּיָא *chăṭṭâyâʼ* (H2409, Aram.) | an expiation | Ezra 6:17 |
| חַטָּאָה *chaṭṭâʼâh* (H2402, Aram.) | an offence, and the penalty or sacrifice forit | Ezra 6:17 |
| מִנְיָן *minyân* (H4510, Aram.) | enumeration | Ezra 6:17 |
| שְׁבַט *shᵉbaṭ* (H7625, Aram.) | a clan | Ezra 6:17 |
| פְּלֻגָּה *pᵉluggâh* (H6392, Aram.) | a section | Ezra 6:18 |
| מַחְלְקָה *machlᵉqâh* (H4255, Aram.) | a section (of the Levites) | Ezra 6:18 |
| מֹשֶׁה *Môsheh* (H4873, Aram.) | Mosheh, the Israelite lawgiver | Ezra 6:18 |
| אַחְמְתָא *ʼAchmᵉthâʼ* (H307, Aram.) | Achmetha (i.e. Ecbatana), the summer capital of Persia | Ezra 6:2 |
| בִּירָא *bîyrâʼ* (H1001, Aram.) | a palace | Ezra 6:2 |
| מְגִלָּה *mᵉgillâh* (H4040, Aram.) | a roll | Ezra 6:2 |
| דְּבַח *dᵉbach* (H1684, Aram.) | to sacrifice (an animal) | Ezra 6:3 |
| דְּבַח *dᵉbach* (H1685, Aram.) | a sacrifice | Ezra 6:3 |
| סְבַל *çᵉbal* (H5446, Aram.) | to erect | Ezra 6:3 |
| חֲדָת *chădâth* (H2323, Aram.) | new | Ezra 6:4 |
| רַחִיק *rachîyq* (H7352, Aram.) | remote, literally or figuratively, of place or time; specifically, precious; often used adverbially  | Ezra 6:6 |
| עֲלָה *ʻălâh* (H5928, Aram.) | a holocaust | Ezra 6:9 |
| גְּמַר *gᵉmar* (H1585, Aram.) | to end (in the sense of completion or failure) | Ezra 7:12 |
| מִשְׁכַּן *mishkan* (H4907, Aram.) | residence | Ezra 7:15 |
| קְנָא *qᵉnâʼ* (H7066, Aram.) | to purchase | Ezra 7:17 |
| נְסַךְ *nᵉçak* (H5261, Aram.) | a libation | Ezra 7:17 |
| מַדְבַּח *madbach* (H4056, Aram.) | a sacrificial altar | Ezra 7:17 |
| יְטַב *yᵉṭab* (H3191, Aram.) | to be (causative) make well, literally (sound, beautiful) or figuratively (happy, successful, right) | Ezra 7:18 |
| פׇּלְחָן *polchân* (H6402, Aram.) | worship | Ezra 7:19 |
| חַשְׁחוּת *chashchûwth* (H2819, Aram.) | necessity | Ezra 7:20 |
| גִּזְבָּר *gizbâr* (H1490, Aram.) | treasurer | Ezra 7:21 |
| כִּכֵּר *kikkêr* (H3604, Aram.) | a talent | Ezra 7:22 |
| אַדְרַזְדָּא *ʼadrazdâʼ* (H149, Aram.) | quickly or carefully | Ezra 7:23 |
| קְצַף *qᵉtsaph* (H7109, Aram.) | rage | Ezra 7:23 |
| זַמָּר *zammâr* (H2171, Aram.) | an instrumental musician | Ezra 7:24 |
| תָּרָע *târâʻ* (H8652, Aram.) | a doorkeeper | Ezra 7:24 |
| נְתִין *Nᵉthîyn* (H5412, Aram.) | the Nethinim, or Temple-servants (as given to that duty) | Ezra 7:24 |
| שְׁפַט *shᵉphaṭ* (H8200, Aram.) | to judge | Ezra 7:25 |
| דַּיָּן *dayân* (H1782, Aram.) | a judge or advocate | Ezra 7:25 |
| מוֹת *môwth* (H4193, Aram.) | death | Ezra 7:26 |
| עֲנַשׁ *ʻănash* (H6065, Aram.) | a mulct | Ezra 7:26 |
| יְסֻד *yᵉçud* (H3246) | a foundation (figuratively, i.e. beginning) | Ezra 7:9 |
| יוֹסִפְיָה *Yôwçiphyâh* (H3131) | Josiphjah, an Israelite | Ezra 8:10 |
| קָטָן *Qâṭân* (H6997) | Katan, an Israelite | Ezra 8:12 |
| זַבּוּד *Zabbûwd* (H2072) | Zabbud, an Israelite | Ezra 8:14 |
| צָהַב *tsâhab* (H6668) | to glitter, i.e. be golden in color | Ezra 8:27 |
| תַּעֲנִית *taʻănîyth* (H8589) | affliction (of self), i.e. fasting | Ezra 9:5 |
| אֶרֶךְ *ʼErek* (H751) | Erek, a place in Babylon | Gen 10:10 |
| אַכַּד *ʼAkkad* (H390) | Accad, a place in Babylon | Gen 10:10 |
| רֶסֶן *Reçen* (H7449) | Resen, a place in Assyrian | Gen 10:12 |
| לֶשַׁע *Leshaʻ* (H3962) | Lesha, a place probably East of the Jordan | Gen 10:19 |
| מַשׁ *Mash* (H4851) | Mash, a son of Aram, and the people descended from him | Gen 10:23 |
| עוֹבָל *ʻÔwbâl* (H5745) | Obal, a son of Joktan | Gen 10:28 |
| מֵשָׁא *Mêshâʼ* (H4852) | Mesha, a place in Arabia | Gen 10:30 |
| סְפָר *Çᵉphâr* (H5611) | Sephar, a place in Arabia | Gen 10:30 |
| יִסְכָּה *Yiçkâh* (H3252) | Jiskah, sister of Lot | Gen 11:29 |
| וָלָד *vâlâd* (H2056) | a boy | Gen 11:30 |
| חָנִיךְ *chânîyk* (H2593) | initiated; i.e. practiced | Gen 14:14 |
| חוֹבָה *chôwbâh* (H2327) | Chobah, a place in Syria | Gen 14:15 |
| בֶּרַע *Beraʻ* (H1298) | Bera, a Sodomitish king | Gen 14:2 |
| בִּרְשַׁע *Birshaʻ* (H1306) | Birsha, a king of Gomorrah | Gen 14:2 |
| שִׁנְאָב *Shinʼâb* (H8134) | Shinab, a Canaanite | Gen 14:2 |
| שֶׁמְאֵבֶר *Shemʼêber* (H8038) | Shemeber, a king of Zeboim | Gen 14:2 |
| זוּזִים *Zûwzîym* (H2104) | Zuzites, an aboriginal tribe of Palestine | Gen 14:5 |
| הָם *Hâm* (H1990) | Ham, a region of Palestine | Gen 14:5 |
| קַדְמֹנִי *Qadmônîy* (H6935) | Kadmonite (collectively), the name of a tribe in Palestine | Gen 15:19 |
| מֶשֶׁק *mesheq* (H4943) | possession | Gen 15:2 |
| הֲפֵכָה *hăphêkâh* (H2018) | destruction | Gen 19:29 |
| טָחָה *ṭâchâh* (H2909) | to stretch a bow, as an archer | Gen 21:16 |
| קַשָּׁת *qashshâth* (H7199) | a bowman | Gen 21:20 |
| כֶּשֶׂד *Kesed* (H3777) | Kesed, a relative of Abraham | Gen 22:22 |
| חֲזוֹ *Chăzôw* (H2375) | Chazo, a nephew of Abraham | Gen 22:22 |
| פִּלְדָּשׁ *Pildâsh* (H6394) | Pildash, a relative of Abraham | Gen 22:22 |
| יִדְלָף *Yidlâph* (H3044) | Jidlaph, a Mesopotamian | Gen 22:22 |
| רְאוּמָה *Rᵉʼûwmâh* (H7208) | Reumah, a Syrian woman | Gen 22:24 |
| טֶבַח *Ṭebach* (H2875) | Tebach, the name of a Mesopotamian and of an Israelite | Gen 22:24 |
| גַּחַם *Gacham* (H1514) | Gacham, a son of Nahor | Gen 22:24 |
| תַּחַשׁ *Tachash* (H8477) | Tachash, a relative of Abraham | Gen 22:24 |
| עָקַד *ʻâqad* (H6123) | to tie with thongs | Gen 22:9 |
| שָׁאָה *shâʼâh* (H7583) | to stun, i.e. (intransitively) be astonished | Gen 24:21 |
| שׂוּחַ *sûwach* (H7742) | to muse pensively | Gen 24:63 |
| לְטוּשִׁם *Lᵉṭûwshim* (H3912) | Letushim, an Arabian tribe | Gen 25:3 |
| לְאֻמִּים *Lᵉʼummîym* (H3817) | Leum mim, an Arabian | Gen 25:3 |
| לָעַט *lâʻaṭ* (H3938) | to swallow greedily; causatively, to feed | Gen 25:30 |
| שַׁעַר *shaʻar* (H8180) | a measure (as a section) | Gen 26:12 |
| עֵשֶׂק *ʻêseq* (H6230) | strife | Gen 26:20 |
| עָשַׂק *ʻâsaq* (H6229) | to press upon, i.e. quarrel | Gen 26:20 |
| שִׂטְנָה *Siṭnâh* (H7856) | Sitnah, the name of a well in Pal | Gen 26:21 |
| אֲחֻזַּת *ʼĂchuzzath* (H276) | Achuzzath, a Philistine | Gen 26:26 |
| שִׁבְעָה *Shibʻâh* (H7656) | Shebah, a well in Palestine | Gen 26:33 |
| יְהוּדִית *Yᵉhûwdîyth* (H3067) | Jehudith, a Canaanitess | Gen 26:34 |
| מֹרָה *môrâh* (H4786) | bitterness, i.e. (figuratively) trouble | Gen 26:35 |
| תְּלִי *tᵉlîy* (H8522) | a quiver (as slung) | Gen 27:3 |
| סֻלָּם *çullâm* (H5551) | a stair-case | Gen 28:12 |
| פִּישׁוֹן *Pîyshôwn* (H6376) | Pishon, a river of Eden | Gen 2:11 |
| אֹשֶׁר *ʼôsher* (H837) | happiness | Gen 30:13 |
| זָבַד *zâbad* (H2064) | to confer | Gen 30:20 |
| זֶבֶד *zebed* (H2065) | a gift | Gen 30:20 |
| זָבַל *zâbal* (H2082) | to reside | Gen 30:20 |
| לוּז *lûwz* (H3869) | some kind of nuttree, perhaps the almond | Gen 30:37 |
| פְּצָלָה *pᵉtsâlâh* (H6479) | a peeling | Gen 30:37 |
| מַחְשֹׂף *machsôph* (H4286) | a peeling | Gen 30:37 |
| נַפְתּוּל *naphtûwl* (H5319) | properly, wrestled; but used (in the plural) transitively, a struggle | Gen 30:8 |
| חִתָּה *chittâh* (H2847) | fear | Gen 35:5 |
| הֵימָם *Hêymâm* (H1967) | Hemam, an Idumaean | Gen 36:22 |
| יֵם *yêm* (H3222) | a warm spring | Gen 36:24 |
| חֶמְדָּן *Chemdân* (H2533) | Chemdan, an Idumaean | Gen 36:26 |
| עָקָן *ʻÂqân* (H6130) | Akan, an Idummaean | Gen 36:27 |
| הֲדַר *Hădar* (H1924) | Hadar, an Edomite | Gen 36:39 |
| מְדָנִי *Mᵉdânîy* (H4092) | a Midjanite or descendant (native) of Midjan | Gen 37:36 |
| חֹתֶמֶת *chôthemeth* (H2858) | a seal | Gen 38:25 |
| כְּזִיב *Kᵉzîyb* (H3580) | Kezib, a place in Palestine | Gen 38:5 |
| זֵעָה *zêʻâh* (H2188) | perspiration | Gen 3:19 |
| שָׂחַט *sâchaṭ* (H7818) | to tread out, i.e. squeeze (grapes) | Gen 40:11 |
| חֹרִי *chôrîy* (H2751) | white bread | Gen 40:16 |
| צָנַם *tsânam* (H6798) | to blast or shrink | Gen 41:23 |
| חָמַשׁ *châmash* (H2567) | to tax a fifth | Gen 41:34 |
| אַבְרֵךְ *ʼabrêk* (H86) | kneel | Gen 41:43 |
| זִמְרָה *zimrâh* (H2173) | pruned (i.e. choice) fruit | Gen 43:11 |
| בֹּטֶן *bôṭen* (H992) | (only in plural) a pistachio-nut (from its form) | Gen 43:11 |
| מִשְׁגֶּה *mishgeh* (H4870) | an error | Gen 43:12 |
| צְעִירָה *tsᵉʻîyrâh* (H6812) | smallness (of age), i.e. juvenility | Gen 43:33 |
| טָעַן *ṭâʻan* (H2943) | to load a beast | Gen 45:17 |
| יוֹב *Yôwb* (H3102) | Job, an Israelite | Gen 46:13 |
| צִפְיוֹן *Tsiphyôwn* (H6837) | Tsiphjon, an Israelite | Gen 46:16 |
| אֵחִי *ʼÊchîy* (H278) | Echi, an Israelite | Gen 46:21 |
| רֹאשׁ *Rôʼsh* (H7220) | Rosh, the name of an Israelite and of a foreign nation | Gen 46:21 |
| מֻפִּים *Muppîym* (H4649) | Muppim, an Israelite | Gen 46:21 |
| חֹמֶשׁ *chômesh* (H2569) | a fifth tax | Gen 47:26 |
| זֹקֶן *zôqen* (H2207) | old age | Gen 48:10 |
| דָּגָה *dâgâh* (H1711) | to spawn, i.e. become numerous | Gen 48:16 |
| חַכְלִיל *chaklîyl* (H2447) | darkly flashing (only of the eyes); in a good sense, brilliant (as stimulated by wine) | Gen 49:12 |
| שְׁפִיפֹן *shᵉphîyphôn* (H8207) | a kind of serpent (as snapping), probably the cerastes or horned adder | Gen 49:17 |
| שֶׁפֶר *shepher* (H8233) | beauty | Gen 49:21 |
| תַּאֲוָה *taʼăvâh* (H8379) | a limit, i.e. full extent | Gen 49:26 |
| פַּחַז *pachaz* (H6349) | ebullition, i.e. froth (figuratively, lust) | Gen 49:4 |
| מְכֵרָה *mᵉkêrâh* (H4380) | a sword | Gen 49:5 |
| נוֹד *Nôwd* (H5113) | Nod, the land of Cain | Gen 4:16 |
| יָבָל *Yâbâl* (H2989) | Jabal, an antediluvian | Gen 4:20 |
| יוּבַל *Yûwbal* (H3106) | Jubal, an antediluvian | Gen 4:21 |
| בְּכִית *bᵉkîyth* (H1068) | a weeping | Gen 50:4 |
| גֹּפֶר *gôpher* (H1613) | a kind of tree or wood (as used for building), apparently the cypress | Gen 6:14 |
| טָרָף *ṭârâph* (H2965) | recently torn off, i.e. fresh | Gen 8:11 |
| קֹר *qôr* (H7120) | cold | Gen 8:22 |
| מִשְׂחַק *mischaq* (H4890) | a laughing-stock | Hab 1:10 |
| טְהוֹר *ṭᵉhôwr* (H2890) | purity | Hab 1:13 |
| עָקַל *ʻâqal* (H6127) | to wrest | Hab 1:4 |
| מְגַמָּה *mᵉgammâh* (H4041) | properly, accumulation, i.e. impulse or direction | Hab 1:9 |
| כָּפִיס *kâphîyç* (H3714) | a girder | Hab 2:11 |
| מָעוֹר *mâʻôwr* (H4589) | nakedness, i.e. (in plural) the pudenda | Hab 2:15 |
| קִיקָלוֹן *qîyqâlôwn* (H7022) | intense disgrace | Hab 2:16 |
| עַבְטִיט *ʻabṭîyṭ* (H5671) | something pledged, i.e. (collectively) pawned goods | Hab 2:6 |
| רוֹם *rôwm* (H7315) | elevation, i.e. (adverbially) aloft | Hab 3:10 |
| עֲלִיצוּת *ʻălîytsûwth* (H5951) | exultation | Hab 3:14 |
| רֶפֶת *repheth* (H7517) | a stall for cattle (from their resting there) | Hab 3:17 |
| חֶבְיוֹן *chebyôwn* (H2253) | a concealment | Hab 3:4 |
| מוּד *mûwd* (H4128) | to shake | Hab 3:6 |
| כּוּשָׁן *Kûwshân* (H3572) | Cushan, a region of Arabia | Hab 3:7 |
| עוּר *ʻûwr* (H5783) | to (be) bare | Hab 3:9 |
| מַלְאֲכוּת *malʼăkûwth* (H4400) | a message | Hag 1:13 |
| שַׁלְמַן *Shalman* (H8020) | Shalman, a king apparently of Assyria | Hos 10:14 |
| בׇּשְׁנָה *boshnâh* (H1317) | shamefulness | Hos 10:6 |
| עַלְוָה *ʻalvâh* (H5932) | moral perverseness | Hos 10:9 |
| תִּרְגַּל *tirgal* (H8637) | to cause to walk | Hos 11:3 |
| רְתֵת *rᵉthêth* (H7578) | terror | Hos 13:1 |
| קֹטֶב *qôṭeb* (H6987) | extermination | Hos 13:14 |
| נֹחַם *nôcham* (H5164) | ruefulness, i.e. desistance | Hos 13:14 |
| פָּרָא *pârâʼ* (H6500) | to bear fruit | Hos 13:15 |
| תַּלְאוּבָה *talʼûwbâh* (H8514) | desiccation | Hos 13:5 |
| דִּבְלַיִם *Diblayim* (H1691) | Diblajim, a symbolic name | Hos 1:3 |
| נַבְלוּת *nablûwth* (H5040) | properly, disgrace, i.e. the (female) pudenda | Hos 2:12 |
| אֶתְנָה *ʼethnâh* (H866) | a present (as the price of harlotry) | Hos 2:14 |
| חֶלְיָה *chelyâh* (H2484) | a trinket | Hos 2:15 |
| בַּעֲלִי *Baʻălîy* (H1180) | Baali, a symbolical name for Jehovah | Hos 2:18 |
| נַאֲפוּף *naʼăphûwph* (H5005) | adultery | Hos 2:4 |
| לֶתֶךְ *lethek* (H3963) | a measure for things dry | Hos 3:2 |
| גָּהָה *gâhâh* (H1455) | to remove (a bandage from a wound, i.e. heal it) | Hos 5:13 |
| שֵׂט *sêṭ* (H7846) | a departure from right, i.e. sin | Hos 5:2 |
| זוֹ *zôw* (H2097) | this or that | Hos 7:16 |
| לָצַץ *lâtsats* (H3945) | to deride | Hos 7:5 |
| הַבְהָב *habhâb* (H1890) | gift (in sacrifice), i.e. holocaust | Hos 8:13 |
| שָׁבָב *shâbâb* (H7616) | a fragment, i.e. ruin | Hos 8:6 |
| צָמַק *tsâmaq* (H6784) | to dry up | Hos 9:14 |
| מֹף *Môph* (H4644) | Moph, the capital of Lower Egypt | Hos 9:6 |
| יָקוֹשׁ *yâqôwsh* (H3352) | properly, entangling; hence, a snarer | Hos 9:8 |
| מַשּׂוֹר *massôwr* (H4883) | a saw | Isa 10:15 |
| נָסַס *nâçaç* (H5263) | to wane, i.e. be sick | Isa 10:18 |
| תַּבְלִית *tablîyth* (H8399) | consumption | Isa 10:25 |
| מַדְמֵנָה *Madmênâh* (H4088) | Madmenah, a place in Palestine | Isa 10:31 |
| גֵּבִים *Gêbîym* (H1374) | Gebim, a place in Palestine | Isa 10:31 |
| סָעַף *çâʻaph* (H5586) | to disbranch (a tree) | Isa 10:33 |
| מַעֲרָצָה *maʻărâtsâh* (H4637) | violence | Isa 10:33 |
| מִשְׁמָע *mishmâʻ* (H4926) | a report | Isa 11:3 |
| מְאוּרָה *mᵉʼûwrâh* (H3975) | something lighted, i.e. an aperture; by implication, a crevice or hole (of a serpent) | Isa 11:8 |
| הָדָה *hâdâh* (H1911) | to stretch forth the hand | Isa 11:8 |
| אֹחַ *ʼôach* (H255) | a howler or lonesome wild animal | Isa 13:21 |
| הֶמְיָה *hemyâh* (H1998) | sound | Isa 14:11 |
| הֵילֵל *hêylêl* (H1966) | the morning-star | Isa 14:12 |
| טָעַן *ṭâʻan* (H2944) | to stab | Isa 14:19 |
| מַטְבֵּחַ *maṭbêach* (H4293) | slaughter | Isa 14:21 |
| טוּא *ṭûwʼ* (H2894) | to sweep away | Isa 14:23 |
| מַטְאֲטֵא *maṭʼăṭêʼ* (H4292) | a broom (as removing dirt (compare English 'to dust', i.e. remove dust)) | Isa 14:23 |
| מוֹעָד *môwʻâd* (H4151) | properly, an assembly  figuratively, a troop | Isa 14:31 |
| מַדְהֵבָה *madhêbâh* (H4062) | goldmaking, i.e. exactness | Isa 14:4 |
| מֻרְדָּף *murdâph* (H4783) | persecuted | Isa 14:6 |
| בַּיִת *Bayith* (H1006) | Bajith, a place in Palestine | Isa 15:2 |
| אֶגְלַיִם *ʼEglayim* (H97) | Eglajim, a place in Moab | Isa 15:8 |
| פְּלִילָה *pᵉlîylâh* (H6415) | justice | Isa 16:3 |
| מוּץ *mûwts* (H4160) | to press, i.e. (figuratively) to oppress | Isa 16:4 |
| גֵּא *gêʼ* (H1341) | haughty | Isa 16:6 |
| אָשִׁישׁ *ʼâshîysh* (H808) | a (ruined) foundation | Isa 16:7 |
| שָׂרוּק *sârûwq* (H8291) | a grapevine | Isa 16:8 |
| שִׁלֻּחָה *shilluchâh* (H7976) | a shoot | Isa 16:8 |
| מְעִי *mᵉʻîy* (H4596) | a pile of rubbish (as contorted), i.e. a ruin | Isa 17:1 |
| נַעֲמָן *naʻămân* (H5282) | pleasantness (plural as concrete) | Isa 17:10 |
| שׂוּג *sûwg* (H7735) | to hedge in | Isa 17:11 |
| גַּרְגַּר *gargar* (H1620) | a berry (as if a pellet of rumination) | Isa 17:6 |
| זַלְזַל *zalzal* (H2150) | tremulous, i.e. a twig | Isa 18:5 |
| תָּזַז *tâzaz* (H8456) | to lop off | Isa 18:5 |
| קוּץ *qûwts* (H6972) | to spend the harvest season | Isa 18:6 |
| אָגֵם *ʼâgêm* (H99) | figuratively, sad | Isa 19:10 |
| עַוְעֶה *ʻavʻeh* (H5773) | perversity | Isa 19:14 |
| חָגָא *châgâʼ* (H2283) | properly, vertigo, i.e. (figuratively) fear | Isa 19:17 |
| הֶרֶס *hereç* (H2041) | demolition | Isa 19:18 |
| עָרָה *ʻârâh* (H6169) | a naked (i.e. level) plot | Isa 19:7 |
| מִזְרָע *mizrâʻ* (H4218) | a planted field | Isa 19:7 |
| שְׂרִיקָה *sᵉrîyqâh* (H8305) | hetchelling (or combing flax), i.e. (concretely) tow (by extension, linen cloth) | Isa 19:9 |
| חוֹר *chôwr* (H2355) | white linen | Isa 19:9 |
| חָמוֹץ *châmôwts* (H2541) | properly, violent; by implication, a robber | Isa 1:17 |
| מָהַל *mâhal* (H4107) | properly, to cut down or reduce, i.e. by implication, to adulterate | Isa 1:22 |
| שַׁלְמֹן *shalmôn* (H8021) | a bribe | Isa 1:23 |
| נִיצוֹץ *nîytsôwts* (H5213) | a spark | Isa 1:31 |
| מִקְשָׁה *miqshâh* (H4750) | literally a cucumbered field, i.e. a cucumber patch | Isa 1:8 |
| סַרְגּוֹן *Çargôwn* (H5623) | Sargon, an Assyrian king | Isa 20:1 |
| מְדֻשָּׁה *mᵉdushshâh* (H4098) | a threshing, i.e. (concretely and figuratively) down-trodden people | Isa 21:10 |
| דְּדָנִים *Dᵉdânîym* (H1720) | Dedanites, the descendants or inhabitants of Dedan | Isa 21:13 |
| צָפִית *tsâphîyth* (H6844) | a sentry | Isa 21:5 |
| מִקְוָה *miqvâh* (H4724) | a collection, i.e. (of water) a reservoir | Isa 22:11 |
| טַלְטֵלָה *ṭalṭêlâh* (H2925) | overthrow or rejection | Isa 22:17 |
| צְנֵפָה *tsᵉnêphâh* (H6802) | a ball | Isa 22:18 |
| צְפִעָה *tsᵉphiʻâh* (H6849) | an outcast thing | Isa 22:24 |
| חָסַן *châçan* (H2630) | properly, to (be) compact; by implication, to hoard | Isa 23:18 |
| עָתִיק *ʻâthîyq* (H6266) | properly, antique, i.e. venerable or splendid | Isa 23:18 |
| שְׁאִיָּה *shᵉʼîyâh* (H7591) | desolation | Isa 24:12 |
| אֲסֵפָה *ʼăçêphâh* (H626) | a collection of people (only adverbial) | Isa 24:22 |
| אֹמֶן *ʼômen* (H544) | verity | Isa 25:1 |
| מַתְבֵּן *mathbên* (H4963) | straw in the heap | Isa 25:10 |
| מַדְמֵנָה *madmênâh* (H4087) | a dunghill | Isa 25:10 |
| אׇרֳבָה *ʼorŏbâh* (H698) | ambuscades | Isa 25:11 |
| לוֹט *lôwṭ* (H3875) | a veil | Isa 25:7 |
| נָסַךְ *nâçak* (H5259) | to interweave, i.e. (figuratively) to overspread | Isa 25:7 |
| עֲקַלָּתוֹן *ʻăqallâthôwn* (H6129) | tortuous | Isa 27:1 |
| פָּשַׂע *pâsaʻ* (H6585) | to stride (from spreading the legs), i.e. rush upon | Isa 27:4 |
| צוּת *tsûwth* (H6702) | to blaze | Isa 27:4 |
| סַאסְּאָה *çaʼçᵉʼâh* (H5432) | measurement, i.e. moderation | Isa 27:8 |
| גִּר *gir* (H1615) | lime (from being burned in a kiln) | Isa 27:9 |
| מַרְגֵּעָה *margêʻâh* (H4774) | rest | Isa 28:12 |
| בֹּחַן *bôchan* (H976) | trial | Isa 28:16 |
| יָעָה *yâʻâh* (H3261) | to brush aside | Isa 28:17 |
| מַצָּע *matstsâʻ* (H4702) | a couch | Isa 28:20 |
| פְּרָצִים *pᵉrâtsîym* (H6559) | Peratsim, a mountain in Palestine | Isa 28:21 |
| שׂוֹרָה *sôwrâh* (H7795) | properly, a ring, i.e. (by analogy) a row (adverbially) | Isa 28:25 |
| סָמַן *çâman* (H5567) | to designate | Isa 28:25 |
| אָדַשׁ *ʼâdash* (H156) | to tread out (grain) | Isa 28:28 |
| גִּלְגָּל *gilgâl* (H1536) | a wheel; by analogy, a whirlwind; also dust (as whirled) | Isa 28:28 |
| צִיצָה *tsîytsâh* (H6733) | a flower | Isa 28:4 |
| פְּלִילִיָּה *pᵉlîylîyâh* (H6417) | judicature | Isa 28:7 |
| הֹפֶךְ *hôphek* (H2017) | an upset, i.e. (abstract) perversity | Isa 29:16 |
| קוֹשׁ *qôwsh* (H6983) | to set a trap | Isa 29:21 |
| חָוַר *châvar* (H2357) | to blanch (as with shame) | Isa 29:22 |
| מֻצָּב *mutstsâb* (H4674) | a station, i.e. military post | Isa 29:3 |
| שְׂכִיָּה *sᵉkîyâh* (H7914) | a conspicuous object | Isa 2:16 |
| מְחִלָּה *mᵉchillâh* (H4247) | a cavern (as if excavated) | Isa 2:19 |
| חֲפֹר *chăphôr* (H2661) | a burrower, i.e. probably a rat | Isa 2:20 |
| פֵּרָה *pêrâh* (H6512) | a hole (as broken, i.e. dug) | Isa 2:20 |
| מַהֲתַלָּה *mahăthallâh* (H4123) | a delusion | Isa 30:10 |
| מְכִתָּה *mᵉkittâh* (H4386) | a fracture | Isa 30:14 |
| שׁוּבָה *shûwbâh* (H7729) | a return | Isa 30:15 |
| בִּטְחָה *biṭchâh* (H985) | trust | Isa 30:15 |
| כָּנַף *kânaph* (H3670) | properly, to project laterally, i.e. probably (reflexive) to withdraw | Isa 30:20 |
| אָמַן *ʼâman* (H541) | to take the right hand road | Isa 30:21 |
| חָמִיץ *châmîyts* (H2548) | seasoned, i.e. salt provender | Isa 30:24 |
| רַחַת *rachath* (H7371) | a winnowing-fork (as blowing the chaff away) | Isa 30:24 |
| מַחַץ *machats* (H4273) | a contusion | Isa 30:26 |
| מַשָּׂאָה *massâʼâh* (H4858) | a conflagration (from the rising of smoke) | Isa 30:27 |
| חָסוּת *châçûwth* (H2622) | confidence | Isa 30:3 |
| נֶפֶץ *nephets* (H5311) | a storm (as dispersing) | Isa 30:30 |
| תׇּפְתֶּה *Tophteh* (H8613) | Tophteh, a place of cremation | Isa 30:33 |
| חָנֵס *Chânêç* (H2609) | Chanes, a place in Egypt | Isa 30:4 |
| דַּבֶּשֶׁת *dabbesheth* (H1707) | a sticky mass, i.e. the hump of acamel | Isa 30:6 |
| כֶּחָשׁ *kechâsh* (H3586) | faithless | Isa 30:9 |
| בַּחַן *bachan* (H975) | a watch-tower | Isa 32:14 |
| בָּרַד *bârad* (H1258) | to hail | Isa 32:19 |
| שִׁפְלָה *shiphlâh* (H8218) | depression | Isa 32:19 |
| עִלֵּג *ʻillêg* (H5926) | stuttering | Isa 32:4 |
| חֹנֶף *chôneph* (H2612) | moral filth, i.e. wickedness | Isa 32:6 |
| נָלָה *nâlâh* (H5239) | to complete | Isa 33:1 |
| יָעַז *yâʻaz* (H3267) | to be bold or obstinate | Isa 33:19 |
| צָעַן *tsâʻan* (H6813) | to load up (beasts), i.e. to migrate | Isa 33:20 |
| רֹמֵמֻת *rômêmuth* (H7427) | exaltation | Isa 33:3 |
| מַשָּׁק *mashshâq* (H4944) | a traversing, i.e. rapid motion | Isa 33:4 |
| גֵּב *gêb* (H1357) | a locust (from its cutting) | Isa 33:4 |
| אֶרְאֵל *ʼerʼêl* (H691) | a hero (collectively) | Isa 33:7 |
| חָצִיר *châtsîyr* (H2681) | a court or abode | Isa 34:13 |
| לִילִית *lîylîyth* (H3917) | a night spectre | Isa 34:14 |
| קִפּוֹז *qippôwz* (H7091) | spring forward; an arrow-snake (as darting on its prey) | Isa 34:15 |
| מַסְלוּל *maçlûwl* (H4547) | a thoroughfare (as turnpiked) | Isa 35:8 |
| חֶרֶא *chereʼ* (H2716) | excrement | Isa 36:12 |
| חֶדֶל *chedel* (H2309) | rest, i.e. the state of the dead | Isa 38:11 |
| קָפַד *qâphad* (H7088) | to contract, i.e. roll together | Isa 38:12 |
| עׇשְׁקָה *ʻoshqâh* (H6234) | anguish | Isa 38:14 |
| מָרַח *mârach* (H4799) | properly, to soften by rubbing or pressure; hence (medicinally) to apply as an emollient | Isa 38:21 |
| שָׂקַר *sâqar* (H8265) | to ogle, i.e. blink coquettishly | Isa 3:16 |
| טָפַף *ṭâphaph* (H2952) | to trip (with short steps) coquettishly | Isa 3:16 |
| עָכַס *ʻâkaç* (H5913) | to put on anklets | Isa 3:16 |
| שָׁבִיס *shâbîyç* (H7636) | a netting for the hair | Isa 3:18 |
| שֵׁרָה *shêrâh* (H8285) | a wrist-band (as compact or clasping) | Isa 3:19 |
| רַעֲלָה *raʻălâh* (H7479) | a long veil (as fluttering) | Isa 3:19 |
| מַעֲטָפָה *maʻăṭâphâh* (H4595) | a cloak | Isa 3:22 |
| נִקְפָּה *niqpâh* (H5364) | probably a rope (as encircling) | Isa 3:24 |
| מִקְשֶׁה *miqsheh* (H4748) | something turned (rounded), i.e. a curl (of tresses) | Isa 3:24 |
| פְּתִיגִיל *pᵉthîygîyl* (H6614) | probably a figured mantle forholidays | Isa 3:24 |
| מַחֲגֹרֶת *machăgôreth* (H4228) | a girdle | Isa 3:24 |
| כִּי *kîy* (H3587) | a brand or scar | Isa 3:24 |
| הַכָּרָה *hakkârâh* (H1971) | respect, i.e. partiality | Isa 3:9 |
| טְלָא *ṭᵉlâʼ* (H2922) | a lamb | Isa 40:11 |
| מַר *mar* (H4752) | a drop | Isa 40:15 |
| רְתֻקָה *rᵉthuqâh* (H7577) | something fastened, i.e. a chain | Isa 40:19 |
| דֹּק *dôq* (H1852) | something crumbling, i.e. fine (as a thin cloth) | Isa 40:22 |
| מָתַח *mâthach* (H4969) | to stretch out | Isa 40:22 |
| רֶכֶס *rekeç* (H7406) | a mountain ridge (as of tied summits) | Isa 40:4 |
| מַצּוּת *matstsûwth* (H4695) | a quarrel | Isa 41:12 |
| עַצֻּמָה *ʻatstsumâh* (H6110) | a bulwark, i.e. (figuratively) argument | Isa 41:21 |
| אֵפַע *ʼêphaʻ* (H659) | properly, a breath, i.e. nothing | Isa 41:24 |
| צָוַח *tsâvach* (H6681) | to screech (exultingly) | Isa 42:11 |
| פָּעָה *pâʻâh* (H6463) | to scream | Isa 42:14 |
| נָשַׁם *nâsham* (H5395) | properly, to blow away, i.e. destroy | Isa 42:14 |
| מַעֲקָשׁ *maʻăqâsh* (H4625) | a crook (in a road) | Isa 42:16 |
| פָּחַח *pâchach* (H6351) | to spread a net | Isa 42:22 |
| מְשׁוּסָה *mᵉshûwçâh* (H4882) | spoilation | Isa 42:24 |
| שֶׂרֶד *sered* (H8279) | a (carpenter's) scribing-awl (for pricking or scratching measurements) | Isa 44:13 |
| מַקְצֻעָה *maqtsuʻâh* (H4741) | a scraper, i.e. a carving chisel | Isa 44:13 |
| מְחוּגָה *mᵉchûwgâh* (H4230) | an instrument for marking a circle, i.e. compasses | Isa 44:13 |
| תִּרְזָה *tirzâh* (H8645) | a species of tree (apparently from its slenderness), perhaps the cypress | Isa 44:14 |
| אֹרֶן *ʼôren* (H766) | the ash tree (from its toughness) | Isa 44:14 |
| צוּלָה *tsûwlâh* (H6683) | an abyss (of the sea) | Isa 44:27 |
| רָהָה *râhâh* (H7297) | to fear | Isa 44:8 |
| סְבָאִי *Çᵉbâʼîy* (H5436) | a Sebaite, or inhabitant of Seba | Isa 45:14 |
| נְשׂוּאָה *nᵉsûwʼâh* (H5385) | something borne, i.e. a load | Isa 46:1 |
| אִישׁ *ʼîysh* (H377) | to be a man, i.e. act in amanly way | Isa 46:8 |
| שֹׁבֶל *shôbel* (H7640) | a lady's train (as trailing after her) | Isa 47:2 |
| עָדִין *ʻâdîyn* (H5719) | voluptuous | Isa 47:8 |
| אַלְמֹן *ʼalmôn* (H489) | bereavement | Isa 47:9 |
| מֵעָה *mêʻâh* (H4579) | the belly, i.e. (figuratively) interior | Isa 48:19 |
| חָטַם *châṭam* (H2413) | to stop | Isa 48:9 |
| סִינִים *Çîynîym* (H5515) | Sinim, a distant Oriental region | Isa 49:12 |
| הֲרִיסוּת *hărîyçûwth* (H2035) | demolition | Isa 49:19 |
| שִׁכֻּלִים *shikkulîym* (H7923) | childlessness (by continued bereavements) | Isa 49:20 |
| נָצִיר *nâtsîyr* (H5336) | properly, conservative; but used passively, delivered | Isa 49:6 |
| בָּזֹה *bâzôh* (H960) | scorned | Isa 49:7 |
| מִסְתּוֹר *miçtôwr* (H4563) | a refuge | Isa 4:6 |
| מַעֲצֵבָה *maʻătsêbâh* (H4620) | anguish | Isa 50:11 |
| קַדְרוּת *qadrûwth* (H6940) | duskiness | Isa 50:3 |
| עוּת *ʻûwth* (H5790) | to hasten, i.e. succor | Isa 50:4 |
| סָס *çâç* (H5580) | a moth (from the agility of the fly) | Isa 51:8 |
| יוֹנֵק *yôwnêq* (H3126) | a sucker; hence, a twig (of a tree felled and sprouting) | Isa 53:2 |
| מַסְתֵּר *maçtêr* (H4564) | properly, a hider, i.e. (abstractly) a hiding, i.e. aversion | Isa 53:3 |
| אֶקְדָּח *ʼeqdâch* (H688) | burning, i.e. a carbuncle or other fiery gem | Isa 54:12 |
| שֶׁצֶף *shetseph* (H8241) | an outburst (of anger) | Isa 54:8 |
| סַרְפָּד *çarpâd* (H5636) | a nettle (as stinging like a burn) | Isa 55:13 |
| נָבַח *nâbach* (H5024) | to bark (as a dog) | Isa 56:10 |
| הָזָה *hâzâh* (H1957) | to dream | Isa 56:10 |
| קִבּוּץ *qibbûwts* (H6899) | a throng | Isa 57:13 |
| רֶפֶשׁ *rephesh* (H7516) | mud (as roiled) | Isa 57:20 |
| חַלָּק *challâq* (H2511) | smooth | Isa 57:6 |
| רַקֻּחַ *raqquach* (H7547) | a scented substance | Isa 57:9 |
| צַחְצָחָה *tsachtsâchâh* (H6710) | a dry place, i.e. desert | Isa 58:11 |
| עָצֵב *ʻâtsêb* (H6092) | a (hired) workman | Isa 58:3 |
| אַשְׁמָן *ʼashmân* (H820) | a fat-field | Isa 59:10 |
| תַּלְבֹּשֶׁת *talbôsheth* (H8516) | a garment | Isa 59:17 |
| זוּרֶה *zûwreh* (H2116) | trodden on | Isa 59:5 |
| נְגֹהָה *nᵉgôhâh* (H5054) | splendor | Isa 59:9 |
| צִחֶה *tsicheh* (H6704) | parched | Isa 5:13 |
| עָלֵז *ʻâlêz* (H5938) | exultant | Isa 5:14 |
| עָזַק *ʻâzaq* (H5823) | to grub over | Isa 5:2 |
| סוּחָה *çûwchâh* (H5478) | something swept away, i.e. filth | Isa 5:25 |
| עָרִיף *ʻârîyph* (H6183) | the sky (as dropping at the horizon) | Isa 5:30 |
| בָּתָה *bâthâh* (H1326) | desolation | Isa 5:6 |
| מִשְׂפָּח *mispâch* (H4939) | slaughter | Isa 5:7 |
| זֶרַח *zerach* (H2225) | a rising of light | Isa 60:3 |
| בֶּכֶר *beker* (H1070) | a young camel | Isa 60:6 |
| יָעַט *yâʻaṭ* (H3271) | to clothe | Isa 61:10 |
| מַעֲטֶה *maʻăṭeh* (H4594) | a vestment | Isa 61:3 |
| יָמַר *yâmar* (H3235) | to exchange; by implication, to change places | Isa 61:6 |
| הָמָס *hâmâç* (H2003) | a dry twig or brushwood | Isa 64:1 |
| עֵד *ʻêd* (H5708) | the menstrual flux (as periodical); by implication (in plural) soiling | Isa 64:5 |
| גַּד *Gad* (H1408) | Fortune, a Babylonian deity | Isa 65:11 |
| מְנִי *Mᵉnîy* (H4507) | the Apportioner, i.e. Fate (as an idol) | Isa 65:11 |
| פָּרָק *pârâq* (H6564) | soup (as full of crumbed meat) | Isa 65:4 |
| מָצַץ *mâtsats* (H4711) | to suck | Isa 66:11 |
| כַּרְכָּרָה *karkârâh* (H3753) | a dromedary (from its rapid motion as if dancing) | Isa 66:20 |
| עֲזוּבָה *ʻăzûwbâh* (H5805) | desertion (of inhabitants) | Isa 6:12 |
| שַׁלֶּכֶת *shalleketh* (H7995) | a felling (of trees) | Isa 6:13 |
| בַּתָּה *battâh* (H1327) | desolation | Isa 7:19 |
| נַהֲלֹל *nahălôl* (H5097) | pasture | Isa 7:19 |
| שְׂכִירָה *sᵉkîyrâh* (H7917) | a hiring | Isa 7:20 |
| מַעְדֵּר *maʻdêr* (H4576) | a (weeding) hoe | Isa 7:25 |
| יְבֶרֶכְיָהוּ *Yᵉberekyâhûw* (H3000) | Jeberekjah, an Israelite | Isa 8:2 |
| מָעוּף *mâʻûwph* (H4588) | darkness | Isa 8:22 |
| מוּעָף *mûwʻâph* (H4155) | properly, covered, i.e. dark; abstractly, obscurity, i.e. distress | Isa 8:23 |
| מֻטָּה *muṭṭâh* (H4298) | expansion | Isa 8:8 |
| אָבַךְ *ʼâbak* (H55) | probably to coil upward | Isa 9:17 |
| עָתַם *ʻâtham* (H6272) | probably to glow, i.e. (figuratively) be desolated | Isa 9:18 |
| סְאוֹן *çᵉʼôwn* (H5430) | perhaps a military boot (as aprotection from mud | Isa 9:4 |
| סָאַן *çâʼan* (H5431) | to shoe, i.e. (active participle) a soldier shod | Isa 9:4 |
| אֲרַק *ʼăraq* (H778, Aram.) | the earth | Jer 10:11 |
| אֵלֶּה *ʼêlleh* (H429, Aram.) | these or those | Jer 10:11 |
| כִּנְעָה *kinʻâh* (H3666) | a package | Jer 10:17 |
| יָאָה *yâʼâh* (H2969) | to be suitable | Jer 10:7 |
| כָּסַל *kâçal* (H3688) | properly, to be fat, i.e. (figuratively) silly | Jer 10:8 |
| יְדִדוּת *yᵉdidûwth* (H3033) | properly, affection; concretely, a darling object | Jer 12:7 |
| צָבוּעַ *tsâbûwaʻ* (H6641) | dyed (in stripes), i.e. the hyena | Jer 12:9 |
| מֵאֵן *mêʼên* (H3987) | refractory | Jer 13:10 |
| מַרְאָשָׁה *marʼâshâh* (H4761) | properly, headship, i.e. (plural for collective) dominion | Jer 13:18 |
| חֲבַרְבֻּרָה *chăbarburâh* (H2272) | a streak (like a line), as on the tiger | Jer 13:23 |
| אֱלוּל *ʼĕlûwl* (H434) | good for nothing | Jer 14:14 |
| גָּשַׁם *gâsham* (H1652) | to shower violently | Jer 14:22 |
| דָּהַם *dâham* (H1724) | to be dumb, i.e. (figuratively) dumbfounded | Jer 14:9 |
| שֵׁרוּת *shêrûwth* (H8293) | freedom | Jer 15:11 |
| שָׁרָה *shârâh* (H8281) | to free | Jer 15:11 |
| חֲנִינָה *chănîynâh* (H2594) | graciousness | Jer 16:13 |
| דִּיג *dîyg* (H1770) | to fish | Jer 16:16 |
| צַיָּד *tsayâd* (H6719) | a huntsman | Jer 16:16 |
| מַרְזֵחַ *marzêach* (H4798) | a cry, i.e. (of grief) a lamentation | Jer 16:5 |
| יָסוּר *yâçûwr* (H3249) | departing | Jer 17:13 |
| חָרֵר *chârêr* (H2788) | arid | Jer 17:6 |
| יוּבַל *yûwbal* (H3105) | a stream | Jer 17:8 |
| מְרֻצָה *mᵉrutsâh* (H4835) | oppression | Jer 22:17 |
| עָשׁוֹק *ʻâshôwq* (H6216) | oppressive (as noun, a tyrant) | Jer 22:3 |
| חֲנֻפָה *chănuphâh* (H2613) | impiety | Jer 23:15 |
| נָאַם *nâʼam* (H5001) | properly, to whisper, i.e. (by implication) to utter as aoracle | Jer 23:31 |
| פַּחֲזוּת *pachăzûwth* (H6350) | frivolity | Jer 23:32 |
| כְּלִמּוּת *kᵉlimmûwth* (H3640) | disgrace | Jer 23:40 |
| בַּכֻּרָה *bakkurâh* (H1073) | a first-ripe fig | Jer 24:2 |
| רִאשֹׁנִי *riʼshônîy* (H7224) | first | Jer 25:1 |
| קָיָה *qâyâh* (H7006) | to vomit | Jer 25:27 |
| תְּפוֹצָה *tᵉphôwtsâh* (H8600) | a dispersal | Jer 25:34 |
| כַּשָּׁף *kashshâph* (H3786) | a magician | Jer 27:9 |
| שֹׁעָר *shôʻâr* (H8182) | harsh or horrid, i.e. offensive | Jer 29:17 |
| צִינֹק *tsîynôq* (H6729) | the pillory | Jer 29:26 |
| פַּחְדָּה *pachdâh* (H6345) | alarm (i.e. awe) | Jer 2:19 |
| כְּלוּלָה *kᵉlûwlâh* (H3623) | bridehood (only in the plural) | Jer 2:2 |
| סוּר *çûwr* (H5494) | turned off, i.e. deteriorated | Jer 2:21 |
| כָּתַם *kâtham* (H3799) | properly, to carve or engrave, i.e. (by implication) to inscribe indelibly | Jer 2:22 |
| בִּכְרָה *bikrâh* (H1072) | a young she-camel | Jer 2:23 |
| שָׂרַךְ *sârak* (H8308) | to interlace | Jer 2:23 |
| צִמְאָה *tsimʼâh* (H6773) | thirst (figuratively, of libidinousnes) | Jer 2:25 |
| מַאְפֵלְיָה *maʼphêlᵉyâh* (H3991) | opaqueness | Jer 2:31 |
| שָׁאַס *shâʼaç* (H7601) | to plunder | Jer 30:16 |
| יַקִּיר *yaqqîyr* (H3357) | precious | Jer 31:20 |
| תַּמְרוּר *tamrûwr* (H8564) | an erection, i.e. pillar (probably for a guide-board) | Jer 31:21 |
| גֹּעָה *Gôʻâh* (H1601) | Goah, a place near Jerusalem | Jer 31:39 |
| שְׁרֵמָה *shᵉrêmâh* (H8309) | a common | Jer 31:40 |
| עֲלִילִיָּה *ʻălîylîyâh* (H5950) | (miraculous) execution | Jer 32:19 |
| עֲתֶרֶת *ʻăthereth* (H6283) | copiousness | Jer 33:6 |
| חֲבַצַּנְיָה *Chăbatstsanyâh* (H2262) | Chabatstsanjah, a Rechabite | Jer 35:3 |
| יִגְדַּלְיָהוּ *Yigdalyâhûw* (H3012) | Jigdaljah, an Israelite | Jer 35:4 |
| דְּיוֹ *dᵉyôw* (H1773) | ink | Jer 36:18 |
| עַבְדְּאֵל *ʻAbdᵉʼêl* (H5655) | Abdeel, an Israelite | Jer 36:26 |
| פְּקִדֻת *pᵉqiduth* (H6488) | supervision | Jer 37:13 |
| חָנוּת *chânûwth* (H2588) | properly, a vault or cell (with an arch); by implication, a prison | Jer 37:16 |
| יְהוּכַל *Yᵉhûwkal* (H3081) | Jehukal, an Israelite | Jer 37:3 |
| יוּכַל *Yûwkal* (H3116) | Jukal, an Israelite | Jer 38:1 |
| בֹץ *bôts* (H1206) | mud (as whitish clay) | Jer 38:22 |
| יָגֵב *yâgêb* (H3010) | a plowed field | Jer 39:10 |
| נְבוּשַׁזְבָּן *Nᵉbûwshazbân* (H5021) | Nebushazban, Nebuchadnezzar's chief eunuch | Jer 39:13 |
| בַּעֲלִיס *Baʻălîyç* (H1185) | Baalis, an Ammonitish king | Jer 40:14 |
| גֵּרוּת *gêrûwth* (H1628) | a (temporary) residence | Jer 41:17 |
| אֲנוּ *ʼănûw* (H580) | we | Jer 42:6 |
| מֶלֶט *meleṭ* (H4423) | cement (from its plastic smoothness) | Jer 43:9 |
| קִטֵּר *qiṭṭêr* (H7002) | perfume | Jer 44:21 |
| קֶרֶץ *qerets* (H7171) | extirpation (as if by constriction) | Jer 46:20 |
| שַׁעֲטָה *shaʻăṭâh* (H8161) | a clatter (of hoofs) | Jer 47:3 |
| רִפְיוֹן *riphyôwn* (H7510) | slackness | Jer 47:3 |
| מַדְמֵן *Madmên* (H4086) | Madmen, a place in Palestine | Jer 48:2 |
| גְּדוּד *gᵉdûwd* (H1417) | a furrow (as cut) | Jer 48:37 |
| נִיס *nîyç* (H5211) | fugitive | Jer 48:44 |
| נָצָא *nâtsâʼ* (H5323) | to go away | Jer 48:9 |
| תִּפְלֶצֶת *tiphletseth* (H8606) | fearfulness | Jer 49:16 |
| רֶטֶט *reṭeṭ* (H7374) | terror | Jer 49:24 |
| יָפַח *yâphach* (H3306) | properly, to breathe hard, i.e. (by implication) to sigh | Jer 4:31 |
| עָיֵף *ʻâyêph* (H5888) | to languish | Jer 4:31 |
| סֹבֶךְ *çôbek* (H5441) | a copse | Jer 4:7 |
| מְרֹדָךְ *Mᵉrôdâk* (H4781) | Merodak, a Babylonian idol | Jer 50:2 |
| מְרָתַיִם *Mᵉrâthayim* (H4850) | Merathajim, an epithet of Babylon | Jer 50:21 |
| מַאֲבוּס *maʼăbûwç* (H3965) | a granary | Jer 50:26 |
| מַפֵּץ *mappêts* (H4661) | a smiter, i.e. a war club | Jer 51:20 |
| מִנִּי *Minnîy* (H4508) | Minni, an Armenian province | Jer 51:27 |
| סָמָר *çâmâr* (H5569) | bristling, i.e. shaggy | Jer 51:27 |
| כְּרֵשׂ *kᵉrês* (H3770) | the paunch or belly (as swelling out) | Jer 51:34 |
| נָעַר *nâʻar* (H5286) | to growl | Jer 51:38 |
| אַלְמָן *ʼalmân* (H488) | discarded (as a divorced person) | Jer 51:5 |
| אָמוֹן *ʼâmôwn* (H527) | a throng of people | Jer 52:15 |
| יָגַב *yâgab* (H3009) | to dig or plow | Jer 52:16 |
| שָׁרָה *shârâh* (H8284) | a fortification (literally or figuratively) | Jer 5:10 |
| זוּן *zûwn* (H2109) | perhaps properly, to be plump, i.e. (transitively) to nourish | Jer 5:8 |
| שָׁכָה *shâkâh* (H7904) | to roam (through lust) | Jer 5:8 |
| מַרְגּוֹעַ *margôwaʻ* (H4771) | a resting place | Jer 6:16 |
| בָּחוֹן *bâchôwn* (H969) | an assayer or metals | Jer 6:27 |
| מַפֻּחַ *mappuach* (H4647) | the bellows (i.e. blower) of aforge | Jer 6:29 |
| אֶשָּׁה *ʼeshshâh* (H800) | fire | Jer 6:29 |
| עֵצָה *ʻêtsâh* (H6097) | timber | Jer 6:6 |
| סַלְסִלָּה *çalçillâh* (H5552) | a twig (as pendulous) | Jer 6:9 |
| מַבְלִיגִית *mablîygîyth* (H4010) | desistance (or rather desolation) | Jer 8:18 |
| אֹרֶב *ʼôreb* (H696) | ambuscade | Jer 9:7 |
| נָקַט *nâqaṭ* (H5354) | to loathe | Job 10:1 |
| גְּבִנָה *gᵉbinâh* (H1385) | curdled milk | Job 10:10 |
| רָאֶה *râʼeh* (H7202) | seeing, i.e. experiencing | Job 10:15 |
| סֶדֶר *çeder* (H5468) | order | Job 10:22 |
| מַפָּח *mappâch* (H4646) | a breathing out (of life), i.e. expiring | Job 11:20 |
| עַשְׁתּוּת *ʻashtûwth* (H6248) | cogitation | Job 12:5 |
| בַּטֻּחוֹת *baṭṭuchôwth* (H987) | security | Job 12:6 |
| אַחְוָה *ʼachvâh* (H262) | an utterance | Job 13:17 |
| רָזַם *râzam* (H7335) | to twinkle the eye (in mockery) | Job 15:12 |
| כִּידוֹר *kîydôwr* (H3593) | perhaps tumult | Job 15:24 |
| פִּימָה *pîymâh* (H6371) | obesity | Job 15:27 |
| מִנְלֶה *minleh* (H4512) | completion, i.e. (in produce) wealth | Job 15:29 |
| בֶּסֶר *beçer* (H1154) | an immature grape | Job 15:33 |
| עֲוִיל *ʻăvîyl* (H5760) | perverse (morally) | Job 16:11 |
| מְרֵרָה *mᵉrêrâh* (H4845) | bile (from its bitterness) | Job 16:13 |
| גֶּלֶד *geled* (H1539) | the (human) skin (as smooth) | Job 16:15 |
| שָׂהֵד *sâhêd* (H7717) | a witness | Job 16:19 |
| נִיד *nîyd* (H5205) | motion (of the lips in speech) | Job 16:5 |
| זָעַךְ *zâʻak* (H2193) | to extinguish | Job 17:1 |
| הָתֹל *hâthôl* (H2049) | a derision | Job 17:2 |
| מְשֹׁל *mᵉshôl* (H4914) | a satire | Job 17:6 |
| תֹּפֶת *tôpheth* (H8611) | a smiting, i.e. (figuratively) contempt | Job 17:6 |
| יָצֻר *yâtsur* (H3338) | structure, i.e. limb or part | Job 17:7 |
| אֹמֶץ *ʼômets* (H555) | strength | Job 17:9 |
| מַלְכֹּדֶת *malkôdeth* (H4434) | a snare | Job 18:10 |
| קֶנֶץ *qenets* (H7078) | perversion | Job 18:2 |
| טָמָה *ṭâmâh* (H2933) | to be impure in a religious sense | Job 18:3 |
| שָׁבִיב *shâbîyb* (H7632) | flame (as split into tongues) | Job 18:5 |
| הָכַר *hâkar* (H1970) | to injure | Job 19:3 |
| מְשׁוּגָה *mᵉshûwgâh* (H4879) | mistake | Job 19:4 |
| פְּלַגָּה *pᵉlaggâh* (H6390) | a runlet, i.e. gully | Job 20:17 |
| יָגָע *yâgâʻ* (H3022) | earnings (as the product of toil) | Job 20:18 |
| גֵּוָה *gêvâh* (H1465) | the back, i.e. (by extensive) the person | Job 20:25 |
| שִׂיא *sîyʼ* (H7863) | elevation | Job 20:6 |
| כִּיד *kîyd* (H3589) | a crushing; figuratively, calamity | Job 21:20 |
| שַׁלְאֲנָן *shalʼănân* (H7946) | tranquil | Job 21:23 |
| עֲטִין *ʻăṭîyn* (H5845) | a receptacle (for milk, i.e. pail; figuratively, breast) | Job 21:24 |
| מֹחַ *môach* (H4221) | fat, i.e. marrow | Job 21:24 |
| קִים *qîym* (H7009) | an opponent (as rising against one), i.e. (collectively) enemies | Job 22:20 |
| שַׁח *shach* (H7807) | sunk, i.e. downcast | Job 22:29 |
| אִי *ʼîy* (H336) | not | Job 22:30 |
| תְּכוּנָה *tᵉkûwnâh* (H8499) | something arranged or fixed, i.e. a place | Job 23:3 |
| צָהַר *tsâhar* (H6671) | to press out oil | Job 24:11 |
| מָתָק *mâthâq* (H4988) | a dainty, i.e. (generally) food | Job 24:20 |
| לָקַשׁ *lâqash* (H3953) | to gather the after crop | Job 24:6 |
| רָטַב *râṭab* (H7372) | to be moist | Job 24:8 |
| אָהַל *ʼâhal* (H166) | to be clear | Job 25:5 |
| חוּג *chûwg* (H2328) | to describe a circle | Job 26:10 |
| רוּף *rûwph* (H7322) | properly, to triturate (in a mortar), i.e. (figuratively) to agitate (by concussion) | Job 26:11 |
| שִׁפְרָה *shiphrâh* (H8235) | brightness | Job 26:13 |
| פַּרְשֵׁז *parshêz* (H6576) | to expand | Job 26:9 |
| שָׁלָה *shâlâh* (H7953) | to draw out or off, i.e. remove (the soul by death) | Job 27:8 |
| זְכוּכִית *zᵉkûwkîyth* (H2137) | properly, transparency, i.e. glass | Job 28:17 |
| גָּבִישׁ *gâbîysh* (H1378) | crystal (from its resemblance to ice) | Job 28:18 |
| הָלִיךְ *hâlîyk* (H1978) | a walk, i.e. (by implication) a step | Job 29:6 |
| גָּרַד *gârad* (H1623) | to abrade | Job 2:8 |
| פִּרְחַח *pirchach* (H6526) | progeny, i.e. a brood | Job 30:12 |
| נָתָס *nâthâç* (H5420) | to tear up | Job 30:13 |
| נְדִיבָה *nᵉdîybâh* (H5082) | properly, nobility, i.e. reputation | Job 30:15 |
| שָׁוָה *shâvâh* (H7738) | to destroy | Job 30:22 |
| בְּעִי *bᵉʻîy* (H1164) | a prayer | Job 30:24 |
| עָגַם *ʻâgam* (H5701) | to be sad | Job 30:25 |
| שָׁחַר *shâchar* (H7835) | to be dim or dark (in color) | Job 30:30 |
| מַלּוּחַ *mallûwach* (H4408) | sea-purslain (from its saltness) | Job 30:4 |
| עָרוּץ *ʻârûwts* (H6178) | feared, i.e. (concretely) a horrible place or chasm | Job 30:6 |
| נָכָא *nâkâʼ* (H5217) | to smite, i.e. drive away | Job 30:8 |
| שִׁכְמָה *shikmâh* (H7929) | the shoulderbone | Job 31:22 |
| פְּלִילִי *pᵉlîylîy* (H6416) | judicial | Job 31:28 |
| חֹב *chôb* (H2243) | properly, a cherisher, i.e. the bosom | Job 31:33 |
| בׇּאְשָׁה *boʼshâh* (H890) | stink-weed or any other noxious or useless plant | Job 31:40 |
| מֹסָר *môçâr* (H4561) | admonition | Job 33:16 |
| זָהַם *zâham* (H2092) | to be rancid, i.e. (transitively) to loathe | Job 33:20 |
| פָּדַע *pâdaʻ* (H6308) | to retrieve | Job 33:24 |
| רֻטֲפַשׁ *ruṭăphash* (H7375) | to be rejuvenated | Job 33:25 |
| אֶכֶף *ʼekeph* (H405) | a load; by implication, a stroke (others dignity) | Job 33:7 |
| חַף *chaph* (H2643) | pure | Job 33:9 |
| מַעְבָּד *maʻbâd* (H4566) | an act | Job 34:25 |
| אָבֶה *ʼâbeh* (H15) | longing | Job 34:36 |
| חֶבְרָה *chebrâh* (H2274) | association | Job 34:8 |
| פַּשׁ *pash* (H6580) | stupidity (as a result of grossness or of degeneracy) | Job 35:15 |
| כָּבַר *kâbar* (H3527) | properly, to plait together, i.e. (figuratively) to augment (especially in number or quantity, to ac | Job 35:16 |
| בְּצַר *bᵉtsar* (H1222) | gold | Job 36:19 |
| מַאֲמָץ *maʼămâts* (H3981) | strength, i.e. (plural) resources | Job 36:19 |
| מַכְבִּיר *makbîyr* (H4342) | plenty | Job 36:31 |
| רִי *rîy* (H7377) | irrigation, i.e. a shower | Job 37:11 |
| טָרַח *ṭârach* (H2959) | to overburden | Job 37:11 |
| מִפְלָשׂ *miphlâs* (H4657) | a poising | Job 37:16 |
| מִפְלָאָה *miphlâʼâh* (H4652) | a miracle | Job 37:16 |
| רְאִי *rᵉʼîy* (H7209) | a mirror (as seen) | Job 37:18 |
| בָּהִיר *bâhîyr* (H925) | shining | Job 37:21 |
| מְזָרֶה *mᵉzâreh* (H4215) | properly, a scatterer, i.e. the north wind (as dispersing clouds; only in plural) | Job 37:9 |
| נֵבֶךְ *nêbek* (H5033) | a fountain | Job 38:16 |
| אֶגֶל *ʼegel* (H96) | a reservoir | Job 38:28 |
| מַעֲדַנָּה *maʻădannâh* (H4575) | a bond, i.e. group | Job 38:31 |
| מוֹשְׁכָה *môwshᵉkâh* (H4189) | something drawing, i.e. (figuratively) a cord | Job 38:31 |
| מַזָּרָה *mazzârâh* (H4216) | some noted constellation (only in the plural), perhaps collectively, the zodiac | Job 38:32 |
| מִשְׁטָר *mishṭâr* (H4896) | jurisdiction | Job 38:33 |
| שֶׂכְוִי *sekvîy* (H7907) | observant, i.e. (concretely) the mind | Job 38:36 |
| מֵמַד *mêmad* (H4461) | a measure | Job 38:5 |
| חֲתֻלָּה *chăthullâh* (H2854) | a swathing cloth (figuratively) | Job 38:9 |
| רֶנֶן *renen* (H7443) | an ostrich (from its wail) | Job 39:13 |
| רַעְמָה *raʻmâh* (H7483) | the mane of a horse (as quivering in the wind) | Job 39:19 |
| רָנָה *rânâh* (H7439) | to whiz | Job 39:23 |
| אָבַר *ʼâbar* (H82) | to soar | Job 39:26 |
| עָלַע *ʻâlaʻ* (H5966) | to sip up | Job 39:30 |
| עָרוֹד *ʻârôwd* (H6171) | an onager (from his lonesome habits) | Job 39:5 |
| יָתוּר *yâthûwr* (H3491) | properly, what is left, i.e. (by implication) a gleaning | Job 39:8 |
| יָרוֹק *yârôwq* (H3387) | green, i.e. an herb | Job 39:8 |
| יָגִיעַ *yâgîyaʻ* (H3019) | tired | Job 3:17 |
| נְהָרָה *nᵉhârâh* (H5105) | daylight | Job 3:4 |
| עֲנָנָה *ʻănânâh* (H6053) | cloudiness | Job 3:5 |
| כִּמְרִיר *kimrîyr* (H3650) | obscuration (as if from shrinkage of light, i.e. an eclipse (only in plural) | Job 3:5 |
| הָדַךְ *hâdak* (H1915) | to crush with the foot | Job 40:12 |
| בְּהֵמוֹת *bᵉhêmôwth* (H930) | a water-ox, i.e. the hippopotamus or Nile-horse | Job 40:15 |
| שָׁרִיר *shârîyr* (H8306) | a cord, i.e. (by analogy) sinew | Job 40:16 |
| מְטִיל *mᵉṭîyl* (H4300) | an iron bar (as forged) | Job 40:18 |
| יִסּוֹר *yiççôwr* (H3250) | a reprover | Job 40:2 |
| חַבָּר *chabbâr* (H2271) | a partner | Job 40:30 |
| שֻׂכָּה *sukkâh* (H7905) | a dart (as pointed like a thorn) | Job 40:31 |
| עֲטִישָׁה *ʻăṭîyshâh* (H5846) | sneezing | Job 41:10 |
| כִידוֹד *kîydôwd* (H3590) | properly, something struck off, i.e. a spark (as struck) | Job 41:11 |
| נְחִיר *nᵉchîyr* (H5156) | a nostril | Job 41:12 |
| דּוּץ *dûwts* (H1750) | to leap | Job 41:14 |
| דְּאָבָה *dᵉʼâbâh* (H1670) | properly, pining; by analogy, fear | Job 41:14 |
| רִקָּבוֹן *riqqâbôwn* (H7539) | decay (by caries) | Job 41:19 |
| תּוֹתָח *tôwthâch* (H8455) | a club | Job 41:21 |
| חַדּוּד *chaddûwd* (H2303) | a point | Job 41:22 |
| חִין *chîyn* (H2433) | beauty | Job 41:4 |
| שִׁבְעָנָה *shibʻânâh* (H7658) | seven | Job 42:13 |
| יְמִימָה *Yᵉmîymâh* (H3224) | Jemimah, one of Job's daughters | Job 42:14 |
| קְצִיעָה *Qᵉtsîyʻâh* (H7103) | Ketsiah, a daughter of Job | Job 42:14 |
| נָתַע *nâthaʻ* (H5421) | to tear out | Job 4:10 |
| תׇּהֳלָה *tohŏlâh* (H8417) | braggadocio, i.e. (by implication) fatuity | Job 4:18 |
| עֹרֶם *ʻôrem* (H6193) | a stratagem | Job 5:13 |
| סָלַד *çâlad* (H5539) | probably to leap (with joy), i.e. exult | Job 6:10 |
| נָחוּשׁ *nâchûwsh* (H5153) | coppery, i.e. (figuratively) hard | Job 6:12 |
| מָס *mâç* (H4523) | fainting, i.e. (figuratively) disconsolate | Job 6:14 |
| זָרַב *zârab* (H2215) | to flow away | Job 6:17 |
| הַיָּה *hayâh* (H1962) | ruin | Job 6:2 |
| חֲתַת *chăthath* (H2866) | dismay | Job 6:21 |
| חַלָּמוּת *challâmûwth* (H2495) | probably purslain | Job 6:6 |
| מַחֲנַק *machănaq* (H4267) | choking | Job 7:15 |
| מִפְגָּע *miphgâʻ* (H4645) | an object of attack | Job 7:20 |
| מִדַּד *middad* (H4059) | flight | Job 7:4 |
| נָדֻד *nâdud* (H5076) | properly, tossed; abstractly, a rolling (on the bed) | Job 7:4 |
| קָטַט *qâṭaṭ* (H6990) | to clip off, i.e. (figuratively) destroy | Job 8:14 |
| רָטֹב *râṭôb* (H7373) | moist (with sap) | Job 8:16 |
| חָתַף *châthaph* (H2862) | to clutch | Job 9:12 |
| מַמְרֹר *mamrôr* (H4472) | a bitterness, i.e. (figuratively) calamity | Job 9:18 |
| אֵבֶה *ʼêbeh* (H16) | the papyrus | Job 9:26 |
| טוּשׂ *ṭûws* (H2907) | to pounce as a bird of prey | Job 9:26 |
| פָּלַץ *pâlats* (H6426) | properly, perhaps to rend, i.e. (by implication) to quiver | Job 9:6 |
| פְּתוּאֵל *Pᵉthûwʼêl* (H6602) | Pethuel, an Israelite | Joel 1:1 |
| עָבַשׁ *ʻâbash* (H5685) | to dry up | Joel 1:17 |
| פְּרֻדָה *pᵉrudâh* (H6507) | something separated, i.e. a kernel | Joel 1:17 |
| מִגְרָפָה *migrâphâh* (H4053) | something thrown off (by the spade), i.e. a clod | Joel 1:17 |
| מַמְּגֻרָה *mammᵉgurâh* (H4460) | a granary | Joel 1:17 |
| קְצָפָה *qᵉtsâphâh* (H7111) | a fragment | Joel 1:7 |
| אָלָה *ʼâlâh* (H421) | to bewail | Joel 1:8 |
| צְפוֹנִי *tsᵉphôwnîy* (H6830) | northern | Joel 2:20 |
| צַחֲנָה *tsachănâh* (H6709) | stench | Joel 2:20 |
| חַלָּשׁ *challâsh* (H2523) | frail | Joel 4:10 |
| עוּשׁ *ʻûwsh* (H5789) | to hasten | Joel 4:11 |
| יְוָנִי *Yᵉvânîy* (H3125) | a Jevanite, or descendant of Javan | Joel 4:6 |
| שְׁבָאִי *Shᵉbâʼîy* (H7615) | a Shebaite or descendant of Sheba | Joel 4:8 |
| סְפִינָה *çᵉphîynâh* (H5600) | a (sea-going) vessel (as ceiled with a deck) | Jonah 1:5 |
| קְרִיאָה *qᵉrîyʼâh* (H7150) | a proclamation | Jonah 3:2 |
| חֲרִישִׁי *chărîyshîy* (H2759) | quiet, i.e. sultry (as feminine noun, the sirocco or hot east wind) | Jonah 4:8 |
| שָׂרַד *sârad* (H8277) | properly, to puncture, i.e. (figuratively through the idea of slipping out) to escape or survive | Josh 10:20 |
| הוֹהָם *Hôwhâm* (H1944) | Hoham, a Canaanitish king | Josh 10:3 |
| פִּרְאָם *Pirʼâm* (H6502) | Piram, a Canaanite | Josh 10:3 |
| הֹרָם *Hôrâm* (H2036) | Horam, a Canaanitish king | Josh 10:33 |
| גֶּדֶר *Geder* (H1445) | Geder, a place in Palestine | Josh 12:13 |
| בְּטֹנִים *Bᵉṭônîym* (H993) | Betonim, a place in Palestine | Josh 13:26 |
| צָפוֹן *Tsâphôwn* (H6829) | Tsaphon, a place in Palestine | Josh 13:27 |
| אֶשְׁקְלוֹנִי *ʼEshqᵉlôwnîy* (H832) | Ashkelonite (collectively) or inhabitant of Ashkelon | Josh 13:3 |
| מְעָרָה *Mᵉʻârâh* (H4632) | Mearah, a place in Palestine | Josh 13:4 |
| יְעָרִים *Yᵉʻârîym* (H3297) | Jearim, a place in Palestine | Josh 15:10 |
| כְּסָלוֹן *Kᵉçâlôwn* (H3693) | Kesalon, a place in Palestine | Josh 15:10 |
| שִׁכְּרוֹן *Shikkᵉrôwn* (H7942) | drunkenness, Shikkeron, a place in Palestine | Josh 15:11 |
| יָגוּר *Yâgûwr* (H3017) | Jagur, a place in Palestine | Josh 15:21 |
| קִינָה *Qîynâh* (H7016) | Kinah, a place in Palestine | Josh 15:22 |
| דִּימוֹנָה *Dîymôwnâh* (H1776) | Dimonah, a place in Palestine | Josh 15:22 |
| עֲדְעָדָה *ʻĂdʻâdâh* (H5735) | Adadah, a place in Palestine | Josh 15:22 |
| יִתְנָן *Yithnân* (H3497) | Jithnan, a place in Palestine | Josh 15:23 |
| אֲמָם *ʼĂmâm* (H538) | Amam, a place in Palestine | Josh 15:26 |
| שְׁמָע *Shᵉmâʻ* (H8090) | Shema, a place in Palestine | Josh 15:26 |
| חֶשְׁמוֹן *Cheshmôwn* (H2829) | Cheshmon, a place in Palestine | Josh 15:27 |
| בִּזְיוֹתְיָה *bizyôwthᵉyâh* (H964) | Bizjothjah, a place in Palestine | Josh 15:28 |
| קַרְקַע *Qarqaʻ* (H7173) | Karka (with the article prefix), a place in Palestine | Josh 15:3 |
| כְּסִיל *Kᵉçîyl* (H3686) | Kesil, a place in Palestine | Josh 15:30 |
| סַנְסַנָּה *Çançannâh* (H5578) | Sansannah, a place in Palestine | Josh 15:31 |
| לְבָאוֹת *Lᵉbâʼôwth* (H3822) | Lebaoth, a place in Palestine | Josh 15:32 |
| שִׁלְחִים *Shilchîym* (H7978) | Shilchim, a place in Palestine | Josh 15:32 |
| עֲדִיתַיִם *ʻĂdîythayim* (H5723) | Adithajim, a place in Palestine | Josh 15:36 |
| גְּדֵרָה *Gᵉdêrâh* (H1449) | (with the article) Gederah, a place in Palestine | Josh 15:36 |
| גְּדֵרֹתַיִם *Gᵉdêrôthayim* (H1453) | Gederothajim, a place in Palestine | Josh 15:36 |
| צְנָן *Tsᵉnân* (H6799) | Tsenan, a place near Palestine | Josh 15:37 |
| חֲדָשָׁה *Chădâshâh* (H2322) | Chadashah, a place in Palestine | Josh 15:37 |
| דִּלְעָן *Dilʻân* (H1810) | Dilan, a place in Palestine | Josh 15:38 |
| כַּבּוֹן *Kabbôwn* (H3522) | Cabon, a place in Palestine | Josh 15:40 |
| לַחְמָס *Lachmâç* (H3903) | Lachmam or Lachmas, a place in Palestine | Josh 15:40 |
| כִּתְלִישׁ *Kithlîysh* (H3798) | Kithlish, a place in Palestine | Josh 15:40 |
| נְצִיב *Nᵉtsîyb* (H5334) | Netsib, a place in Palestine | Josh 15:43 |
| דַּנָּה *Dannâh* (H1837) | Dannah, a place in Palestine | Josh 15:49 |
| עָנִים *ʻÂnîym* (H6044) | Anim, a place in Palestine | Josh 15:50 |
| אֲרָב *ʼĂrâb* (H694) | Arab, a place in Palestine | Josh 15:52 |
| אֶשְׁעָן *ʼEshʻân* (H824) | Eshan, a place in Palestine | Josh 15:52 |
| אֲפֵקָה *ʼĂphêqâh* (H664) | Aphekah, a place in Palestine | Josh 15:53 |
| חֻמְטָה *Chumṭâh* (H2547) | Chumtah, a place in Palestine | Josh 15:54 |
| צִיעֹר *Tsîyʻôr* (H6730) | Tsior, a place in Palestine | Josh 15:54 |
| יׇקְדְעָם *Yoqdᵉʻâm* (H3347) | Jokdeam, a place in Palestine | Josh 15:56 |
| חַלְחוּל *Chalchûwl* (H2478) | Chalchul, a place in Palestine | Josh 15:58 |
| מַעֲרָת *Maʻărâth* (H4638) | Maarath, a place in Palestine | Josh 15:59 |
| אֶלְתְּקֹן *ʼEltᵉqôn* (H515) | Eltekon, a place in Palestine | Josh 15:59 |
| מִדִּין *Middîyn* (H4081) | Midjan, a son of Abraham; also his country and (collectively) his descendants | Josh 15:61 |
| סְכָכָה *Çᵉkâkâh* (H5527) | Secacah, a place in Palestine | Josh 15:61 |
| נִבְשָׁן *Nibshân* (H5044) | Nibshan, a place in Palestine | Josh 15:62 |
| יַפְלֵטִי *Yaphlêṭîy* (H3311) | a Japhletite or descendant of Japhlet | Josh 16:3 |
| מִבְדָּלָה *mibdâlâh* (H3995) | a separation, i.e. (concretely) a separate place | Josh 16:9 |
| נֶפֶת *nepheth* (H5316) | a height | Josh 17:11 |
| גְּלִילוֹת *Gᵉlîylôwth* (H1553) | Geliloth, a place in Palestine | Josh 18:17 |
| קְצִיץ *Qᵉtsîyts* (H7104) | Keziz, a valley in Palestine | Josh 18:21 |
| פָּרָה *Pârâh* (H6511) | Parah, a place in Palestine | Josh 18:23 |
| עׇפְנִי *ʻOphnîy* (H6078) | an Ophnite (collectively) or inhabitants of Ophen | Josh 18:24 |
| מֹצָה *Môtsâh* (H4681) | Motsah, a place in Palestine | Josh 18:26 |
| יִרְפְּאֵל *Yirpᵉʼêl* (H3416) | Jirpeel, a place in Palestine | Josh 18:27 |
| תַּרְאֲלָה *Tarʼălâh* (H8634) | Taralah, a place in Palestine | Josh 18:27 |
| אֶלֶף *ʼEleph* (H507) | Eleph, a place in Palestine | Josh 18:28 |
| גִּבְעַת *Gibʻath* (H1394) | Gibath | Josh 18:28 |
| מַרְעֲלָה *Marʻălâh* (H4831) | Maralah, a place in Palestine | Josh 19:11 |
| דַּבֶּשֶׁת *Dabbesheth* (H1708) | Dabbesheth, a place in Palestine | Josh 19:11 |
| נֵעָה *Nêʻâh* (H5269) | Neah, a place in Palestine | Josh 19:13 |
| חַנָּתֹן *Channâthôn* (H2615) | Channathon, a place in Palestine | Josh 19:14 |
| קַטָּת *Qaṭṭâth* (H7005) | Kattath, a place in Palestine | Josh 19:15 |
| יִדְאֲלָה *Yidʼălâh* (H3030) | Jidalah, a place in Palestine | Josh 19:15 |
| כְּסֻלּוֹת *Kᵉçullôwth* (H3694) | Kesulloth, a place in Palestine | Josh 19:18 |
| חֲפָרַיִם *Chăphârayim* (H2663) | Chapharajim, a place in Palestine | Josh 19:19 |
| שִׁיאוֹן *Shîyʼôwn* (H7866) | Shijon, a place in Palestine | Josh 19:19 |
| אֲנָחֲרָת *ʼĂnâchărâth* (H588) | Anacharath, a place in Palestine | Josh 19:19 |
| רַבִּית *Rabbîyth* (H7245) | Rabbith, a place in Palestine | Josh 19:20 |
| אֶבֶץ *ʼEbets* (H77) | Ebets, a place in Palestine | Josh 19:20 |
| רֶמֶת *Remeth* (H7432) | Remeth, a place in Palestine | Josh 19:21 |
| חֲלִי *Chălîy* (H2482) | Chali, a place in Palestine | Josh 19:25 |
| בֶּטֶן *Beṭen* (H991) | Beten. a place in Palestine | Josh 19:25 |
| אַלַּמֶּלֶךְ *ʼAllammelek* (H487) | Allammelek, a place in Palestine | Josh 19:26 |
| עַמְעָד *ʻAmʻâd* (H6008) | Amad, a place in Palestine | Josh 19:26 |
| נְעִיאֵל *Nᵉʻîyʼêl* (H5272) | Neiel, a place in Palestine | Josh 19:27 |
| עֶבְרֹן *ʻEbrôn* (H5683) | Ebron, a place in Palestine | Josh 19:28 |
| בָּלָה *Bâlâh* (H1088) | Balah, a place in Palestine | Josh 19:3 |
| עֻמָּה *ʻUmmâh* (H5981) | Ummah, a place in Palestine | Josh 19:30 |
| חֶלֶף *Cheleph* (H2501) | Cheleph, a place in Palestine | Josh 19:33 |
| אֲדָמִי *ʼĂdâmîy* (H129) | Adami, a place in Palestine | Josh 19:33 |
| נֶקֶב *Neqeb* (H5346) | Nekeb, a place in Palestine | Josh 19:33 |
| לַקּוּם *Laqqûwm* (H3946) | Lakkum, a place in Palestine | Josh 19:33 |
| צִדִּים *Tsiddîym* (H6661) | Tsiddim (with the article), a place in Palestine | Josh 19:35 |
| צֵר *Tsêr* (H6863) | Tser, a place in Palestine | Josh 19:35 |
| רַקַּת *Raqqath* (H7557) | Rakkath, a place in Palestine | Josh 19:35 |
| אֲדָמָה *ʼĂdâmâh* (H128) | Adamah, a place in Palestine | Josh 19:36 |
| יִרְאוֹן *Yirʼôwn* (H3375) | Jiron, a place in Palestine | Josh 19:38 |
| חֳרֵם *Chŏrêm* (H2765) | Chorem, a place in Palestine | Josh 19:38 |
| בְּתוּל *Bᵉthûwl* (H1329) | Bethul (i.e. Bethuel), a place in Palestine | Josh 19:4 |
| יִתְלָה *Yithlâh* (H3494) | Jithlah, a place in Palestine | Josh 19:42 |
| יְהֻד *Yᵉhud* (H3055) | Jehud, a place in Palestine | Josh 19:45 |
| רַקּוֹן *Raqqôwn* (H7542) | Rakkon, a place in Palestine | Josh 19:46 |
| שָׁרוּחֶן *Shârûwchen* (H8287) | Sharuchen, a place in Palestine | Josh 19:6 |
| מוּעָדָה *mûwʻâdâh* (H4152) | an appointed place, i.e. asylum | Josh 20:9 |
| עַלְמוֹן *ʻAlmôwn* (H5960) | Almon, a place in Palestine | Josh 21:18 |
| קִבְצַיִם *Qibtsayim* (H6911) | Kibtsajim, a place in Palestine | Josh 21:22 |
| בְּעֶשְׁתְּרָה *Bᵉʻeshtᵉrâh* (H1203) | Beeshterah, a place East of the Jordan | Josh 21:27 |
| קַרְתָּן *Qartân* (H7178) | Kartan, a place in Palestine | Josh 21:32 |
| קַרְתָּה *Qartâh* (H7177) | Kartah, a place in Palestine | Josh 21:34 |
| דִּמְנָה *Dimnâh* (H1829) | Dimnah, a place in Palestine | Josh 21:35 |
| מֶרֶד *mered* (H4777) | rebellion | Josh 22:22 |
| שֹׁטֵט *shôṭêṭ* (H7850) | to flog; a goad | Josh 23:13 |
| אַלָּה *ʼallâh* (H427) | an oak or other strong tree | Josh 24:26 |
| מַאֲפֵל *maʼăphêl* (H3990) | something opaque | Josh 24:7 |
| שְׁבָרִים *Shᵉbârîym* (H7671) | Shebarim, a place in Palestine | Josh 7:5 |
| צָיַר *tsâyar* (H6737) | to make an errand, i.e. betake oneself | Josh 9:4 |
| קָמוֹן *Qâmôwn* (H7056) | Kamon, a place East of the Jordan | Judg 10:5 |
| פִּרְעָתוֹן *Pirʻâthôwn* (H6552) | Pirathon, a place in Palestine | Judg 12:15 |
| סִבֹּלֶת *çibbôleth* (H5451) | an ear of grain | Judg 12:6 |
| תִּמְנִי *Timnîy* (H8554) | a Timnite or inhabitant of Timnah | Judg 15:6 |
| אָלַץ *ʼâlats* (H509) | to press | Judg 16:16 |
| יָמַשׁ *yâmash* (H3237) | to touch | Judg 16:26 |
| שׂוֹרֵק *Sôwrêq* (H7796) | Sorek, a valley in Palestine | Judg 16:4 |
| עֶצֶר *ʻetser* (H6114) | restraint | Judg 18:7 |
| עָצַל *ʻâtsal* (H6101) | to lean idly, i.e. to be indolent or slack | Judg 18:9 |
| צְפַת *Tsᵉphath* (H6857) | Tsephath, a place in Palestine | Judg 1:17 |
| קִטְרוֹן *Qiṭrôwn* (H7003) | Kitron, a place in Palestine | Judg 1:30 |
| עַכּוֹ *ʻAkkôw* (H5910) | Akko (from its situation on a bay) | Judg 1:31 |
| אַחְלָב *ʼAchlâb* (H303) | Achlab, a place in Palestine | Judg 1:31 |
| חֶלְבָּה *Chelbâh* (H2462) | Chelbah, a place in Palestine | Judg 1:31 |
| אָשֵׁרִי *ʼÂshêrîy* (H843) | an Asherite (collectively) or descendant of Asher | Judg 1:32 |
| חֶרֶס *Chereç* (H2776) | Cheres, a mountain in Palestine | Judg 1:35 |
| מַעֲרֶה *maʻăreh* (H4629) | a nude place, i.e. a common | Judg 20:33 |
| גִּדְעֹם *Gidʻôm* (H1440) | Gidom, a place in Palestine | Judg 20:45 |
| לְבוֹנָה *Lᵉbôwnâh* (H3829) | Lebonah, a place in Palestine | Judg 21:19 |
| פֵּיָה *pêyâh* (H6366) | an edge | Judg 3:16 |
| גֹּמֶד *gômed* (H1574) | properly, a span | Judg 3:16 |
| נִצָּב *nitstsâb* (H5325) | fixed, i.e. a handle | Judg 3:22 |
| פַּרְשְׁדֹן *parshᵉdôn* (H6574) | the crotch (or anus) | Judg 3:22 |
| מִסְדְּרוֹן *miçdᵉrôwn* (H4528) | a colonnade or internal portico (from its rows of pillars) | Judg 3:23 |
| שְׂעִירָה *Sᵉʻîyrâh* (H8167) | Seirah, a place in Palestine | Judg 3:26 |
| מַלְמָד *malmâd* (H4451) | a goad for oxen | Judg 3:31 |
| שְׂמִיכָה *sᵉmîykâh* (H8063) | a run (as sustaining the Oriental sitter) | Judg 4:18 |
| לָאט *lâʼṭ* (H3814) | properly, muffled, i.e. silently | Judg 4:21 |
| לַפִּידוֹת *Lappîydôwth* (H3941) | Lappidoth, the husband of Deborah | Judg 4:4 |
| צָחֹר *tsâchôr* (H6715) | white | Judg 5:10 |
| מַשְׁאָב *mashʼâb* (H4857) | a trough for cattle to drink from | Judg 5:11 |
| מִפְרָץ *miphrâts* (H4664) | a break (in the shore), i.e. a haven | Judg 5:17 |
| גָּרַף *gâraph* (H1640) | to bear off violently | Judg 5:21 |
| קָדוּם *qâdûwm* (H6917) | a pristine hero | Judg 5:21 |
| מֵרוֹז *Mêrôwz* (H4789) | Meroz, a place in Palestine | Judg 5:23 |
| הַלְמוּת *halmûwth* (H1989) | a hammer (or mallet) | Judg 5:26 |
| מָחַק *mâchaq* (H4277) | to crush | Judg 5:26 |
| יָבַב *yâbab* (H2980) | to bawl | Judg 5:28 |
| רַחֲמָה *rachămâh* (H7361) | a maiden | Judg 5:30 |
| לָחֶם *lâchem* (H3901) | battle | Judg 5:8 |
| מִנְהָרָה *minhârâh* (H4492) | properly, a channel or fissure, i.e. (by implication) a cavern | Judg 6:2 |
| צְרֵרָה *Tsᵉrêrâh* (H6888) | Tsererah for Tseredah | Judg 7:22 |
| טַבַּת *Ṭabbath* (H2888) | Tabbath, a place East of the Jordan | Judg 7:22 |
| צָפַר *tsâphar* (H6852) | to skip about, i.e. return | Judg 7:3 |
| קַרְקֹר *Qarqôr* (H7174) | Karkor, a place East of the Jordan | Judg 8:10 |
| מֹתֶק *môtheq* (H4987) | sweetness | Judg 9:11 |
| אֲרוּמָה *ʼĂrûwmâh* (H725) | Arumah, a place in Palestine | Judg 9:41 |
| בְּרִית *Bᵉrîyth* (H1286) | Berith, a Shechemitish deity | Judg 9:46 |
| שָׂקַד *sâqad* (H8244) | to fasten | Lam 1:14 |
| מִשְׁבָּת *mishbâth* (H4868) | cessation, i.e. destruction | Lam 1:7 |
| נִידָה *nîydâh* (H5206) | removal, i.e. exile | Lam 1:8 |
| עוּב *ʻûwb* (H5743) | to be dense or dark, i.e. to becloud | Lam 2:1 |
| מַדּוּחַ *maddûwach* (H4065) | seduction | Lam 2:14 |
| פּוּגָה *pûwgâh* (H6314) | intermission | Lam 2:18 |
| טִפֻּח *ṭippuch* (H2949) | nursing | Lam 2:20 |
| שֹׂךְ *sôk* (H7900) | a booth (as interlaced) | Lam 2:6 |
| פָּשַׁח *pâshach* (H6582) | to tear in pieces | Lam 3:11 |
| כָּפַשׁ *kâphash* (H3728) | to tread down; figuratively, to humiliate | Lam 3:16 |
| יָחִיל *yâchîyl* (H3175) | expectant | Lam 3:26 |
| סְחִי *çᵉchîy* (H5501) | refuse (as swept off) | Lam 3:45 |
| מָאוֹס *mâʼôwç* (H3973) | refuse | Lam 3:45 |
| שֵׁאת *shêʼth* (H7612) | devastation | Lam 3:47 |
| הֲפֻגָה *hăphugâh* (H2014) | relaxation | Lam 3:49 |
| עַוָּתָה *ʻavvâthâh* (H5792) | oppression | Lam 3:59 |
| קִימָה *qîymâh* (H7012) | an arising | Lam 3:63 |
| מַנְגִּינָה *mangîynâh* (H4485) | a satire | Lam 3:63 |
| מְגִנָּה *mᵉginnâh* (H4044) | a covering (in a bad sense), i.e. blindness or obduracy | Lam 3:65 |
| תַּאֲלָה *taʼălâh* (H8381) | an imprecation | Lam 3:65 |
| רַחְמָנִי *rachmânîy* (H7362) | compassionate | Lam 4:10 |
| צְפִיָּה *tsᵉphîyâh* (H6836) | watchfulness | Lam 4:17 |
| סָלָא *çâlâʼ* (H5537) | to suspend in a balance, i.e. weigh | Lam 4:2 |
| צָחַח *tsâchach* (H6705) | to glare, i.e. be dazzling white | Lam 4:7 |
| שְׁחוֹר *shᵉchôwr* (H7815) | dinginess, i.e. perhaps soot | Lam 4:8 |
| צָפַד *tsâphad* (H6821) | to adhere | Lam 4:8 |
| טְחוֹן *ṭᵉchôwn* (H2911) | a hand mill; hence, a millstone | Lam 5:13 |
| דָּאָה *dâʼâh* (H1676) | the kite (from its rapid flight) | Lev 11:14 |
| סׇלְעָם *çolʻâm* (H5556) | a kind of locust (from its destructiveness) | Lev 11:22 |
| חָרְגֹּל *chârᵉgôl* (H2728) | the leaping insect, i.e. a locust | Lev 11:22 |
| חֹלֶד *chôled* (H2467) | a weasel (from its gliding motion) | Lev 11:29 |
| אֲנָקָה *ʼănâqâh* (H604) | some kind of lizard, probably the gecko (from its wail) | Lev 11:30 |
| לְטָאָה *lᵉṭâʼâh* (H3911) | a kind of lizard (from its covert habits) | Lev 11:30 |
| חֹמֶט *chômeṭ* (H2546) | a lizard (as creeping) | Lev 11:30 |
| כִּיר *kîyr* (H3600) | a cooking range (consisting of two parallel stones, across which the boiler is set) | Lev 11:35 |
| דָּוָה *dâvâh* (H1738) | to be sick (as if in menstruation) | Lev 12:2 |
| בֹּהַק *bôhaq* (H933) | white scurf | Lev 13:39 |
| גִּבֵּחַ *gibbêach* (H1371) | bald in the forehead | Lev 13:41 |
| פְּחֶתֶת *pᵉchetheth* (H6356) | a hole (by mildew in a garment) | Lev 13:55 |
| שְׁקַעְרוּרָה *shᵉqaʻrûwrâh* (H8258) | a depression | Lev 14:37 |
| רוּר *rûwr* (H7325) | to slaver (with spittle), i.e. (by analogy) to emit afluid (ulcerous or natural) | Lev 15:3 |
| רָקַק *râqaq* (H7556) | to spit | Lev 15:8 |
| עִתִּי *ʻittîy* (H6261) | timely | Lev 16:21 |
| גְּזֵרָה *gᵉzêrâh* (H1509) | a desert (as separated) | Lev 16:22 |
| שַׁאֲרָה *shaʼărâh* (H7608) | female kindred by blood | Lev 18:17 |
| פֶּרֶט *pereṭ* (H6528) | a stray or single berry | Lev 19:10 |
| חֻפְשָׁה *chuphshâh* (H2668) | liberty (from slavery) | Lev 19:20 |
| בִּקֹּרֶת *biqqôreth* (H1244) | properly, examination, i.e. (by implication) punishment | Lev 19:20 |
| חָפַשׁ *châphash* (H2666) | to spread loose; figuratively, to manumit | Lev 19:20 |
| כְּתֹבֶת *kᵉthôbeth* (H3793) | a letter or other mark branded on the skin | Lev 19:28 |
| קַעֲקַע *qaʻăqaʻ* (H7085) | an incision or gash | Lev 19:28 |
| מֻרְאָה *murʼâh* (H4760) | something conspicuous, i.e. the craw of abird (from its prominence) | Lev 1:16 |
| גִּבֵּן *gibbên* (H1384) | hunch-backed | Lev 21:20 |
| תְּבַּלֻּל *tᵉballul* (H8400) | a cataract (in the eye) | Lev 21:20 |
| מְרוֹחַ *mᵉrôwach* (H4790) | bruised, i.e. emasculated | Lev 21:20 |
| אֶשֶׁךְ *ʼeshek* (H810) | a testicle (as a lump) | Lev 21:20 |
| יַבֵּל *yabbêl* (H2990) | having running sores | Lev 22:22 |
| קָלַט *qâlaṭ* (H7038) | to maim | Lev 22:23 |
| דִּבְרִי *Dibrîy* (H1704) | Dibri, an Israelite | Lev 24:11 |
| מִמְכֶּרֶת *mimkereth* (H4466) | a sale | Lev 25:42 |
| עֵקֶר *ʻêqer* (H6133) | figuratively, a transplanted person, i.e. naturalized citizen | Lev 25:47 |
| קוֹמְמִיּוּת *qôwmᵉmîyûwth* (H6968) | elevation, i.e. (adverbially) erectly (figuratively) | Lev 26:13 |
| דּוּב *dûwb* (H1727) | to mope, i.e. (figuratively) pine | Lev 26:16 |
| מֹרֶךְ *môrek* (H4816) | softness, i.e. (figuratively) fear | Lev 26:36 |
| תְּקוּמָה *tᵉqûwmâh* (H8617) | resistfulness | Lev 26:37 |
| דַּיִשׁ *dayish* (H1786) | threshing-time | Lev 26:5 |
| מַאֲפֶה *maʼăpheh* (H3989) | something baked, i.e. a batch | Lev 2:4 |
| פָּתַת *pâthath* (H6626) | to open, i.e. break | Lev 2:6 |
| עָצֶה *ʻâtseh* (H6096) | the spine (as giving firmness to the body) | Lev 3:9 |
| תְּשׂוּמֶת *tᵉsûwmeth* (H8667) | a deposit, i.e. pledging | Lev 5:21 |
| כִּשְׂבָּה *kisbâh* (H3776) | a young ewe | Lev 5:6 |
| תֻּפִין *tuphîyn* (H8601) | cookery, i.e. (concretely) a cake | Lev 6:14 |
| מוֹקְדָה *môwqᵉdâh* (H4169) | fuel | Lev 6:2 |
| מַלְאָכִי *Malʼâkîy* (H4401) | Malaki, a prophet | Mal 1:1 |
| מַתְּלָאָה *mattᵉlâʼâh* (H4972) | what a trouble! | Mal 1:13 |
| חֲבֶרֶת *chăbereth* (H2278) | a consort | Mal 2:14 |
| קְדֹרַנִּית *qᵉdôrannîyth* (H6941) | blackish ones (i.e. in sackcloth); used adverbially, in mourning weeds | Mal 3:14 |
| עָסַס *ʻâçaç* (H6072) | to squeeze out juice; figuratively, to trample | Mal 3:21 |
| שָׁפִיר *Shâphîyr* (H8208) | Shaphir, a place in Palestine | Mic 1:11 |
| צַאֲנָן *Tsaʼănân* (H6630) | Zaanan, a place in Palestine | Mic 1:11 |
| עֶמְדָּה *ʻemdâh* (H5979) | a station, i.e. domicile | Mic 1:11 |
| מָרוֹת *Mârôwth* (H4796) | Maroth, a place in Palestine | Mic 1:12 |
| רָתַם *râtham* (H7573) | to yoke up (to the pole of a vehicle) | Mic 1:13 |
| בׇּצְרָה *botsrâh* (H1223) | an enclosure, i.e. sheep fold | Mic 2:12 |
| רוֹמָה *rôwmâh* (H7317) | elation, i.e. (adverbially) proudly | Mic 2:3 |
| נִהְיָה *nihyâh* (H5093) | lamentation | Mic 2:4 |
| הָלָא *hâlâʼ* (H1972) | to remove or be remote | Mic 4:7 |
| יֶשַׁח *yeshach* (H3445) | hunger | Mic 6:14 |
| עָבַת *ʻâbath* (H5686) | to interlace, i.e. (figuratively) to pervert | Mic 7:3 |
| מְסוּכָה *mᵉçûwkâh* (H4534) | a hedge | Mic 7:4 |
| נַחוּם *Nachûwm* (H5151) | Nachum, an Israelite prophet | Nah 1:1 |
| אֶלְקֹשִׁי *ʼElqôshîy* (H512) | an Elkoshite or native of Elkosh | Nah 1:1 |
| בּוּקָה *bûwqâh* (H950) | emptiness (as adjective) | Nah 2:11 |
| מְבוּקָה *mᵉbûwqâh* (H4003) | emptiness | Nah 2:11 |
| פִּיק *pîyq* (H6375) | a tottering | Nah 2:11 |
| תָּלַע *tâlaʻ* (H8529) | to crimson, i.e. dye that color | Nah 2:4 |
| פְּלָדָה *pᵉlâdâh* (H6393) | a cleaver, i.e. iron armature (of a chariot) | Nah 2:4 |
| רָעַל *râʻal* (H7477) | to reel, i.e. (figuratively) to brandish | Nah 2:4 |
| מִנְּזָר *minnᵉzâr* (H4502) | a prince | Nah 3:17 |
| כֵּהָה *kêhâh* (H3545) | properly, a weakening; figuratively, alleviation, i.e. cure | Nah 3:19 |
| דָּהַר *dâhar* (H1725) | to curvet or move irregularly | Nah 3:2 |
| אֲזַנְיָה *ʼĂzanyâh* (H245) | Azanjah, an Israelite | Neh 10:10 |
| בְּנִינוּ *Bᵉnîynûw* (H1148) | Beninu, an Israelite | Neh 10:14 |
| מַגְפִּיעָשׁ *Magpîyʻâsh* (H4047) | Magpiash, an Israelite | Neh 10:21 |
| פִּלְחָא *Pilchâʼ* (H6401) | Pilcha, an Israelite | Neh 10:25 |
| שׁוֹבֵק *Shôwbêq* (H7733) | Shobek, an Israelite | Neh 10:25 |
| חֲשַׁבְנָה *Chăshabnâh* (H2812) | Chashnah, an Israelite | Neh 10:26 |
| עָנָן *ʻÂnân* (H6052) | Anan, an Israelite | Neh 10:27 |
| מַקָּחָה *maqqâchâh* (H4728) | something received, i.e. merchandise (purchased) | Neh 10:32 |
| בִּלְגַּי *Bilgay* (H1084) | Bilgai, an Israelite | Neh 10:9 |
| פְּלַלְיָה *Pᵉlalyâh* (H6421) | Pelaljah, an Israelite | Neh 11:12 |
| עֲמַשְׁסַי *ʻĂmashçay* (H6023) | Amashsay, an Israelite | Neh 11:13 |
| אַחְזַי *ʼAchzay* (H273) | Achzai, an Israelite | Neh 11:13 |
| גִּשְׁפָּא *Gishpâʼ* (H1658) | Gishpa, an Israelite | Neh 11:21 |
| יְקַבְצְאֵל *Yᵉqabtsᵉʼêl* (H3343) | Jekabtseel, a place in Palestine | Neh 11:25 |
| מְכֹנָה *Mᵉkônâh* (H4368) | Mekonah, a place in Palestine | Neh 11:28 |
| נְבַלָּט *Nᵉballâṭ* (H5041) | Neballat, a place in Palestine | Neh 11:34 |
| עֲתָיָה *ʻĂthâyâh* (H6265) | Athajah, an Israelite | Neh 11:4 |
| חֲזָיָה *Chăzâyâh* (H2382) | Chazajah, an Israelite | Neh 11:5 |
| שִׁלֹנִי *Shilônîy* (H8023) | Shiloni, an Israelite | Neh 11:5 |
| יוֹעֵד *Yôwʻêd* (H3133) | Joed, an Israelite | Neh 11:7 |
| גַּבַּי *Gabbay* (H1373) | Gabbai, an Israelite | Neh 11:8 |
| מְרָיָה *Mᵉrâyâh* (H4811) | Merajah, an Israelite | Neh 12:12 |
| חֶלְקַי *Chelqay* (H2517) | Chelkai, an Israelite | Neh 12:15 |
| מוֹעַדְיָה *Môwʻadyâh* (H4153) | Moadjah, an Israelite | Neh 12:17 |
| פִּלְטַי *Pilṭay* (H6408) | Piltai, an Israelite | Neh 12:17 |
| קַלַּי *Qallay* (H7040) | Kallai, an Israelite | Neh 12:20 |
| פַּרְסִי *Parçîy* (H6542) | a Parsite (i.e. Persian), or inhabitant of Peres | Neh 12:22 |
| תַּהֲלֻכָה *tahălukâh* (H8418) | a procession | Neh 12:31 |
| מִלֲלַי *Milălay* (H4450) | Milalai, an Israelite | Neh 12:36 |
| גִּלֲלַי *Gilălay* (H1562) | Gilalai, an Israelite | Neh 12:36 |
| מָעַי *Mâʻay* (H4597) | Maai, an Israelite | Neh 12:36 |
| מַעֲדְיָה *Maʻădyâh* (H4573) | Maadjah, an Israelite | Neh 12:5 |
| הֻיְּדָה *huyᵉdâh* (H1960) | properly, an acclaim, i.e. a choir of singers | Neh 12:8 |
| אַשְׁדּוֹדִית *ʼAshdôwdîyth* (H797) | (only adverb) in the language of Ashdod | Neh 13:24 |
| גֹּאֶל *gôʼel* (H1352) | profanation | Neh 13:29 |
| חֲרוּמַף *chărûwmaph* (H2739) | Charumaph, an Israelite | Neh 3:10 |
| שַׁלּוּן *Shallûwn* (H7968) | Shallun, an Israelite | Neh 3:15 |
| טָלַל *ṭâlal* (H2926) | properly, to strew over, i.e. (by implication) to cover in or plate (with beams) | Neh 3:15 |
| עַזְבּוּק *ʻAzbûwq* (H5802) | Azbuk, an Israelite | Neh 3:16 |
| בַּוַּי *Bavvay* (H942) | Bavvai, an Israelite | Neh 3:18 |
| פָּלָל *Pâlâl* (H6420) | Palal, an Israelite | Neh 3:25 |
| אוּזַי *ʼÛwzay* (H186) | Uzai, an Israelite | Neh 3:25 |
| צָלָף *Tsâlâph* (H6764) | Tsalaph, an Israelite | Neh 3:30 |
| צֹרְפִי *Tsôrᵉphîy* (H6885) | Tsorephi (with the article), an Israelite | Neh 3:31 |
| מִפְקָד *Miphqâd* (H4663) | Miphkad, the name of a gate in Jerusalem | Neh 3:31 |
| אֲמֵלָל *ʼămêlâl* (H537) | languid | Neh 3:34 |
| בּוּזָה *bûwzâh* (H939) | something scorned; an object of contempt | Neh 3:36 |
| בְּסוֹדְיָה *Bᵉçôwdᵉyâh* (H1152) | Besodejah, an Israelite | Neh 3:6 |
| מְלַטְיָה *Mᵉlaṭyâh* (H4424) | Melatjah, a Gibeonite | Neh 3:7 |
| יָדוֹן *Yâdôwn* (H3036) | Jadon, an Israelite | Neh 3:7 |
| חַרְהֲיָה *Charhăyâh* (H2736) | Charhajah, an Israelite | Neh 3:8 |
| רַקָּח *raqqâch* (H7546) | a male perfumer | Neh 3:8 |
| צְחִיחִי *tsᵉchîychîy* (H6708) | bare spot, i.e. in the glaring sun | Neh 4:7 |
| אֱלוּל *ʼĔlûwl* (H435) | Elul, the sixth Jewish month | Neh 6:15 |
| גּוּף *gûwph* (H1479) | properly, to hollow or arch, i.e. (figuratively) close; to shut | Neh 7:3 |
| הוֹדְוָה *Hôwdᵉvâh* (H1937) | Hodevah (or Hodevjah), an Israelite | Neh 7:43 |
| יַחַשׂ *yachas* (H3188) | a pedigree or family list (as growing spontaneously) | Neh 7:5 |
| נְפוּשְׁסִים *Nᵉphûwshᵉçîym* (H5300) | Nephushesim, a Temple-servant | Neh 7:52 |
| אַדּוֹן *ʼAddôwn* (H114) | Addon, apparently an Israelite | Neh 7:61 |
| רַעַמְיָה *Raʻamyâh* (H7485) | Raamjah, an Israelite | Neh 7:7 |
| נַחֲמָנִי *Nachămânîy* (H5167) | Nachamani, an Israelite | Neh 7:7 |
| מִסְפֶּרֶת *Miçpereth* (H4559) | Mispereth, an Israelite | Neh 7:7 |
| נְחוּם *Nᵉchûwm* (H5149) | Nechum, an Israelite | Neh 7:7 |
| חַשְׁבַּדָּנָה *Chashbaddânâh* (H2806) | Chasbaddanah, an Israelite | Neh 8:4 |
| מֹעַל *môʻal* (H4607) | a raising (of the hands) | Neh 8:6 |
| עָדַן *ʻâdan* (H5727) | to be soft or pleasant; figuratively and reflexively, to live voluptuously | Neh 9:25 |
| כְּנָנִי *Kᵉnânîy* (H3662) | Kenani, an Israelite | Neh 9:4 |
| זָרָא *zârâʼ* (H2214) | disgust | Num 11:20 |
| אֲסְפְּסֻף *ʼăçpᵉçuph* (H628) | gathered up together, i.e. a promiscuous assemblage (of people) | Num 11:4 |
| קִשֻּׁא *qishshuʼ* (H7180) | a cucumber (from the difficulty of digestion) | Num 11:5 |
| אֲבַטִּיחַ *ʼăbaṭṭîyach* (H20) | a melon (only plural) | Num 11:5 |
| בֶּצֶל *betsel* (H1211) | an onion | Num 11:5 |
| שׁוּם *shûwm* (H7762) | garlic (from its rank odor) | Num 11:5 |
| דּוּךְ *dûwk* (H1743) | to bruise in a mortar | Num 11:8 |
| מְדֹכָה *mᵉdôkâh* (H4085) | a mortar | Num 11:8 |
| גַּדִּיאֵל *Gaddîyʼêl* (H1427) | Gaddiel, an Israelite | Num 13:10 |
| סוֹדִי *Çôwdîy* (H5476) | Sodi, an Israelite | Num 13:10 |
| גַּדִּי *Gaddîy* (H1426) | Gaddi, an Israelite | Num 13:11 |
| סוּסִי *Çûwçîy* (H5485) | Susi, an Israelite | Num 13:11 |
| גְּמַלִּי *Gᵉmallîy* (H1582) | Gemalli, an Israelite | Num 13:12 |
| סְתוּר *Çᵉthûwr* (H5639) | Sethur, an Israelite | Num 13:13 |
| נַחְבִּי *Nachbîy* (H5147) | Nachbi, an Israelite | Num 13:14 |
| וׇפְסִי *Vophçîy* (H2058) | Vophsi, an Israelite | Num 13:14 |
| גְּאוּאֵל *Gᵉʼûwʼêl* (H1345) | Geuel, an Israelite | Num 13:15 |
| מָכִי *Mâkîy* (H4352) | Maki, an Israelite | Num 13:15 |
| רָפוּא *Râphûwʼ* (H7505) | Raphu, an Israelite | Num 13:9 |
| אוֹן *ʼÔwn* (H203) | On, an Israelite | Num 16:1 |
| בְּרִיאָה *bᵉrîyʼâh* (H1278) | a creation, i.e. a novelty | Num 16:30 |
| רִקֻּעַ *riqquaʻ* (H7555) | beaten out, i.e. a (metallic) plate | Num 17:3 |
| אֲתָרִים *ʼĂthârîym* (H871) | Atharim, a place near Palestine | Num 21:1 |
| וָהֵב *Vâhêb* (H2052) | Vaheb, a place in Moab | Num 21:14 |
| אֶשֶׁד *ʼeshed* (H793) | an outpouring | Num 21:15 |
| נֹפַח *Nôphach* (H5302) | Nophach, a place in Moab | Num 21:30 |
| קְלֹקֵל *qᵉlôqêl* (H7052) | insubstantial | Num 21:5 |
| מִשְׁעוֹל *mishʻôwl* (H4934) | a hollow, i.e. a narrow passage | Num 22:24 |
| צֹפִים *Tsôphîym* (H6839) | Tsophim, a place East of the Jordan | Num 23:14 |
| שֵׁת *shêth* (H8351) | tumult | Num 24:17 |
| נֵכֶל *nêkel* (H5231) | deceit | Num 25:18 |
| קֻבָּה *qubbâh* (H6898) | a pavilion (as a domed cavity) | Num 25:8 |
| קֹבָה *qôbâh* (H6897) | the abdomen (as a cavity) | Num 25:8 |
| נְמוּאֵלִי *Nᵉmûwʼêlîy* (H5242) | a Nemuelite, or descendant of Nemuel | Num 26:12 |
| יָכִינִי *Yâkîynîy* (H3200) | a Jakinite (collectively) or descendants of Jakin | Num 26:12 |
| שָׁאוּלִי *Shâʼûwlîy* (H7587) | a Shaulite or descendant of Shaul | Num 26:13 |
| צְפוֹן *Tsᵉphôwn* (H6827) | Tsephon, an Israelite | Num 26:15 |
| צְפוֹנִי *Tsᵉphôwnîy* (H6831) | a Tsephonite, or (collectively) descendants of Tsephon | Num 26:15 |
| שׁוּנִי *Shûwnîy* (H7765) | a Shunite (collectively) or descendants of Shuni | Num 26:15 |
| עֵרִי *ʻÊrîy* (H6180) | a Erite (collectively) or descendants of Eri | Num 26:16 |
| אֲרוֹד *ʼĂrôwd* (H720) | Arod, an Israelite | Num 26:17 |
| שֵׁלָנִי *Shêlânîy* (H8024) | a Shelanite (collectively), or descendants of Shelah | Num 26:20 |
| פַּרְצִי *Partsîy* (H6558) | a Partsite (collectively) or descendants of Perets | Num 26:20 |
| חָמוּלִי *Châmûwlîy* (H2539) | a Chamulite (collectively) or descendants of Chamul | Num 26:21 |
| תּוֹלָעִי *Tôwlâʻîy* (H8440) | a Tolaite (collectively) or descendants of Tola | Num 26:23 |
| פּוּנִי *Pûwnîy* (H6324) | a Punite (collectively) or descendants of an unknown Pun | Num 26:23 |
| יָשֻׁבִי *Yâshubîy* (H3432) | a Jashubite, or descendant of Jashub | Num 26:24 |
| שִׁמְרֹנִי *Shimrônîy* (H8117) | a Shimronite (collectively) or descendants of Shimron | Num 26:24 |
| סַרְדִּי *Çardîy* (H5625) | a Seredite (collectively) or descendants of Sered | Num 26:26 |
| אֵלוֹנִי *ʼÊlôwnîy* (H440) | an Elonite or descendant (collectively) of Elon | Num 26:26 |
| יַחְלְאֵלִי *Yachlᵉʼêlîy* (H3178) | a Jachleelite or descendant of Jachleel | Num 26:26 |
| מָכִירִי *Mâkîyrîy* (H4354) | a Makirite or descendant of Makir | Num 26:29 |
| אִיעֶזֵר *ʼÎyʻezêr* (H372) | Iezer, an Israelite | Num 26:30 |
| אִיעֶזְרִי *ʼÎyʻezrîy* (H373) | an Iezrite or descendant of Iezer | Num 26:30 |
| חֶלְקִי *Chelqîy* (H2516) | a Chelkite or descendant of Chelek | Num 26:30 |
| אַשְׂרִאֵלִי *ʼAsriʼêlîy* (H845) | an Asrielite (collectively) or descendant of Asriel | Num 26:31 |
| שִׁכְמִי *Shikmîy* (H7930) | a Shikmite (collectively), or descendants of Shekem | Num 26:31 |
| שְׁמִידָעִי *Shᵉmîydâʻîy* (H8062) | a Shemidaite (collectively) or descendants of Shemida | Num 26:32 |
| חֶפְרִי *Chephrîy* (H2662) | a Chephrite (collectively) or descendants of Chepher | Num 26:32 |
| שֻׁתַלְחִי *Shuthalchîy* (H8364) | a Shuthalchite (collectively) or descendants of Shuthelach | Num 26:35 |
| בַּכְרִי *Bakrîy* (H1076) | a Bakrite (collectively) or descendants of Beker | Num 26:35 |
| תַּחֲנִי *Tachănîy* (H8470) | a Tachanite (collectively) or descendants of Tachan | Num 26:35 |
| עֵרָן *ʻÊrân* (H6197) | Eran, an Israelite | Num 26:36 |
| עֵרָנִי *ʻÊrânîy* (H6198) | an Eranite or descendant (collectively) of Eran | Num 26:36 |
| בַּלְעִי *Balʻîy* (H1108) | a Belaite (collectively) or descendants of Bela | Num 26:38 |
| אַשְׁבֵּלִי *ʼAshbêlîy* (H789) | an Ashbelite (collectively) or descendant of Ashbel | Num 26:38 |
| אֲחִירָם *ʼĂchîyrâm* (H297) | Achiram, an Israelite | Num 26:38 |
| אֲחִירָמִי *ʼĂchîyrâmîy* (H298) | an Achiramite or descendant (collectively) of Achiram | Num 26:38 |
| שׁוּפָמִי *Shûwphâmîy* (H7781) | a Shuphamite (collectively) or descendants of Shephupham | Num 26:39 |
| חוּפָם *Chûwphâm* (H2349) | Chupham, an Israelite | Num 26:39 |
| חוּפָמִי *Chûwphâmîy* (H2350) | a Chuphamite or descendant of Chupham | Num 26:39 |
| אַרְדִּי *ʼArdîy* (H716) | an Ardite (collectively) or descendant of Ard | Num 26:40 |
| נַעֲמִי *Naʻămîy* (H5280) | a Naamanite, or descendant of Naaman (collectively) | Num 26:40 |
| שׁוּחָם *Shûwchâm* (H7748) | Shucham, an Israelite | Num 26:42 |
| יִשְׁוִי *Yishvîy* (H3441) | a Jishvite (collectively) or descendants of Jishvi | Num 26:44 |
| בְּרִיעִי *Bᵉrîyʻîy* (H1284) | a Beriite (collectively) or descendants of Beriah | Num 26:44 |
| חֶבְרִי *Chebrîy* (H2277) | a Chebrite (collectively) or descendants of Cheber | Num 26:45 |
| מַלְכִּיאֵלִי *Malkîyʼêlîy* (H4440) | a Malkielite or descendant of Malkiel | Num 26:45 |
| יַחְצְאֵלִי *Yachtsᵉʼêlîy* (H3184) | a Jachtseelite (collectively) or descendants of Jachtseel | Num 26:48 |
| גּוּנִי *Gûwnîy* (H1477) | a Gunite (collectively with article prefix) or descendants of Guni | Num 26:48 |
| יִצְרִי *Yitsrîy* (H3340) | a Jitsrite (collectively) or descendants of Jetser | Num 26:49 |
| שִׁלֵּמִי *Shillêmîy* (H8016) | a Shilemite (collectively) or descendants of Shillem | Num 26:49 |
| חֲנֹכִי *Chănôkîy* (H2599) | a Chanokite (collectively) or descendants of Chanok | Num 26:5 |
| פַּלֻּאִי *Palluʼîy* (H6384) | a Palluite (collectively) or descendants of Pallu | Num 26:5 |
| מְרָרִי *Mᵉrârîy* (H4848) | a Merarite (collectively), or decendants of Merari | Num 26:57 |
| כַּרְמִי *Karmîy* (H3757) | a Karmite or descendant of Karmi | Num 26:6 |
| תַּרְבּוּת *tarbûwth* (H8635) | multiplication, i.e. progeny | Num 32:14 |
| נִמְרָה *Nimrâh* (H5247) | Nimrah, a place East of the Jordan | Num 32:3 |
| בְּעֹן *Bᵉʻôn* (H1194) | Beon, a place East of the Jordan | Num 32:3 |
| שֵׂךְ *sêk* (H7899) | a brier (as of a hedge) | Num 33:55 |
| אָוָה *ʼâvâh* (H184) | to extend or mark out | Num 34:10 |
| אֱלִידָד *ʼĔlîydâd* (H449) | Elidad, an Israelite | Num 34:21 |
| כִּסְלוֹן *Kiçlôwn* (H3692) | Kislon, an Israelite | Num 34:21 |
| יׇגְלִי *Yoglîy* (H3020) | Jogli, an Israelite | Num 34:22 |
| אֵפֹד *ʼÊphôd* (H641) | Ephod, an Israelite | Num 34:23 |
| שִׁפְטָן *Shiphṭân* (H8204) | Shiphtan, an Israelite | Num 34:24 |
| פַּרְנַךְ *Parnak* (H6535) | Parnak, an Israelite | Num 34:25 |
| עַזָּן *ʻAzzân* (H5821) | Azzan, an Israelite | Num 34:26 |
| אֲחִיהוּד *ʼĂchîyhûwd* (H282) | Achihud, an Israelite | Num 34:27 |
| שְׁלֹמִי *Shᵉlômîy* (H8015) | Shelomi, an Israelite | Num 34:27 |
| פְּדַהְאֵל *Pᵉdahʼêl* (H6300) | Pedahel, an Israelite | Num 34:28 |
| זִפְרֹן *Ziphrôn* (H2202) | Ziphron, a place in Palestine | Num 34:9 |
| לָאֵל *Lâʼêl* (H3815) | Lael an Israelite | Num 3:24 |
| צוּרִיאֵל *Tsûwrîyʼêl* (H6700) | Tsuriel, an Israelite | Num 3:35 |
| צָבֶה *tsâbeh* (H6639) | turgid | Num 5:21 |
| מִשְׁרָה *mishrâh* (H4952) | maceration, i.e. steeped juice | Num 6:3 |
| חַרְצַן *chartsan* (H2785) | a sour grape (as sharp in taste) | Num 6:4 |
| זָג *zâg* (H2085) | the skin of a grape | Num 6:4 |
| סְפָרָד *Çᵉphârâd* (H5614) | Sepharad, a region of Assyria | Obad 1:20 |
| מִצְפֻּן *mitspun* (H4710) | a secret (place or thing, perhaps, treasure) | Obad 1:6 |
| מָזוֹר *mâzôwr* (H4204) | treachery, i.e. a plot | Obad 1:7 |
| קֶטֶל *qeṭel* (H6993) | a violent death | Obad 1:9 |
| מַדְקָרָה *madqârâh* (H4094) | a wound | Prov 12:18 |
| חָרַךְ *chârak* (H2760) | to braid (i.e. to entangle or snare) or catch (game) in anet | Prov 12:27 |
| מׇרָּה *morrâh* (H4787) | trouble | Prov 14:10 |
| רָזוֹן *râzôwn* (H7333) | a dignitary | Prov 14:28 |
| מַעֲרָךְ *maʻărâk* (H4633) | an arrangement, i.e. (figuratively) mental disposition | Prov 16:1 |
| כִּשָּׁלוֹן *kishshâlôwn* (H3783) | properly, a tottering, i.e. ruin | Prov 16:18 |
| אָכַף *ʼâkaph* (H404) | to urge | Prov 16:26 |
| עָצָה *ʻâtsâh* (H6095) | properly, to fasten (or make firm), i.e. to close (the eyes) | Prov 16:30 |
| גֵּהָה *gêhâh* (H1456) | a cure | Prov 17:22 |
| מֶמֶר *memer* (H4470) | sorrow | Prov 17:25 |
| גָּרֹל *gârôl* (H1632) | harsh | Prov 19:19 |
| שַׁאֲוָה *shaʼăvâh* (H7584) | a tempest (as rushing) | Prov 1:27 |
| יָלַע *yâlaʻ* (H3216) | to blurt or utter inconsiderately | Prov 20:25 |
| כָּפָה *kâphâh* (H3711) | properly, to bend, i.e. (figuratively) to tame or subdue | Prov 21:14 |
| הֲפַכְפַּךְ *hăphakpak* (H2019) | very perverse | Prov 21:8 |
| וָזָר *vâzâr* (H2054) | crime | Prov 21:8 |
| חָשֹׁךְ *châshôk* (H2823) | dark (figuratively, i.e. obscure) | Prov 22:29 |
| שַׂכִּין *sakkîyn* (H7915) | a knife (as pointed or edged) | Prov 23:2 |
| לֹעַ *lôaʻ* (H3930) | the gullet | Prov 23:2 |
| נוּמָה *nûwmâh* (H5124) | sleepiness | Prov 23:21 |
| חֶתֶף *chetheph* (H2863) | properly, rapine; figuratively, robbery | Prov 23:28 |
| אֲבוֹי *ʼăbôwy* (H17) | want | Prov 23:29 |
| חַכְלִלוּת *chaklilûwth* (H2448) | flash (of the eyes); in a bad sense, blearedness | Prov 23:29 |
| חִבֵּל *chibbêl* (H2260) | a mast | Prov 23:34 |
| שָׁעַר *shâʻar* (H8176) | to act as gatekeeper; (figuratively) to estimate | Prov 23:7 |
| קִמָּשׁוֹן *qimmâshôwn* (H7063) | a prickly plant | Prov 24:31 |
| אֹפֶן *ʼôphen* (H655) | a turn, i.e. a season | Prov 25:11 |
| מֵפִיץ *mêphîyts* (H4650) | a breaker, i.e. mallet | Prov 25:18 |
| רֹעָה *rôʻâh* (H7465) | breakage | Prov 25:19 |
| מוּעֶדֶת *mûwʻedeth* (H4154) | properly, made to slip, i.e. dislocated | Prov 25:19 |
| מַעְצָר *maʻtsâr* (H4623) | subjectively, control | Prov 25:28 |
| עֹמֶק *ʻômeq* (H6011) | depth | Prov 25:3 |
| מַשָּׁאוֹן *mashshâʼôwn* (H4860) | dissimulation | Prov 26:26 |
| מִדְחֶה *midcheh* (H4072) | overthrow | Prov 26:28 |
| מַרְגֵּמָה *margêmâh* (H4773) | a stone-heap | Prov 26:8 |
| סַגְרִיד *çagrîyd* (H5464) | a pouring rain | Prov 27:15 |
| מַהֲלָל *mahălâl* (H4110) | fame | Prov 27:21 |
| כָּתַשׁ *kâthash* (H3806) | to butt or pound | Prov 27:22 |
| עֱלִי *ʻĕlîy* (H5940) | a pestle (as lifted) | Prov 27:22 |
| נֵטֶל *nêṭel* (H5192) | a burden | Prov 27:3 |
| אַכְזְרִיּוּת *ʼakzᵉrîyûwth* (H395) | fierceness | Prov 27:4 |
| שְׁחוּת *shᵉchûwth* (H7816) | pit | Prov 28:10 |
| תָּכָךְ *tâkâk* (H8501) | to dissever, i.e. crush | Prov 29:13 |
| פָּנַק *pânaq* (H6445) | to enervate | Prov 29:21 |
| מָנוֹן *mânôwn* (H4497) | a continuator, i.e. heir | Prov 29:21 |
| אָגוּר *ʼÂgûwr* (H94) | Agur, a fanciful name for Solomon | Prov 30:1 |
| יָקֶה *Yâqeh* (H3348) | Jakeh, a symbolical name (for Solomon) | Prov 30:1 |
| אֻכָל *ʼUkâl* (H401) | Ucal, a fancy name | Prov 30:1 |
| עֲלוּקָה *ʻălûwqâh* (H5936) | the leech | Prov 30:15 |
| שְׂמָמִית *sᵉmâmîyth* (H8079) | a lizard (from the superstition of its noxiousness) | Prov 30:28 |
| זַרְזִיר *zarzîyr* (H2223) | properly, tightly girt, i.e. probably a racer, or some fleet animal (as being slender in the waist) | Prov 30:31 |
| אַלְקוּם *ʼalqûwm* (H510) | a non-rising (i.e. resistlessness) | Prov 30:31 |
| כִּישׁוֹר *kîyshôwr* (H3601) | literally a director, i.e. the spindle or shank of adistaff, by which it is twirled | Prov 31:19 |
| עַצְלוּת *ʻatslûwth* (H6104) | indolence | Prov 31:27 |
| חֲלוֹף *chălôwph* (H2475) | properly, surviving; by implication (collectively) orphans | Prov 31:8 |
| לֶכֶד *leked* (H3921) | something to capture with, i.e. a noose | Prov 3:26 |
| רִפְאוּת *riphʼûwth* (H7500) | a cure | Prov 3:8 |
| לְזוּת *lᵉzûwth* (H3891) | perverseness | Prov 4:24 |
| יַעֲלָה *yaʻălâh* (H3280) | an ibex (as climbing) | Prov 5:19 |
| רָבַד *râbad* (H7234) | to spread | Prov 7:16 |
| חֲטֻבָה *chăṭubâh* (H2405) | properly, a carving; hence, a tapestry (as figured) | Prov 7:16 |
| אֵטוּן *ʼêṭûwn* (H330) | properly, twisted (yarn), i.e. tapestry | Prov 7:16 |
| אֹהַב *ʼôhab* (H159) | affection (in a good or a bad sense) | Prov 7:18 |
| גֵּאָה *gêʼâh* (H1344) | arrogance | Prov 8:13 |
| עָתֵק *ʻâthêq* (H6276) | antique, i.e. valued | Prov 8:18 |
| אָמוֹן *ʼâmôwn* (H525) | skilled, i.e. an architect | Prov 8:30 |
| כְּסִילוּת *kᵉçîylûwth* (H3687) | silliness | Prov 9:13 |
| פְּתַיּוּת *pᵉthayûwth* (H6615) | silliness (i.e. seducibility) | Prov 9:13 |
| שִׁקֻּו *shiqquv* (H8249) | (plural collective) a draught | Ps 102:10 |
| עַרעָר *ʻarʻâr* (H6199) | naked, i.e. (figuratively) poor | Ps 102:18 |
| עֳפֶא *ʻŏpheʼ* (H6073) | a bough (as covering the tree) | Ps 104:12 |
| רְכוּב *rᵉkûwb* (H7398) | a vehicle (as ridden on) | Ps 104:3 |
| מָחוֹז *mâchôwz* (H4231) | a harbor (as shut in by the shore) | Ps 107:30 |
| מִשְׁחָר *mishchâr* (H4891) | dawn | Ps 110:3 |
| לָעַז *lâʻaz* (H3937) | to speak in a foreign tongue | Ps 114:1 |
| תַּגְמוּל *tagmûwl* (H8408) | a bestowment | Ps 116:12 |
| מָלַץ *mâlats* (H4452) | to be smooth, i.e. (figuratively) pleasant | Ps 119:103 |
| סֵעֵף *çêʻêph* (H5588) | divided (in mind), i.e. (concretely) a skeptic | Ps 119:113 |
| פֵּתַח *pêthach* (H6608) | opening (figuratively) i.e. disclosure | Ps 119:130 |
| יָאַב *yâʼab* (H2968) | to desire | Ps 119:131 |
| תַּאֲבָה *taʼăbâh* (H8375) | desire | Ps 119:20 |
| טָפַשׁ *ṭâphash* (H2954) | properly, apparently to be thick; figuratively, to be stupid | Ps 119:70 |
| תִּכְלָה *tiklâh* (H8502) | completeness | Ps 119:96 |
| אוֹיָה *ʼôwyâh* (H190) | lamentation; also interjectionally Oh! | Ps 120:5 |
| גַּאֲיוֹן *gaʼăyôwn* (H1349) | haughty | Ps 123:4 |
| זֵידוֹן *zêydôwn* (H2121) | boiling of water, i.e. wave | Ps 124:5 |
| שִׁיבָה *shîybâh* (H7870) | a return (of property) | Ps 126:1 |
| שְׁתִל *shᵉthil* (H8363) | a sprig (as if transplanted), i.e. sucker | Ps 128:3 |
| חֵצֶן *chêtsen* (H2683) | the bosom (as comprised between the arms) | Ps 129:7 |
| פָּסַס *pâçaç* (H6461) | probably to disperse, i.e. (intransitive) disappear | Ps 12:2 |
| עֲלִיל *ʻălîyl* (H5948) | probably a crucible (as working over the metal) | Ps 12:7 |
| זֻלּוּת *zullûwth* (H2149) | properly, a shaking, i.e. perhaps a tempest | Ps 12:9 |
| רַנֵּן *rannên* (H7444) | shouting (for joy) | Ps 132:16 |
| שְׁנָת *shᵉnâth* (H8153) | sleep | Ps 132:4 |
| תּוֹלָל *tôwlâl* (H8437) | causing to howl, i.e. an oppressor | Ps 137:3 |
| גֹּלֶם *gôlem* (H1564) | a wrapped (and unformed mass, i.e. as the embryo) | Ps 139:16 |
| תְּקוֹמֵם *tᵉqôwmêm* (H8618) | an opponent | Ps 139:21 |
| רֶבַע *rebaʻ* (H7252) | prostration (for sleep) | Ps 139:3 |
| נָסַק *nâçaq* (H5266) | to go up | Ps 139:8 |
| מַהֲמֹרָה *mahămôrâh* (H4113) | perhaps an abyss | Ps 140:11 |
| מְדַחְפָה *mᵉdachphâh* (H4073) | a push, i.e. ruin | Ps 140:12 |
| עַכְשׁוּב *ʻakshûwb* (H5919) | an asp (from lurking coiled up) | Ps 140:4 |
| מַאֲוַי *maʼăvay* (H3970) | a desire | Ps 140:9 |
| זָמָם *zâmâm* (H2162) | a plot | Ps 140:9 |
| שׇׁמְרָה *shomrâh* (H8108) | watchfulness | Ps 141:3 |
| מַנְעַם *manʻam* (H4516) | a delicacy | Ps 141:4 |
| נָטִיעַ *nâṭîyaʻ* (H5195) | a plant | Ps 144:12 |
| מֶזֶו *mezev* (H4200) | a granary | Ps 144:13 |
| אָלַף *ʼâlaph* (H503) | causative, to make athousandfold | Ps 144:13 |
| בָּרַק *bâraq* (H1299) | to lighten (lightning) | Ps 144:6 |
| עֶשְׁתֹּנָה *ʻeshtônâh* (H6250) | thinking | Ps 146:4 |
| רוֹמְמָה *rôwmᵉmâh* (H7319) | exaltation, i.e. praise | Ps 149:6 |
| תֵּקַע *têqaʻ* (H8629) | a blast of a trumpet | Ps 150:3 |
| שָׁפַר *shâphar* (H8231) | to glisten, i.e. (figuratively) be (causatively, make) fair | Ps 16:6 |
| דִּמְיוֹן *dimyôwn* (H1825) | resemblance | Ps 17:12 |
| צָפִין *tsâphîyn* (H6840) | a treasure (as hidden) | Ps 17:14 |
| חֶשְׁכָה *cheshkâh* (H2824) | darkness | Ps 18:12 |
| חֵזֶק *chêzeq* (H2391) | help | Ps 18:2 |
| גְּבַר *gᵉbar* (H1399) | a person | Ps 18:26 |
| חָרַג *chârag* (H2727) | properly, to leap suddenly, i.e. (by implication) to be dismayed | Ps 18:46 |
| שְׁגִיאָה *shᵉgîyʼâh* (H7691) | a moral mistake | Ps 19:13 |
| אֲרֶשֶׁת *ʼăresheth* (H782) | a longing for | Ps 21:3 |
| אֱיָלוּת *ʼĕyâlûwth* (H360) | power; by implication, protection | Ps 22:20 |
| עֱנוּת *ʻĕnûwth* (H6039) | affliction | Ps 22:25 |
| יָפֵחַ *yâphêach* (H3307) | properly, puffing, i.e. (figuratively) meditating | Ps 27:12 |
| רָגַשׁ *râgash* (H7283) | to be tumultuous | Ps 2:1 |
| שֶׁלֶו *shelev* (H7959) | security | Ps 30:7 |
| רֹכֶס *rôkeç* (H7407) | a snare (as of tied meshes) | Ps 31:21 |
| גָּרַז *gâraz* (H1629) | to cut off | Ps 31:23 |
| חֲרָבוֹן *chărâbôwn* (H2725) | parching heat | Ps 32:4 |
| רֹן *rôn* (H7438) | a shout (of deliverance) | Ps 32:7 |
| בָּלַם *bâlam* (H1102) | to muzzle | Ps 32:9 |
| נֵכֶה *nêkeh* (H5222) | a smiter, i.e. (figuratively) traducer | Ps 35:15 |
| רָגֵעַ *râgêaʻ* (H7282) | restful, i.e. peaceable | Ps 35:20 |
| תִּגְרָה *tigrâh* (H8409) | strife, i.e. infliction | Ps 39:11 |
| מַחְסוֹם *machçôwm* (H4269) | a muzzle | Ps 39:2 |
| רָהָב *râhâb* (H7295) | insolent | Ps 40:5 |
| סָךְ *çâk* (H5519) | properly, a thicket of men, i.e. a crowd | Ps 42:5 |
| חֶרְמוֹנִים *Chermôwnîym* (H2769) | Hermons, i.e. its peaks | Ps 42:7 |
| מִצְעָר *Mitsʻâr* (H4706) | Mitsar, a peak of Lebanon | Ps 42:7 |
| מָנוֹד *mânôwd* (H4493) | a nodding or toss (of the head in derision) | Ps 44:15 |
| רָחַשׁ *râchash* (H7370) | to gush | Ps 45:2 |
| קְצִיעָה *qᵉtsîyʻâh* (H7102) | cassia (as peeled; plural the bark) | Ps 45:9 |
| חֵילָה *chêylâh* (H2430) | an intrenchment | Ps 48:14 |
| פָּסַג *pâçag* (H6448) | to cut up, i.e. (figuratively) contemplate | Ps 48:14 |
| נוֹף *nôwph* (H5131) | elevation | Ps 48:3 |
| הָגוּת *hâgûwth* (H1900) | musing | Ps 49:4 |
| עָקֵב *ʻâqêb* (H6120) | a lier in wait | Ps 49:6 |
| מִכְלָל *miklâl* (H4359) | perfection (of beauty) | Ps 50:2 |
| דׇּפִי *dophîy* (H1848) | a stumbling-block | Ps 50:20 |
| יְשִׁימַה *yᵉshîymah* (H3451) | desolation | Ps 55:16 |
| מַחֲמָאָה *machămâʼâh* (H4260) | something buttery (i.e. unctuous and pleasant), as (figuratively) flattery | Ps 55:22 |
| פְּתִחָה *pᵉthichâh* (H6609) | something opened, i.e. a drawn sword | Ps 55:22 |
| יְהָב *yᵉhâb* (H3053) | properly, what is given (by Providence), i.e. a lot | Ps 55:23 |
| עָקָה *ʻâqâh* (H6125) | constraint | Ps 55:4 |
| מִפְלָט *miphlâṭ* (H4655) | an escape | Ps 55:9 |
| סָעָה *çâʻâh* (H5584) | to rush | Ps 55:9 |
| נוֹד *nôwd* (H5112) | exile | Ps 56:9 |
| מַלְתָּעָה *maltâʻâh* (H4459) | a grinder, i.e. back tooth | Ps 58:7 |
| שַׁבְלוּל *shablûwl* (H7642) | a snail (as if floating in its own slime) | Ps 58:9 |
| תֶּמֶס *temeç* (H8557) | liquefaction, i.e. disappearance | Ps 58:9 |
| נְחִילָה *nᵉchîylâh* (H5155) | a flute | Ps 5:1 |
| שֶׁוַע *shevaʻ* (H7773) | a halloo | Ps 5:3 |
| פָּצַם *pâtsam* (H6480) | to rend (by earthquake) | Ps 60:4 |
| הָתַת *hâthath* (H2050) | properly, to break in upon, i.e. to assail | Ps 62:4 |
| כָּמַהּ *kâmahh* (H3642) | to pine after | Ps 63:2 |
| חֵפֶשׂ *chêphes* (H2665) | something covert, i.e. a trick | Ps 64:7 |
| גְּדוּדָה *gᵉdûwdâh* (H1418) | an incision | Ps 65:11 |
| מוּעָקָה *mûwʻâqâh* (H4157) | pressure, i.e. (figuratively) distress | Ps 66:11 |
| רוֹמָם *rôwmâm* (H7318) | exaltation, i.e. (figuratively and specifically) praise | Ps 66:17 |
| שָׁלַג *shâlag* (H7949) | to be snow-white (with the linen clothing of the slain) | Ps 68:15 |
| רָצַד *râtsad* (H7520) | probably to look askant, i.e. (figuratively) be jealous | Ps 68:17 |
| שִׁנְאָן *shinʼân* (H8136) | change, i.e. repetition | Ps 68:18 |
| מוֹשָׁעָה *môwshâʻâh* (H4190) | deliverance | Ps 68:21 |
| רִגְמָה *rigmâh* (H7277) | a pile (of stones), i.e. (figuratively) a throng | Ps 68:28 |
| רַץ *rats* (H7518) | a fragment | Ps 68:31 |
| חַשְׁמַן *chashman* (H2831) | wealthy | Ps 68:32 |
| תַּעֲצֻמָה *taʻătsumâh* (H8592) | might (plural collective) | Ps 68:36 |
| כּוֹשָׁרָה *kôwshârâh* (H3574) | prosperity; in plural freedom | Ps 68:7 |
| צְחִיחָה *tsᵉchîychâh* (H6707) | a parched region, i.e. the desert | Ps 68:7 |
| אָטַר *ʼâṭar* (H332) | to close up | Ps 69:16 |
| נוּשׁ *nûwsh* (H5136) | to be sick, i.e. (figuratively) distressed | Ps 69:21 |
| בָּרוּת *bârûwth* (H1267) | food | Ps 69:22 |
| מׇעֳמָד *moʻŏmâd* (H4613) | literally a foothold | Ps 69:3 |
| אֻמְלַל *ʼumlal* (H536) | sick | Ps 6:3 |
| חִישׁ *chîysh* (H2439) | to hurry | Ps 71:12 |
| סְפֹרָה *çᵉphôrâh* (H5615) | a numeration | Ps 71:15 |
| גָּזָה *gâzâh* (H1491) | to cut off, i.e. portion out | Ps 71:6 |
| פִּסָּה *piççâh* (H6451) | expansion, i.e. abundance | Ps 72:16 |
| זַרְזִיף *zarzîyph* (H2222) | a pouring rain | Ps 72:6 |
| רָחֵק *râchêq* (H7369) | remote | Ps 73:27 |
| מוּק *mûwq* (H4167) | to jeer, i.e. (intens.) blaspheme | Ps 73:8 |
| כַּשִּׁיל *kashshîyl* (H3781) | properly, a feller, i.e. an axe | Ps 74:6 |
| כֵּילַף *kêylaph* (H3597) | a club or sledge-hammer | Ps 74:6 |
| מֶסֶךְ *meçek* (H4538) | a mixture, i.e. of wine with spices | Ps 75:9 |
| חַנּוֹת *channôwth* (H2589) | supplication | Ps 77:10 |
| שְׁמֻרָה *shᵉmurâh* (H8109) | something guarded, i.e. an eye-lid | Ps 77:5 |
| תָּוָה *tâvâh* (H8428) | to grieve | Ps 78:41 |
| חֲנָמָל *chănâmâl* (H2602) | perhaps the aphis or plantlouse | Ps 78:47 |
| כִּרְסֵם *kirçêm* (H3765) | to lay waste | Ps 80:14 |
| כַּנָּה *kannâh* (H3657) | a plant (as set) | Ps 80:16 |
| יְהוֹסֵף *Yᵉhôwçêph* (H3084) | Jehoseph (i.e. Joseph), a son of Jacob | Ps 81:6 |
| גְּבָל *Gᵉbâl* (H1381) | Gebal, a region in Idumaea | Ps 83:8 |
| סָפַף *çâphaph* (H5605) | to wait at the threshold | Ps 84:11 |
| דּוּר *dûwr* (H1752) | properly, to gyrate (or move in a circle), i.e. to remain | Ps 84:11 |
| בָּכָא *Bâkâʼ* (H1056) | Baca, a valley in Palestine | Ps 84:7 |
| סַלָּח *çallâch* (H5546) | placable | Ps 86:5 |
| יְסוּדָה *yᵉçûwdâh* (H3248) | a foundation | Ps 87:1 |
| נְשִׁיָּה *nᵉshîyâh* (H5388) | oblivion | Ps 88:13 |
| פּוּן *pûwn* (H6323) | be perplexed | Ps 88:16 |
| אֱיָל *ʼĕyâl* (H353) | strength | Ps 88:5 |
| שׂוֹא *sôwʼ* (H7721) | a rising | Ps 89:10 |
| חֲסִין *chăçîyn* (H2626) | properly, firm, i.e. (by implication) mighty | Ps 89:9 |
| רֹהָב *rôhâb* (H7296) | pride | Ps 90:10 |
| חִישׁ *chîysh* (H2440) | properly, a hurry; hence (adverb) quickly | Ps 90:10 |
| סֹחֵרָה *çôchêrâh* (H5507) | something surrounding the person, i.e. a shield | Ps 91:4 |
| שׁוּד *shûwd* (H7736) | properly, to swell up, i.e. figuratively (by implication of insolence) to devastate | Ps 91:6 |
| שִׁלֻּמָה *shillumâh* (H8011) | retribution | Ps 91:8 |
| שׁוּר *shûwr* (H7790) | a foe (as lying in wait) | Ps 92:12 |
| דֳּכִי *dŏkîy* (H1796) | a dashing of surf | Ps 93:3 |
| מֶחְקָר *mechqâr* (H4278) | properly, scrutinized, i.e. (by implication) a recess | Ps 95:4 |
| נוּט *nûwṭ* (H5120) | to quake | Ps 99:1 |
| עָגַן *ʻâgan* (H5702) | to debar, i.e. from marriage | Ruth 1:13 |
| מָרָא *Mârâʼ* (H4755) | Mara, a symbolic name of Naomi | Ruth 1:20 |
| צָבַט *tsâbaṭ* (H6642) | to grasp, i.e. hand out | Ruth 2:14 |
| צֶבֶת *tsebeth* (H6653) | a lock of stalks | Ruth 2:16 |
| טְרוֹם *ṭᵉrôwm* (H2958) | not yet | Ruth 3:14 |
| מוֹדַעַת *môwdaʻath* (H4130) | acquaintance | Ruth 3:2 |
| שַׂלְמָה *Salmâh* (H8009) | Salmah, an Israelite | Ruth 4:20 |
| שַׂלְמוֹן *Salmôwn* (H8012) | Salmon, an Israelite | Ruth 4:21 |
| חָרוּז *chârûwz* (H2737) | properly, pierced, i.e. a bead of pearl, gems or jewels (as strung) | Song 1:10 |
| נְקֻדָּה *nᵉquddâh* (H5351) | a boss | Song 1:11 |
| בְּרוֹת *bᵉrôwth* (H1266) | the cypress (or some elastic tree) | Song 1:17 |
| שְׁחַרְחֹרֶת *shᵉcharchôreth* (H7840) | swarthy | Song 1:6 |
| גְּדִיָּה *gᵉdîyâh* (H1429) | a young female goat | Song 1:8 |
| סוּסָה *çûwçâh* (H5484) | a mare | Song 1:9 |
| נִצָּן *nitstsân* (H5339) | a blossom | Song 2:12 |
| זָמִיר *zâmîyr* (H2159) | a twig (as pruned) | Song 2:12 |
| פַּג *pag* (H6291) | crude; an unripe fig | Song 2:13 |
| בֶּתֶר *Bether* (H1336) | Bether, a (craggy) place in Palestine | Song 2:17 |
| כֹּתֶל *kôthel* (H3796) | a wall (as gathering inmates) | Song 2:9 |
| חֶרֶךְ *cherek* (H2762) | properly, a net, i.e. (by analogy) lattice | Song 2:9 |
| רְפִידָה *rᵉphîydâh* (H7507) | a railing (as spread along) | Song 3:10 |
| רָצַף *râtsaph* (H7528) | to tessellate, i.e. embroider (as if with bright stones) | Song 3:10 |
| חֲתֻנָּה *chăthunnâh* (H2861) | a wedding | Song 3:11 |
| אֲבָקָה *ʼăbâqâh* (H81) | light particles (as volatile) | Song 3:6 |
| אַפִּרְיוֹן *ʼappiryôwn* (H668) | a palanquin | Song 3:9 |
| כַּרְכֹּם *karkôm* (H3750) | the crocus | Song 4:14 |
| תַּלְפִּיָּה *talpîyâh* (H8530) | something tall, i.e. (plural collective) slenderness | Song 4:4 |
| בָּשָׂם *bâsâm* (H1313) | the balsam plant | Song 5:1 |
| תַּלְתַּל *taltal* (H8534) | a trailing bough (as pendulous) | Song 5:11 |
| מִלֵּאת *millêʼth* (H4402) | fulness, i.e. (concretely) a plump socket (of the eye) | Song 5:12 |
| מֶרְקָח *merqâch* (H4840) | a spicy herb | Song 5:13 |
| עֶשֶׁת *ʻesheth* (H6247) | a fabric | Song 5:14 |
| טָנַף *ṭânaph* (H2936) | to soil | Song 5:3 |
| אֱגוֹז *ʼĕgôwz* (H93) | a nut | Song 6:11 |
| דָּבַב *dâbab* (H1680) | to move slowly, i.e. glide | Song 7:10 |
| חַמּוּק *chammûwq* (H2542) | a wrapping, i.e. drawers | Song 7:2 |
| אָמָן *ʼâmân* (H542) | an expert | Song 7:2 |
| שֹׁרֶר *shôrer* (H8326) | the umbilical cord, i.e. (by extension) a bodice | Song 7:3 |
| סַהַר *çahar* (H5469) | roundness | Song 7:3 |
| מֶזֶג *mezeg* (H4197) | tempered wine | Song 7:3 |
| סוּג *çûwg* (H5473) | to hem in, i.e. bind | Song 7:3 |
| סַנְסִן *çançin* (H5577) | a twig (as tapering) | Song 7:9 |
| רֶקַח *reqach* (H7544) | properly, perfumery, i.e. (by implication) spicery (for flavor) | Song 8:2 |
| רָפַק *râphaq* (H7514) | to recline | Song 8:5 |
| אַחֲוָה *ʼachăvâh* (H264) | fraternity | Zech 11:14 |
| אֱוִלִי *ʼĕvilîy* (H196) | silly, foolish; hence (morally) impious | Zech 11:15 |
| נַעַר *naʻar* (H5289) | a wanderer | Zech 11:16 |
| בָּצוֹר *bâtsôwr* (H1208) | inaccessible, i.e. lofty | Zech 11:2 |
| רַעַל *raʻal* (H7478) | a reeling (from intoxication) | Zech 12:2 |
| מַעֲמָסָה *maʻămâçâh* (H4614) | burdensomeness | Zech 12:3 |
| אַמְצָה *ʼamtsâh* (H556) | force | Zech 12:5 |
| רָאַם *râʼam* (H7213) | to rise | Zech 14:10 |
| פֵּן *pên* (H6434) | an angle (of a street or wall) | Zech 14:10 |
| מְצִלָּה *mᵉtsillâh* (H4698) | a tinkler, i.e. a bell | Zech 14:20 |
| שְׁבָט *Shᵉbâṭ* (H7627) | Shebat, a Jewish month | Zech 1:7 |
| מְצֻלָּה *mᵉtsullâh* (H4699) | shade | Zech 1:8 |
| שָׂרֻק *sâruq* (H8320) | bright red (as piercing to the sight), i.e. bay | Zech 1:8 |
| בָּבָה *bâbâh* (H892) | something hollowed (as a gate), i.e. pupil of the eye | Zech 2:12 |
| מַהְלֵךְ *mahlêk* (H4108) | a walking (plural collectively), i.e. access | Zech 3:7 |
| צַנְתָּרָה *tsantârâh* (H6804) | a tube | Zech 4:12 |
| רֹאשָׁה *rôʼshâh* (H7222) | the head | Zech 4:7 |
| מְכֻנָה *mᵉkunâh* (H4369) | a spot | Zech 5:11 |
| חֵלֶם *Chêlem* (H2494) | Chelem, an Israelite | Zech 6:14 |
| חֵן *Chên* (H2581) | Chen, a figurative name for an Israelite | Zech 6:14 |
| חַדְרָךְ *Chadrâk* (H2317) | Chadrak, a Syrian deity | Zech 9:1 |
| בִּצָּרוֹן *bitstsârôwn* (H1225) | a fortress | Zech 9:12 |
| נָסַס *nâçaç* (H5264) | to raise a beacon | Zech 9:16 |
| מַכְתֵּשׁ *Maktêsh* (H4389) | dell; the Maktesh, a place in Jerusalem | Zeph 1:11 |
| נְטִיל *nᵉṭîyl* (H5187) | laden | Zeph 1:11 |
| אַרְזָה *ʼarzâh* (H731) | cedar wainscoating | Zeph 2:14 |
| כָּרָה *kârâh* (H3741) | a meadow | Zeph 2:6 |
| מִמְשָׁק *mimshâq* (H4476) | a possession | Zeph 2:9 |
| מִכְרֶה *mikreh* (H4379) | a pit (for salt) | Zeph 2:9 |
| בֹּגְדוֹת *bôgᵉdôwth* (H900) | treacheries | Zeph 3:4 |

## Quran: top phrase echoes

| Score | Phrase (lemmas) | Count | Places |
|---|---|---|---|
| 41.08 | أَيّ · نَبِيّ · جاهَدَ · كافِر · مُنافِق · اغْلُظْ · مَأْوَى · جَهَنَّم · بِئْسَ · مَصِير | 2 | 66:9, 9:73 |
| 37.81 | رَبّ · أَوْزِعْ · شَكَرَ · نِعْمَة · الَّذِي · أَنْعَمَ · والِدَي · عَمِلَ · صالِح · رَضِيَ | 2 | 27:19, 46:15 |
| 36.87 | إِذا · أَنْعَمَ · إِنسان · أَعْرَضَ · نَأَى · جانِب · إِذا · مَسَّ · شَرّ | 2 | 17:83, 41:51 |
| 34.99 | لَيْسَ · أَعْمَى · حَرَج · أَعْرَج · حَرَج · مَرِيض · حَرَج | 2 | 24:61, 48:17 |
| 34.79 | قالَ · رَبّ · أَوْزِعْ · شَكَرَ · نِعْمَة · الَّذِي · أَنْعَمَ · والِدَي · عَمِلَ · صالِح | 2 | 27:19, 46:15 |
| 34.67 | ما · قالَ · سَبَّحَ · حَمْد · رَبّ · قَبْل · طُلُوع · شَمْس · قَبْل · غُرُوب | 2 | 20:130, 50:39 |
| 33.86 | تَلَى · آيَة · زَكَّى · عَلَّمَ · كِتاب · حِكْمَة · كانَ · قَبْل · ضَلال · مُبِين | 2 | 3:164, 62:2 |
| 33.06 | مَثَل · حَياة · دُنْيا · ماء · أَنزَلَ · سَماء · اخْتَلَطَ · نَبات · أَرْض | 2 | 10:24, 18:45 |
| 32.27 | هَدَى · كَم · أَهْلَكَ · قَبْل · قَرْن · مَشَ · مَسْكَن · ذا · آيَة | 2 | 20:128, 32:26 |
| 31.99 | صَبَرَ · ما · قالَ · سَبَّحَ · حَمْد · رَبّ · قَبْل · طُلُوع · شَمْس · قَبْل | 2 | 20:130, 50:39 |
| 31.88 | جَنَّة · جَرَيْ · تَحْت · نَهَر · خالِد · أَبَدًا · ذا · فَوْز · عَظِيم | 2 | 64:9, 9:100 |
| 31.33 | جَعَلَ · عالِي · سافِل · أُمْطِرَتْ · حِجارَة · سِجِّيل | 2 | 11:82, 15:74 |
| 31.09 | ما · يَلِجَ · أَرْض · ما · خَرَجَ · ما · نَزَلَ · سَماء · ما · يَعْرُجُ | 2 | 34:2, 57:4 |
| 30.43 | جَرَيْ · تَحْت · نَهَر · خالِد · أَبَدًا · رَضِيَ · اللَّه · رَضِيَ · ذا | 2 | 5:119, 98:8 |
| 29.68 | لَمّا · جاءَ · رَسُول · لُوط · ساءَ · ضاقَ · ذَرْع · قالَ | 2 | 11:77, 29:33 |
| 29.65 | نَزَغَ · شَيْطان · نَزْغ · اسْتَعِذْ · اللَّه · سَمِيع · عَلِيم | 2 | 41:36, 7:200 |
| 28.99 | اسْتُهْزِئَ · رَسُول · قَبْل · حاقَ · الَّذِي · سَخِرَ · ما · كانَ · اسْتُهْزِئَ | 2 | 21:41, 6:10 |
| 28.89 | الَّذِي · خَلَقَ · سَماء · أَرْض · ما · بَيْن · سِتَّة · يَوْم · اسْتَوَى · عَرْش | 2 | 25:59, 32:4 |
| 28.67 | دَعا · دُون · اللَّه · أَرَيْ · ماذا · خَلَقَ · أَرْض · شِرْك · سَماء | 2 | 35:40, 46:4 |
| 28.51 | جَرَيْ · تَحْت · نَهَر · حُلُّ · أَساوِر · ذَهَب | 2 | 18:31, 22:23 |
| 28.21 | دَخَلَ · باب · جَهَنَّم · خالِد · بِئْسَ · مَثْوًى · مُتَكَبِّر | 3 | 16:29, 39:72, 40:76 |
| 27.95 | يَذَرَ · خاضُ · يَلْعَبْ · يُلاقُ · يَوْم · الَّذِي · وَعَدَ | 2 | 43:83, 70:42 |
| 27.74 | اللَّه · أُدْخِلَ · الَّذِي · آمَنَ · عَمِلَ · صالِحَة · جَنَّة · جَرَيْ · تَحْت · نَهَر | 3 | 22:14, 22:23, 47:12 |
| 27.7 | عَلِمَ · ما · يَلِجَ · أَرْض · ما · خَرَجَ · ما · نَزَلَ · سَماء · ما | 2 | 34:2, 57:4 |
| 27.6 | أَرْسَلَ · قَبْل · رِجال · أَوْحَى · سَأَلَ · أَهْل · ذِكْر · كانَ · عَلِمَ | 2 | 16:43, 21:7 |
| 26.94 | أُمْطِرَتْ · مَطَر · ساءَ · مَطَر · مُنذَر | 2 | 26:173, 27:58 |
| 26.59 | مَن · ذا · الَّذِي · أَقْرَضُ · اللَّه · قَرْض · حَسَن · يُضاعِفُ | 2 | 2:245, 57:11 |
| 26.31 | الَّذِي · أَرْسَلَ · رَسُول · هُدًى · دِين · حَقّ · أَظْهَرَ · دِين · كُلّ | 3 | 48:28, 61:9, 9:33 |
| 26.24 | قالَ · ضَعِيف · الَّذِي · اسْتَكْبَرَ · كانَ · تَبَع · مُغْني | 2 | 14:21, 40:47 |
| 26.15 | جَنَّة · جَرَيْ · تَحْت · نَهَر · خالِد · ذا · فَوْز · عَظِيم | 3 | 4:13, 57:12, 9:89 |
| 25.82 | أَقامَ · صَلاة · أَنفَقَ · ما · رَزَقَ · سِرّ · عَلانِيَة | 3 | 13:22, 14:31, 35:29 |
| 25.79 | أُدْخِلَ · الَّذِي · آمَنَ · عَمِلَ · صالِحَة · جَنَّة · جَرَيْ · تَحْت · نَهَر | 4 | 14:23, 22:14, 22:23, 47:12 |
| 25.5 | سَخَّرَ · شَمْس · قَمَر · كُلّ · جَرَيْ · أَجَل · مُسَمًّى | 4 | 13:2, 31:29, 35:13, 39:5 |
| 25.18 | جَعَلَ · قَلْب · أَكِنَّة · يَفْقَهُ · أُذُن · وَقْر | 3 | 17:46, 18:57, 6:25 |
| 25.16 | باقِيَة · صالِحَة · خَيْر · عِند · رَبّ · ثَواب · خَيْر | 2 | 18:46, 19:76 |
| 24.96 | كَفَّرَ · سَيِّئَة · أُدْخِلَ · جَنَّة · جَرَيْ · تَحْت · نَهَر | 4 | 3:195, 5:12, 64:9, 66:8 |
| 24.75 | جَعَلَ · سَمْع · بَصَر · فُؤاد · قَلِيل · ما · شَكَرَ | 2 | 32:9, 67:23 |
| 24.39 | مَن · أَتَى · عَذاب · أَخْزَيْ · حَلَلْ · عَذاب · مُقِيم | 2 | 11:39, 39:40 |
| 24.37 | الَّذِي · دَعا · رَبّ · غَداة · عَشِيّ · أَرادَ · وَجْه | 2 | 18:28, 6:52 |
| 24.33 | قالَ · مَلَك · سَجَدَ · آدَم · سَجَدَ · إِبْلِيس · كانَ | 2 | 18:50, 7:11 |
| 24.32 | آتَى · ذُو · قُرْبَى · حَقّ · مِسْكِين · ابْن · سَبِيل | 2 | 17:26, 30:38 |
| 24.23 | أُسْوَة · حَسَنَة · مَن · كانَ · يَرْجُوا۟ · اللَّه · يَوْم · آخِر | 2 | 33:21, 60:6 |
| 24.21 | أُدْخِلَ · جَنَّة · جَرَيْ · تَحْت · نَهَر · خالِد · أَبَدًا | 4 | 4:122, 4:57, 64:9, 65:11 |
| 24.08 | الَّذِي · أَرْسَلَ · رِيح · بُشْر · بَيْن · يَد · رَحْمَة | 2 | 25:48, 7:57 |
| 24.03 | قالَ · إِذا · ماتَ · كانَ · تُراب · عِظام · مَبْعُوث | 2 | 23:82, 56:47 |
| 23.94 | ذا · فَضْل · اللَّه · آتَى · مَن · شاءَ · اللَّه · ذُو · فَضْل · عَظِيم | 2 | 57:21, 62:4 |
| 23.89 | ذُو · أَرْحام · بَعْض · أَوْلَى · بَعْض · كِتاب · اللَّه | 2 | 33:6, 8:75 |
| 23.64 | الَّذِي · خَلَقَ · سَماء · أَرْض · سِتَّة · يَوْم · اسْتَوَى · عَرْش | 3 | 10:3, 57:4, 7:54 |
| 23.37 | يَبْخَسْ · ناس · شَىْء · تَعْثَ · أَرْض · مُفْسِد | 2 | 11:85, 26:183 |
| 23.32 | يُولِجُ · لَيْل · نَهار · يُولِجُ · نَهار · لَيْل | 5 | 22:61, 31:29, 35:13, 3:27, 57:6 |
| 23.28 | أَخْرَجَ · حَيّ · مَيِّت · أَخْرَجَ · مَيِّت · حَيّ | 3 | 10:31, 30:19, 3:27 |
| 23.24 | إِذ · قالَ · مَلَك · سَجَدَ · آدَم · سَجَدَ · إِبْلِيس | 4 | 17:61, 18:50, 20:116, 2:34 |
| 23.21 | جَنَّة · عَدْن · جَرَيْ · تَحْت · نَهَر · خالِد | 2 | 20:76, 98:8 |
| 23.16 | قالَ · بَشَر · مِثْل · أَوْحَى · إِلٰه · إِلٰه · واحِد | 2 | 18:110, 41:6 |
| 23.09 | أَرْض · مَدَّ · أَلْقَى · رَواسِي · أَنۢبَتَ · كُلّ | 2 | 15:19, 50:7 |
| 22.61 | سارَ · أَرْض · نَظَرَ · كَيْف · كانَ · عاقِبَة · الَّذِي · قَبْل · كانَ | 4 | 30:42, 30:9, 35:44, 40:82 |
| 22.32 | قالَ · الَّذِي · كَفَرَ · حَقّ · لَمّا · جاءَ · ذا · سِحْر · مُبِين | 2 | 34:43, 46:7 |
| 22.04 | مال · وَلَد · فِتْنَة · اللَّه · عِند · أَجْر · عَظِيم | 2 | 64:15, 8:28 |
| 21.99 | جَعَلَ · اللَّه · أَنداد · أَضَلَّ · سَبِيل · قالَ · تَمَتَّعَ | 2 | 14:30, 39:8 |
| 21.83 | كانَ · فِئَة · نَصَرَ · دُون · اللَّه · كانَ · مُنتَصِر | 2 | 18:43, 28:81 |
| 21.78 | مَن · وَجَدَ · صِيام · شَهْر · مُتَتابِعَيْن | 2 | 4:92, 58:4 |
| 21.77 | ذا · نَبَأ · غَيْب · أَوْحَى · كانَ · لَدَى · إِذ | 2 | 12:102, 3:44 |
| 21.77 | خاسِر · الَّذِي · خَسِرَ · نَفْس · أَهْل · يَوْم · قِيامَة | 2 | 39:15, 42:45 |
| 21.74 | رَبّ · أَعْلَم · مَن · ضَلَّ · سَبِيل · أَعْلَم · مُهْتَدي | 3 | 16:125, 68:7, 6:117 |
| 21.69 | اللَّه · بَسَطَ · رِزْق · مَن · شاءَ · عَبْد · قَدَرَ | 2 | 28:82, 29:62 |
| 21.69 | الَّذِي · أَحْصَنَتْ · فَرْج · نَفَخَ · رُوح | 2 | 21:91, 66:12 |
| 21.64 | أَرْسَلَ · رِيح · بُشْر · بَيْن · يَد · رَحْمَة | 3 | 25:48, 27:63, 7:57 |
| 21.64 | إِذا · ماتَ · كانَ · تُراب · عِظام · مَبْعُوث | 3 | 23:82, 37:16, 56:47 |
| 21.59 | صَدَّ · سَبِيل · اللَّه · مَن · آمَنَ · بَغَى · عِوَج | 2 | 3:99, 7:86 |
| 21.57 | مَن · وَقَى · شُحّ · نَفْس · ذا · مُفْلِح | 2 | 59:9, 64:16 |
| 21.52 | ظَلَّ · وَجْه · مُسْوَدّ · كَظِيم | 2 | 16:58, 43:17 |
| 21.45 | تَلَى · آيَة · زَكَّى · عَلَّمَ · كِتاب · حِكْمَة | 3 | 2:151, 3:164, 62:2 |
| 21.45 | مُلِئَتْ · جَهَنَّم · جِنَّة · ناس · أَجْمَع | 2 | 11:119, 32:13 |
| 21.44 | اتَّخَذَ · يَمِين · جُنَّة · صَدَّ · سَبِيل · اللَّه | 2 | 58:16, 63:2 |
| 21.43 | مَن · نَصِير · اللَّه · قالَ · حَوارِيّ · نَصِير · اللَّه · آمَنَ | 2 | 3:52, 61:14 |
| 21.29 | غَفَرَ · ذَنب · أَخَّرَ · أَجَل · مُسَمًّى | 2 | 14:10, 71:4 |
| 21.27 | اسْم · سَمَّى · آباء · أَنزَلَ · اللَّه · سُلْطان | 2 | 12:40, 53:23 |
| 21.24 | نَعَم · عِبْرَة · أَسْقَيْ · ما · بَطْن | 2 | 16:66, 23:21 |
| 21.21 | مَن · أَظْلَم · مَن · ذُكِّرَ · آيَة · رَبّ · أَعْرَضَ | 2 | 18:57, 32:22 |
| 21.2 | سَمْع · بَصَر · فُؤاد · قَلِيل · ما · شَكَرَ | 3 | 23:78, 32:9, 67:23 |
| 21.17 | الَّذِي · اجْتَنَبُ · كَبِيرَة · إِثْم · فاحِشَة | 2 | 42:37, 53:32 |
| 21.02 | إِذا · أَنزَلَ · ماء · اهْتَزَّتْ · رَبَتْ | 2 | 22:5, 41:39 |
| 20.89 | الَّذِي · آمَنَ · عَمِلَ · صالِحَة · جَنَّة · جَرَيْ · تَحْت · نَهَر | 6 | 14:23, 22:14, 22:23, 2:25, 47:12, 85:11 |
| 20.83 | الَّذِي · آمَنَ · عَمِلَ · صالِحَة · أَجْر · غَيْر · مَمْنُون | 3 | 41:8, 84:25, 95:6 |
| 20.79 | الَّذِي · كَفَرَ · كَذَّبَ · آيَة · ذا · أَصْحاب · نار · خالِد | 2 | 2:39, 64:10 |
| 20.65 | جَرَيْ · تَحْت · نَهَر · خالِد · ذا · جَزاء | 2 | 20:76, 5:85 |
| 20.37 | إِقام · صَلاة · إِيتاء · زَكاة | 2 | 21:73, 24:37 |
| 20.35 | قالَ · مَلَك · سَجَدَ · آدَم · سَجَدَ · إِبْلِيس | 5 | 17:61, 18:50, 20:116, 2:34, 7:11 |
| 20.26 | أَقامَ · صَلاة · آتَى · زَكاة · أَطاعَ · اللَّه · رَسُول | 3 | 33:33, 58:13, 9:71 |
| 20.23 | أَتْبَعَ · ذا · دُنْيا · لَعْنَة · يَوْم · قِيامَة | 2 | 11:60, 28:42 |
| 20.21 | ذَكَر · أُنثَى · مُؤْمِن · ذا · دَخَلَ · جَنَّة | 2 | 40:40, 4:124 |
| 20.2 | رَفَعَ · بَعْض · فَوْق · بَعْض · دَرَجَة | 2 | 43:32, 6:165 |
| 20.19 | سارَ · أَرْض · نَظَرَ · كَيْف · كانَ · عاقِبَة · الَّذِي · قَبْل | 6 | 12:109, 30:42, 30:9, 35:44, 40:82, 47:10 |
| 20.19 | سَيِّئَة · ما · عَمِلَ · حاقَ · ما · كانَ · اسْتُهْزِئَ | 2 | 16:34, 45:33 |
| 20.14 | الَّذِي · خَلَقَ · سَماء · أَرْض · قادِر · خَلَقَ · مِثْل | 2 | 17:99, 36:81 |
| 20.13 | أَقْرَضُ · اللَّه · قَرْض · حَسَن · يُضاعِفُ | 4 | 2:245, 57:11, 57:18, 64:17 |
| 20.13 | أَرَيْ · بَرْق · خَوْف · طَمَع | 2 | 13:12, 30:24 |
| 20.13 | خاشِع · بَصَر · يَرْهَقُ · ذِلَّة | 2 | 68:43, 70:44 |
| 19.94 | مَن · عَمِلَ · صالِح · ذَكَر · أُنثَى · مُؤْمِن | 2 | 16:97, 40:40 |
| 19.93 | طَلَعَ · إِلٰه · مُوسَى · ظَنَّ · كاذِب | 2 | 28:38, 40:37 |

## Quran: rootless lemmas (loanword candidates, 134)

| Lemma | Count | First place |
|---|---|---|
| مِن | 3226 | 2:3 |
| ما | 2565 | 2:3 |
| لا | 1742 | 1:7 |
| فِي | 1701 | 2:2 |
| إِنّ | 1682 | 2:6 |
| الَّذِي | 1468 | 1:7 |
| عَلَى | 1445 | 1:7 |
| ذا | 1058 | 2:2 |
| مَن | 871 | 2:8 |
| إِلَى | 742 | 2:4 |
| إِن | 703 | 2:23 |
| إِلّا | 659 | 2:9 |
| أَن | 616 | 2:26 |
| عَن | 465 | 2:36 |
| إِذا | 423 | 2:11 |
| قَد | 406 | 2:60 |
| أَنّ | 362 | 2:25 |
| لَم | 348 | 2:6 |
| ثُمّ | 338 | 2:28 |
| إِذ | 309 | 2:30 |
| أَو | 280 | 2:19 |
| لَو | 201 | 2:20 |
| لَمّا | 165 | 2:17 |
| مَع | 164 | 2:14 |
| ذُو | 156 | 2:83 |
| حَتَّى | 142 | 2:55 |
| أَم | 137 | 2:6 |
| مُوسَى | 136 | 2:51 |
| لَعَلّ | 129 | 2:21 |
| بَل | 127 | 2:88 |
| لَن | 106 | 2:24 |
| هَل | 93 | 2:210 |
| جَهَنَّم | 77 | 2:206 |
| لَوْلا | 75 | 2:64 |
| فِرْعَوْن | 74 | 2:49 |
| إِبْراهِيم | 69 | 2:124 |
| لٰكِن | 65 | 2:12 |
| لٰكِنّ | 65 | 2:102 |
| أَمّا | 55 | 2:26 |
| إِسْرائِيل | 43 | 2:40 |
| نُوح | 43 | 3:33 |
| سَوْف | 42 | 4:30 |
| وَيْل | 40 | 2:79 |
| أَلا | 39 | 2:12 |
| مَرْيَم | 34 | 2:87 |
| كَلّا | 33 | 19:79 |
| كَأَنّ | 31 | 2:101 |
| إِذًا | 31 | 2:145 |
| أَنَّى | 28 | 2:223 |
| يُوسُف | 27 | 6:84 |
| لُوط | 27 | 6:86 |
| ماذا | 26 | 2:26 |
| ثَمُود | 26 | 7:73 |
| عِيسَى | 25 | 2:87 |
| إِيّا | 24 | 1:5 |
| إِمّا | 23 | 2:38 |
| بَلَى | 22 | 2:81 |
| لَدَى | 22 | 3:44 |
| كَم | 21 | 2:211 |
| هارُون | 20 | 2:248 |
| أَيْن | 19 | 2:115 |
| تَوْراة | 18 | 3:3 |
| سُلَيْمان | 17 | 2:102 |
| إِسْحاق | 17 | 2:133 |
| يَعْقُوب | 16 | 2:132 |
| داوُد | 16 | 2:251 |
| لَيْت | 14 | 4:73 |
| إِسْماعِيل | 12 | 2:125 |
| إِنجِيل | 12 | 3:3 |
| إِبْلِيس | 11 | 2:34 |
| شُعَيْب | 11 | 7:85 |
| عَدْن | 11 | 9:72 |
| كَي | 10 | 3:153 |
| مَتَى | 9 | 2:214 |
| هُنالِك | 9 | 3:38 |
| كَأَنْ | 9 | 4:73 |
| زَكَرِيّا | 7 | 3:37 |
| كَأَيِّن | 7 | 3:146 |
| أَيّان | 6 | 7:187 |
| هامان | 6 | 28:6 |
| ثَمّ | 4 | 2:115 |
| هُنا | 4 | 3:154 |
| أَيُّوب | 4 | 4:163 |
| يُونُس | 4 | 4:163 |
| أَمْس | 4 | 10:24 |
| أَيْكَة | 4 | 15:78 |
| إِسْتَبْرَق | 4 | 18:31 |
| قارُون | 4 | 28:76 |
| سَقَر | 4 | 54:48 |
| جِبْرِيل | 3 | 2:97 |
| جالُوت | 3 | 2:249 |
| عِمْران | 3 | 3:33 |
| إِلْياس | 3 | 6:85 |
| سُندُس | 3 | 18:31 |
| طالُوت | 2 | 2:247 |
| تابُوت | 2 | 2:248 |
| الْيَسَع | 2 | 6:86 |
| تَنُّور | 2 | 11:40 |
| يَأْجُوج | 2 | 18:94 |
| مَأْجُوج | 2 | 18:94 |
| فِرْدَوْس | 2 | 18:107 |
| إِدْرِيس | 2 | 19:56 |
| هَيْهات | 2 | 23:36 |
| وَيْ | 2 | 28:82 |
| لُقْمان | 2 | 31:12 |
| تُبَّع | 2 | 44:37 |
| مِيكال | 1 | 2:98 |
| بابِل | 1 | 2:102 |
| هارُوت | 1 | 2:102 |
| مارُوت | 1 | 2:102 |
| صَفا | 1 | 2:158 |
| بَكَّة | 1 | 3:96 |
| بَدْر | 1 | 3:123 |
| آزَر | 1 | 6:74 |
| مَهْما | 1 | 7:132 |
| حُنَيْن | 1 | 9:25 |
| عُزَيْر | 1 | 9:30 |
| إِي | 1 | 10:53 |
| رُب | 1 | 15:2 |
| سَيْناء | 1 | 23:20 |
| رُوم | 1 | 30:2 |
| يَثْرِب | 1 | 33:13 |
| زَيْد | 1 | 33:37 |
| يَقْطِين | 1 | 37:146 |
| مَكَّة | 1 | 48:24 |
| اللّات | 1 | 53:19 |
| ياقُوت | 1 | 55:58 |
| لَظَى | 1 | 70:15 |
| يَغُوث | 1 | 71:23 |
| يَعُوق | 1 | 71:23 |
| زَنجَبِيل | 1 | 76:17 |
| سَلْسَبِيل | 1 | 76:18 |
| إِرَم | 1 | 89:7 |
| سِينِين | 1 | 95:2 |
