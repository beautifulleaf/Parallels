# The hadith corpus: scope

## The text

***al-Jāmiʿ al-Kāmil fī l-ḥadīth al-ṣaḥīḥ al-shāmil al-murattab ʿalā abwāb al-fiqh***, by Muḥammad
Ḍiyāʾ al-Raḥmān al-Aʿẓamī (d. 1441/2020). Shamela book 47, in 12 printed volumes.

- **Arrangement:** 67 books (*kutub*) on 8,581 Shamela pages (ids 106–8686), listed with their page
  ranges in `books.yaml`.
- **Not read:** pages 5–105 are the compiler's introduction and page 8687 the conclusion. They hold
  no hadith.
- **Publication data:** Shamela's catalogue records no edition, editor or publisher. The book's own
  front matter, at the title pages of volumes 8 and 9 (Shamela pp. 5021–5024 and 5809–5812), prints:
  Dār al-Salām, Riyadh, first edition, Rabīʿ II 1437 / January 2016, with ISBNs. That is the
  edition read here, as reported independently by the readers of chunks 2 and 8. No editor is
  named.
- **What the book is:** a gathering of the reports the compiler judged ṣaḥīḥ or ḥasan, each followed
  by his grade and takhrij. The grades are his, recorded as his. The project grades nothing.
- **What is not in it:** *isrāʾīliyyāt* (reports drawn from Jewish and Christian lore) are largely
  absent, and the compiler names them as such where he mentions them. A later *isrāʾīliyyāt* layer
  would be a separate corpus (`docs/CLEANUP.md`).

## Access and licence

- **Source:** the text reaches the project only through the Shamela MCP tools, which read the
  user's own Shamela library.
- **No web fetching:** shamela.ws disallows Anthropic's crawlers in its robots.txt, so nothing is
  fetched from the website.
- **Copyright:** the compilation is modern and copyrighted. The saved hadith text
  (`data/raw/hadith/`) stays out of git. What the repo holds are the motif tags, the records and
  short quotations of decisive words.

## The read

`python3 tools/hadith.py plan` divides the corpus into 73 chunks of about 120 pages.
- **Order:** the books that carry narrative and cosmology come first: 1 (revelation), 45 (the
  beginning of creation), 46 (past peoples), 47 (the prophets), 48 (the sīra), 58 (dreams),
  60 (tafsir), 65 (trials and the Hour), 66 (the Resurrection) and 67 (paradise and hell).
  The legal and other books follow in the book's order.
- **What a reader saves:** each hadith's matn, the first transmitter, the compiler's grade, the
  takhrij and the verses it explains, as one line in `data/raw/hadith/NN.json`.
- **References:** `Jāmiʿ <book>:<page_id>.<k>`, the k-th hadith beginning on that page. Each line
  also keeps the printed page for citation.

## Not yet done

- **Canonical links:** the Hadith MCP tools return a canonical id and URL for hadith of the major
  collections. They will be looked up for the hadith that end up in leads, not for all of them.
