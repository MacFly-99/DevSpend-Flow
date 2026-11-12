def test_create_transaction_success(client):
    # On simule l'envoi de données par un utilisateur
    payload = {
        "date": "2026-11-11",
        "description": "Test unitaire",
        "montant": 50.0,
        "categorie": "Test"
    }
    response = client.post("/api/v1/transactions/", json=payload)
    
    # On vérifie que le code de retour est 201 (Créé)
    assert response.status_code == 201
    # On vérifie que l'API nous renvoie bien un ID
    assert "id" in response.json()
    assert response.json()["description"] == "Test unitaire"

def test_create_transaction_invalid_amount(client):
    # On essaie d'envoyer un montant négatif (ce qui doit être bloqué)
    payload = {
        "date": "2026-11-11",
        "description": "Erreur volontaire",
        "montant": -10.0, # <-- ERREUR
        "categorie": "Test"
    }
    response = client.post("/api/v1/transactions/", json=payload)
    
    # Pydantic doit renvoyer une erreur 422 (Unprocessable Entity)
    assert response.status_code == 422

def test_get_non_existent_transaction(client):
    # On demande la transaction avec l'ID 999 (qui n'existe pas)
    response = client.get("/api/v1/transactions/999")
    
    # On doit avoir une erreur 404 (Not Found)
    assert response.status_code == 404
    assert "n'existe pas" in response.json()["detail"]