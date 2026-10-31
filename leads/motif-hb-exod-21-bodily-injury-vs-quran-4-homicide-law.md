---
id: motif-hb-exod-21-bodily-injury-vs-quran-4-homicide-law
title: Covenant Code - homicide, injury and the goring ox ↔ Accidental and deliberate killing of a believer
summary: '2 correspondences read side by side: 2 deliberately changed.'
status: new
relations:
- response
standing: proposed
traditions:
- judaism
- islam
layers:
- motif
motifs:
- city-of-refuge-accidental-killer
- penalty-for-deliberate-murder-as-divergence
- city-of-refuge-accidental-killer-as-divergence
passages: []
evidence:
- text: Read side by side in both originals (alignments/hb-quran/02-hb-quran.yaml).
  basis: reading
- text: 'Shared motifs, rarest first: A place of refuge for one who kills unintentionally (weight 7.7);
    The penalty for deliberate murder [divergence between the texts] (weight 7.7); A place of refuge for
    one who kills unintentionally [divergence between the texts] (weight 7.1). Pair score 22.5.'
  basis: reading
- text: 'Only in Covenant Code - homicide, injury and the goring ox: An animal that kills a person is
    stoned and its flesh not eaten; Men fighting strike a pregnant woman and she miscarries; One who injures
    another pays for his lost time and his healing; Whoever strikes a man so that he dies shall be put
    to death; A master who beats his slave to death is punished, unless the slave survives a day or two;
    Laws of the goring ox and the warned owner; A slave whose eye or tooth the master destroys goes free;
    Striking or cursing father or mother is a capital crime; The owner of an uncovered pit pays for an
    animal that falls in; A deliberate murderer is taken even from God''s altar; Whether one who takes
    refuge at the sanctuary is safe [contrast between the texts]; Kidnapping and selling a person is a
    capital crime; and 7 more.'
  basis: reading
- text: 'Only in Accidental and deliberate killing of a believer: Deliberate killing of a believer is
    punished by hell forever, God''s wrath and curse; Do not tell one who greets you with peace ''you
    are not a believer'' to seize booty; Whoever cannot pay the expiation fasts two consecutive months;
    Accidental killing of a believer: free a believing slave and pay blood money (diya) to the family
    unless they remit it; Blood compensation paid to the kin of a man killed who belongs to a people bound
    by treaty; Murder distinguished from manslaughter by weapon (iron, stone, wood), enmity and intent;
    Whether payment may substitute for a life [contrast between the texts]; Whether payment may substitute
    for a life.'
  basis: reading
- text: 'Covenant Code - homicide, injury and the goring ox: tagged by Claude (model), reading the Hebrew.'
  basis: reading
- text: 'Accidental and deliberate killing of a believer: tagged by Claude (model), reading the Arabic.'
  basis: reading
origin: pipeline
added: '2026-10-29'
finding: The penalty for deliberate murder
kinds:
- divergence
units:
- id: hb-exod-21-bodily-injury
  title: Covenant Code - homicide, injury and the goring ox
  tradition: judaism
- id: quran-4-homicide-law
  title: Accidental and deliberate killing of a believer
  tradition: islam
matches:
- kind: divergence
  label: The penalty for deliberate murder
  note: 'HB punishes deliberate murder on earth: makkēh ʾîš wā-mēt môt yûmāt; even from the altar, kî-yāzid
    ʾîš ... bə-ʿormāh mēʿim mizbəḥî tiqqāḥennû lāmût. Q 4:93 sets no human penalty here: fa-jazāʾuhu jahannamu
    khālidan fīhā wa-ghaḍiba llāhu ʿalayhi wa-laʿanahu.'
  sides:
  - tradition: judaism
    passages:
    - ref: Exod 21:12
      lang: he
      text: מַכֵּ֥ה אִ֛ישׁ וָמֵ֖ת מ֥וֹת יוּמָֽת
    - ref: Exod 21:14
      lang: he
      text: וְכִֽי יָזִ֥ד אִ֛ישׁ עַל רֵעֵ֖הוּ לְהָרְג֣וֹ בְעָרְמָ֑ה מֵעִ֣ם מִזְבְּחִ֔י תִּקָּחֶ֖נּוּ לָמֽוּת
  - tradition: islam
    passages:
    - ref: Quran 4:93
      lang: ar
      text: وَمَن يَقْتُلْ مُؤْمِنًا مُّتَعَمِّدًا فَجَزَآؤُهُۥ جَهَنَّمُ خَٰلِدًا فِيهَا وَغَضِبَ ٱللَّهُ
        عَلَيْهِ وَلَعَنَهُۥ وَأَعَدَّ لَهُۥ عَذَابًا عَظِيمًا
- kind: divergence
  label: A place of refuge for one who kills unintentionally
  note: 'Exod: waʾăšer lōʾ ṣādāh wə-hāʾĕlōhîm ʾinnāh lə-yādô wə-śamtî ləkā māqôm ʾăšer yānûs šāmmāh. Unintentional
    killing is ascribed to God, and asylum is the remedy. Q: wa-mā kāna li-muʾminin an yaqtula muʾminan
    illā khaṭaʾan, with expiation (kaffāra, diya) and a fast as tawbatan mina llāh.'
  sides:
  - tradition: judaism
    passages:
    - ref: Exod 21:13
      lang: he
      text: וַאֲשֶׁר֙ לֹ֣א צָדָ֔ה וְהָאֱלֹהִ֖ים אִנָּ֣ה לְיָד֑וֹ וְשַׂמְתִּ֤י לְךָ֙ מָק֔וֹם אֲשֶׁ֥ר יָנ֖וּס
        שָֽׁמָּה
  - tradition: islam
    passages:
    - ref: Quran 4:92
      lang: ar
      text: وَمَا كَانَ لِمُؤْمِنٍ أَن يَقْتُلَ مُؤْمِنًا إِلَّا خَطَـًٔا وَمَن قَتَلَ مُؤْمِنًا خَطَـًٔا
        فَتَحْرِيرُ رَقَبَةٍ مُّؤْمِنَةٍ وَدِيَةٌ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦٓ إِلَّآ أَن يَصَّدَّقُوا۟
        فَإِن كَانَ مِن قَوْمٍ عَدُوٍّ لَّكُمْ وَهُوَ مُؤْمِنٌ فَتَحْرِيرُ رَقَبَةٍ مُّؤْمِنَةٍ وَإِن
        كَانَ مِن قَوْمٍۭ بَيْنَكُمْ وَبَيْنَهُم مِّيثَٰقٌ فَدِيَةٌ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦ وَتَحْرِيرُ
        رَقَبَةٍ مُّؤْمِنَةٍ فَمَن لَّمْ يَجِدْ فَصِيَامُ شَهْرَيْنِ مُتَتَابِعَيْنِ تَوْبَةً مِّنَ ٱللَّهِ
        وَكَانَ ٱللَّهُ عَلِيمًا حَكِيمًا
---

## Questions

## Notes
