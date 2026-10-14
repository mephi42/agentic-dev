# Structuring commits

- Split changes into atomic commits that each build and pass tests.

# Writing commit messages and comments

- Write for expert maintainers.
- Default to no comment.
- Omit trivial architecture facts.
- Don't explain obvious C/compiler behavior.
- Cut sentences the reader can infer from a referenced function or from
  the code itself.
- Don't add comments that merely narrate obvious code.
- Don't add Co-Authored-By to commit messages.
- Don't put "X used to do Y" implementation history in comments.
- Don't put test-verification notes in commit messages.
- Don't use mannered prose.
- Keep comments to one line: what and why, not how.
- Justify a change by naming what needs it, not what the old code lacked.
- State the fact a reviewer needs to verify the change; skip obvious symptoms.
- Back facts about external formats and APIs with a link to the spec.
- Pin links to a fixed revision and anchor them to the relevant line.
- When removing code that states a rationale, say why it no longer holds.
- Don't enumerate what's in the diff; name the category instead.
