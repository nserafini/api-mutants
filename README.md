# api-mutants

API Rest for check Human DNA and detect Mutants

### Swagger Doc

- **URL:** http://ec2-54-174-45-231.compute-1.amazonaws.com/docs

### Endpoints: 
_________________________________________________

- **Path:** http://ec2-54-174-45-231.compute-1.amazonaws.com/mutant

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

- **Path:** http://ec2-54-174-45-231.compute-1.amazonaws.com/stats

- **Method:** GET

- **Responses:** 

  ```javascript
  {
    "count_mutant_dna": int,
    "count_human_dna": int,
    "ratio": int
  }
  ```
