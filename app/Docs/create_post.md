**Create Post**
----
  Validates and stores a new post. Returns metadata for the post.

* **URL**

  /create_post

* **Method:**

  `POST`
  
*  **Parameters**

   **Required:**
   `content=[string:280(max)]` (text of the post; no longer than 280 characters)
   `user_id=[integer:unique]` (ID of the user creating the post)
   `user_secret_key=[string:128]` (alphanumeric; specific to the user)

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
    **Content:** `{ "error" : "You are unauthorized to make this request." }` (if user_secret_key doesn't match user_id)

  OR

  * **Code:** 422 UNPROCESSABLE ENTRY  <br />
    **Content:** `{ "error" : "Your content cannot be more than 280 characters." }` (or similar message)
    
* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/create_post",
      dataType: "json",
      type : "POST",
      data: { "content": "This is a test post.",
              "user_secret_key": "apC03...",
              "user_id": 1 }
    });
  ```
  
* **Notes:**

  * `content` should be encoded as `utf8mb4` to support emojis.
  
  * The `user_id` is the ID of the user creating the post. It should match the `user_secret_key` associated with the user (authentication).
