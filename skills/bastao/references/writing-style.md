# Writing style: write like a person

The people who read these documents are a school secretary, a director, an IT technician. Text that sounds like a machine wrote it gets skimmed, then ignored. So every sentence the skill writes into the six documents, in French or in Portuguese, follows the rules below. The skill applies them itself; it does not depend on any other skill being installed. The list comes from Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup), adapted to French and Brazilian Portuguese and to documents read by people in a hurry.

## The checklist, run on every document before step 5

1. No long dash (—) as punctuation. Use a comma, a period, a colon or parentheses. The templates have none; do not add any when filling them.
2. No bold label at the start of a list item ("**Vérification :** ..."). A plain lead-in with a colon, or a full sentence.
3. Headings in sentence case. Never Title Case.
4. Quotes: « » in French, straight "..." in Portuguese. Never curly English quotes.
5. No emoji, no decorative symbols, no middle dots as separators.
6. Simple verbs. "est", "a", "sert à", "fait" in French; "é", "tem", "serve para", "faz" in Portuguese. Not "constitue", "représente", "se présente comme", "permet d'assurer"; not "constitui", "representa", "se configura como", "possibilita garantir".
7. No inflated vocabulary. The lists are below; the checker flags them.
8. No participle tails that fake depth: "..., assurant ainsi la sécurité", "..., garantindo assim a segurança". Cut the tail or make it a sentence with a subject.
9. No rhetorical pairs: "non seulement... mais aussi", "não só... mas também", "ce n'est pas X, c'est Y", "não é X, é Y". No trailing fragments tacked after a comma ("sans exception", "sem exceção").
10. No forced triads. Lists have as many items as the facts need. "The three things never to do" is a space limit set by the template, not a figure of speech.
11. The same word for the same thing, every time. The owner is "le propriétaire" / "o dono" in all six documents; the technical referent is "le référent technique" / "a referência técnica"; the system has one name. Synonyms confuse a successor.
12. No vague attribution ("on considère que", "il est généralement admis", "especialistas apontam"). Every fact comes from the repository, from a named person's answer, or carries the marker.
13. No hedging stacks ("pourrait potentiellement", "poderia eventualmente"). Say what is known; mark what is not.
14. No announcements ("Voyons maintenant", "Dans cette section", "Vamos ver agora"), no "challenges and outlook" paragraphs, no upbeat closing line ("Bonne continuation !", "Sucesso!").
15. No chatbot residue: "j'espère que cela vous aide", "n'hésitez pas", "espero ter ajudado", "fique à vontade".
16. Active voice when the doer matters. Procedures in document 3 use the infinitive; document 4 uses the imperative with "vous" / "você"; document 6 is in the first person without gendered forms ("par moi-même", "sans aide", "por conta própria").
17. Rhythm: sentences under 25 words, a short one after a long one, paragraphs of three sentences at most, one idea per line in lists.
18. Specifics over adjectives: names, dates, numbers, screens, buttons. "Le voyant vert de la caméra de l'entrée", not "l'équipement concerné". "A luz verde da câmera da entrada", not "o equipamento em questão".
19. Dates as DD/MM/YYYY. Times with the zone when server time and local time differ.
20. The last pass, in your head, as the person who will receive the document: "what here sounds like a machine wrote it?" Fix those lines. Then: "would this person know what to do at 8 a.m. with people waiting at the gate?" If not, the document is not finished.

## Words the checker flags in French

Significance inflation: crucial, essentiel (figurative), pivot, pierre angulaire, s'inscrit dans, témoigne de, souligne, met en lumière, met en exergue, reflète, incarne, dans un contexte de, en constante évolution, au cœur de, à l'ère de, paysage (figurative).
Promotional: robuste, fluide, transparent (figurative), optimiser, optimal, innovant, performant, de pointe, incontournable, riche (figurative), puissant (figurative).
Filler and ceremony: il convient de noter que, il est important de noter que, il est à noter que, dans le cadre de, afin de (use "pour"), ainsi que (use "et"), ce dernier / cette dernière (name the thing), dès lors, en effet (as a filler), par ailleurs (as a filler), notamment (when nothing follows), de manière à, en termes de, au niveau de (figurative), la question se pose de, force est de constater.
Vague authority: on considère que, il est généralement admis, les experts, de nombreux observateurs, selon certaines sources.
Rhetoric: non seulement, mais aussi, mais également, il ne s'agit pas seulement de, ce n'est pas tant.

## Words the checker flags in Portuguese

Significance inflation: crucial, fundamental (figurative), essencial (figurative), pilar, pedra angular, se insere em, reflete, ressalta, destaca, evidencia, no contexto de, em constante evolução, no cerne de, na era de, cenário (figurative), panorama (figurative).
Promotional: robusto, fluido, transparente (figurative), otimizar, otimizado, inovador, de ponta, imprescindível, rico (figurative), poderoso (figurative).
Filler and ceremony: vale ressaltar, vale destacar, é importante notar que, cabe mencionar, no âmbito de, a fim de (use "para"), bem como (use "e"), o mesmo / a mesma (as a pronoun), por meio de (use "com" or "por"), realizar (use "fazer"), efetuar, viabilizar, impactar, de modo a, em termos de, a nível de, no que tange a, no que diz respeito a, uma vez que (as a filler), haja vista.
Vague authority: considera-se que, é consenso que, especialistas apontam, muitos observadores, segundo algumas fontes.
Rhetoric: não só, não apenas, mas também, não se trata apenas de, não é tanto.

## Before and after

French, document 1:

Before: "Le système constitue un outil essentiel qui permet de garantir une gestion fluide et optimisée des accès, assurant ainsi la sécurité de l'établissement."
After: "Le système enregistre qui entre et qui sort par le portail et par la cantine. Il ne ferme aucune porte."

French, document 4:

Before: "**Vérification :** Il convient de s'assurer que l'équipement concerné est opérationnel et que la connexion réseau est fonctionnelle."
After: "Vérifiez d'abord, sans risque : le voyant vert de la caméra de l'entrée est-il allumé ?"

Portuguese, document 1:

Before: "O sistema representa uma ferramenta fundamental que possibilita otimizar a gestão de acessos, garantindo assim a segurança da instituição."
After: "O sistema registra quem entra e quem sai pelo portão e pela cantina. Ele não tranca nenhuma porta."

Portuguese, document 4:

Before: "**Verificação:** Deve-se assegurar que o equipamento em questão se encontra operacional e que a conectividade de rede está funcional."
After: "Verifique primeiro, sem risco: a luz verde da câmera da entrada está acesa?"

## What scripts/style_check.py will flag

Outside code blocks: a long dash; "**" at the start of a list item; curly quotes in a Portuguese file; an emoji or a middle dot; a heading in Title Case; a word or phrase from the lists above; "non seulement" / "não só" / "não apenas"; a sentence over 35 words. Exit 1 with file, line and rule number; exit 0 otherwise. The checker flags; the agent rewrites. A flagged word that is the right word in context (a real "certificat de sécurité", a literal "pilier" in a building) stays, with a one-line note in verification.md.
