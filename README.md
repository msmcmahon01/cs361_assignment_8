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
![CS361 _ Microservice A UML Sequence Diagram](https://github.com/user-attachments/assets/e619275d-b289-421c-8daa-80ffbad1fe6f)
