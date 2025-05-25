## Projekt: Neuronowy model predykcyjny jako usługa FastAPI

**Problem:** Generowanie tekstu na podstawie promptu przy użyciu modelu LLaMA.

**Model:** Mistral 7B Instruct (GGUF Q4_0)

**Proces:**  
Model uruchomiony lokalnie z wykorzystaniem `llama-cpp-python` jako backend.  
Zastosowano FastAPI do obsługi żądań REST.

**Uczenie:** Model pretrenowany (TheBloke/Mistral), brak dodatkowego treningu.

**Jakość:**  
Brak fine-tuningu — jakość zależna od oryginalnych wag.

**API:**  
POST `/generate` — generuje tekst  
GET `/health` — status
