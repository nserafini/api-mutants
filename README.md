# api-mutants

API Rest for check Human DNA and detect Mutants

### Swagger Doc

- **URL:** http://mutant-db-664268063.us-east-1.elb.amazonaws.com/docs

### Endpoints: 
_________________________________________________

- **Path:** http://mutant-db-664268063.us-east-1.elb.amazonaws.com/mutant

- **Method:** POST

- **Params:** JSON with DNA sequences:

  ```javascript
  {"dna": [str, str, str, str, ...]}
  ```
  Example:

  ```javascript
  {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}
  ```
 
 - **Responses:** 
  
    - 200: Is mutant DNA
    - 403: No Mutant DNA
    - 400: Invalid request

_________________________________________________

- **Path:** http://mutant-db-664268063.us-east-1.elb.amazonaws.com/stats

- **Method:** GET

- **Responses:** 

  ```javascript
  {
    "count_mutant_dna": int,
    "count_human_dna": int,
    "ratio": int
  }
  ```
