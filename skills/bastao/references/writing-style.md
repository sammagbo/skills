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
17. Rhythm: a short sentence after a long one, one idea per line in lists. The limits per sentence and per paragraph are rules 21 and 22.
18. Specifics over adjectives: names, dates, numbers, screens, buttons. "Le voyant vert de la caméra de l'entrée", not "l'équipement concerné". "A luz verde da câmera da entrada", not "o equipamento em questão".
19. Dates as DD/MM/YYYY. Times with the zone when server time and local time differ.
20. The last pass, in your head, as the person who will receive the document: "what here sounds like a machine wrote it?" Fix those lines. Then: "would this person know what to do at 8 a.m. with people waiting at the gate?" If not, the document is not finished.

## Rules adapted from ASD-STE100

ASD-STE100, Simplified Technical English, is a standard of ASD, the Aerospace, Security and Defence Industries Association of Europe. It was written for aircraft maintenance manuals: procedures read under pressure by a person who must do the right thing the first time. Document 4 is read the same way. The current issue is Issue 9 (January 2025). It has two parts: 53 writing rules in nine sections, and a dictionary of about 900 approved words, whose meanings and spelling are American English. The standard is free of charge, but ASD keeps the copyright: its text may not be reproduced or adapted without permission. So the skill does not translate it. It writes its own rules for French and Portuguese below, from the ideas of some rules of the standard, and builds its own approved words. Rules 21 to 27 follow rules of the standard; rules 28 to 30 are the skill's own. The skill claims no conformance to ASD-STE100, and it is not approved by ASD or affiliated with it.

21. Sentence length: 20 words at most in documents 3 and 4, which are procedures; 25 at most in the other documents. A procedure written in another document (the steps of a password change in document 5) keeps to 20 too; the checker does not see that case, you do. The checker counts the words a reader reads: no inline code; a `{{field}}`, a URL or an e-mail address counts as one word. A sentence wrapped over several lines is read whole.
22. One topic per paragraph, three sentences at most: these documents are read in a hurry, and the six sentences of ASD-STE100 are an upper bound. A list item and a table cell are paragraphs too. In documents 3 and 4, one that holds a short procedure (the fixed rows of document 3) may have six sentences, never more. The first sentence says what the paragraph is about.
23. One instruction per sentence. Two actions are two sentences, unless they happen at the same time. An instruction may carry its condition ("Si le voyant est éteint, appuyez sur le bouton." / "Se a luz estiver apagada, aperte o botão."), nothing else.
24. Procedures in the imperative, active voice, present tense: "Vérifiez" / "Verifique". Document 3 keeps the infinitive of a checklist ("Vérifier" / "Verificar"). Descriptive text in the active voice and the present; the past only for an incident that happened, with its date.
25. Articles always written: "la machine", "a máquina", never a telegraphic "machine redémarrée" / "máquina reiniciada". No chain of more than three nouns; split it with a verb ("le script de sauvegarde de la base de la bibliothèque" becomes "le script qui sauvegarde la base de la bibliothèque"). ASD-STE100 sets the same limit, three words, for an English noun group.
26. One word for one meaning, one meaning for one word, from the approved words below. A product name is written the way the inventory found it, every time.
27. A warning starts with the command, or with its condition and then the command, and then says what can happen: "N'éteignez pas l'onduleur. La machine s'arrêterait sans enregistrer les informations." / "Não desligue o nobreak. A máquina pararia sem gravar as informações." ASD-STE100 sets how a warning starts and that it explains the risk. Where it goes is this skill's rule: before the step it protects, as the first sentence of the list item or an item of its own, never inside the step's sentence, never after the step.
28. No "etc.", no "e assim por diante", no "entre autres". List everything, or say how many there are.
29. Say what to do before what not to do. A negative instruction stands alone only when no positive one exists.
30. A pronoun ("il", "cela", "ele", "isso") only when its referent is the subject of the previous sentence. Otherwise repeat the noun.

## Approved words

One word per thing, in every document of a pack. A technical thing takes, the first time, the plain expression of `references/plain-language.md`; after that, the word below. The last column lists the words not to use for that thing; the same word can be right for another thing ("une application installée sur les postes" is the program people install on their computers, not the program on the machine). When you choose a word for a thing that is in no list, write it under "Words chosen" in `verification.md` and use it everywhere.

| Thing | Français | Português | Not, for this thing |
|---|---|---|---|
| the person who keeps the system after the handover | le propriétaire | o dono | as a name for the owner: le responsable, le gestionnaire, le référent; o responsável, o gestor, o proprietário |
| the person called for technical matters | le référent technique | a referência técnica | l'informaticien, le technicien, le prestataire; o técnico, o TI, o suporte |
| the person who hands over | le développeur d'origine, then « le développeur » or the name | o desenvolvedor de origem, then "o desenvolvedor" or the name | le prestataire, le fournisseur, l'auteur; o prestador, o fornecedor, o autor |
| the system | its name, the one in document 1 | its name, the one in document 1 | la solution, l'outil, la plateforme; a solução, a ferramenta, a plataforma |
| the machine where the program runs | la machine; « le serveur » only in documents 2, 3 and 5, after its explanation | a máquina; "o servidor" only in documents 2, 3 and 5, after its explanation | l'instance, la VM, l'hôte; a instância, a VM, o host |
| the program on that machine | le programme | o programa | l'application, le logiciel, le backend; a aplicação, o aplicativo, o software, o backend |
| what people see and use | l'écran | a tela | l'interface, le portail, le front; a interface, o portal, o front |
| a copy of the data | la sauvegarde; in documents 1, 4 and 6, the plain expression or the verb ("sauvegardées") | o backup; in documents 1, 4 and 6, the plain expression or the verb ("copiadas") | le backup, l'archive, la copie de sécurité; a cópia de segurança, o arquivo de backup |
| to install a new version | installer la nouvelle version | instalar a nova versão | déployer, mettre en production; fazer o deploy, subir |
| to start the program again | redémarrer | reiniciar | relancer, rebooter; dar um restart, resetar |
| to check | vérifier | verificar | contrôler, s'assurer que; checar, conferir, assegurar |
| the place where secrets are kept | its name ({{vault}}), every time | its name ({{vault}}), every time | le vault, « le coffre » alone when the place has a name; o vault, "o cofre" alone when the place has a name |

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

Outside code blocks and comments: a long dash; "**" at the start of a list item; curly quotes in a Portuguese file; an emoji or a middle dot; a heading in Title Case; a word or phrase from the lists above; "non seulement" / "não só" / "não apenas"; a sentence over the limit of rule 21 (20 words in documents 3 and 4, 25 in the others); a paragraph, a list item or a table cell of more than three sentences, or more than six for a list item or a table cell of documents 3 and 4 (rule 22). It reads a sentence across the lines of its paragraph or list item; it ends no sentence after "M.", "Sr.", "Dr.", "n." or "p.", nor before a lowercase word or a closing quote (« Erreur ! » quand...). `--max-words N` and `--max-sentences N` replace the limits of rules 21 and 22, for a pack written before them. Exit 1 with file, line and rule number; exit 0 otherwise. Rules 23 to 30, and rule 21 for a procedure outside documents 3 and 4, are read by the agent, not by the checker. The checker flags; the agent rewrites. A flagged word that is the right word in context (a real "certificat de sécurité", a literal "pilier" in a building) stays, with a one-line note in verification.md.
