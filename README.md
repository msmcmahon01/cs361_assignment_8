# Item Modifier API spec

Routes:
  - Add Adjective to Item
    - itemName (string): The name of the item without an adjective.

  - Returns
    - modifiedName (string): The modified name of the item with a randomly added adjective.

### Example Input
```json
{
    "itemName": "Potion"
}
```

### Example Output
```json
{
    "modifiedName": "Super Potion"
}
```

### UML Sequence Diagram
"https://github.com/msmcmahon01/cs361_assignment_8/blob/main/CS361%20_%20Microservice%20A%20UML%20Sequence%20Diagram.png"
