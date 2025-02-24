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
![CS361 _ Microservice A UML Sequence Diagram](https://github.com/user-attachments/assets/0b8f0d80-23c9-482d-9055-6b892465fb69)
