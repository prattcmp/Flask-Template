**Get Post**
----
  Returns a post based on input.

* **URL**

  /get_post

* **Method:**

  `GET`
  
*  **Parameters**

   **Required:**
   `post_id=[integer:unique]` (the ID of the post being requested) <br />
   `user_secret_key=[string:128]` (alphanumeric; specific to the user)
   
   **Optional:**
   `type=[string]` (can be either "post" or "comment") <br />

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
    ```json
    { 
        "post_id": [integer:primary_key], 
    	"content": "[string:280(max)]",
    	"created_at": "[timestamp]"
	}
	```
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

  OR

  * **Code:** 404 NOT FOUND  <br />
    **Content:** `{ error : "That post doesn't exist." }` (or similar message)
    
* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/get_post",
      dataType: "json",
      type : "POST",
      data: { "post_id": 20,
      		  "user_secret_key": "abc123...128" }
    });
  ```
  
* **Notes:**

  * None