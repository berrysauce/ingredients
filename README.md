# 🧪 Ingredients

![GitHub repo size](https://img.shields.io/github/repo-size/berrysauce/ingredients)
[![CodeQL](https://github.com/berrysauce/ingredients/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/berrysauce/ingredients/actions/workflows/github-code-scanning/codeql)


> [!IMPORTANT]
> The domain for ingredients is being switched from "ingredients.tech" to "ingredients.work". I no longer own the old domain. 

Ingredients is a website scanner that is able to determine the "ingredients" (or technologies) behind a website.

It helps users discover the various software, frameworks, content management systems, analytics tools, and other technologies that are used to build and maintain a particular website.


<img alt="Ingredients Screenshot" src="https://public-cdn.berrysauce.me/shared/ingredients-screenshot.png">


<br>


## 📚 How it works

Ingredients consists of a frontend application (made with SvelteKit) and an API (made with FastAPI) with a simple script, that requests websites and checks their HTML tags and HTTP headers based on filters. The filters or "ingredients" are stored in their respective category-folders in the [ingredients/](https://github.com/berrysauce/ingredients/tree/main/ingredients) folder.

Each "ingredient" consists of a JSON file like the following:

```json
{
    "name": "Ingredient Name",
    "description": "Short description of the ingredient",
    "icon": "/icon/ingredient-name.png",
    "checks": {
        "tags": [
            {
                "tag": "script",
                "attribute": "src",
                "value": "cdn.example.com"
            },
            {
                "tag": "script",
                "attribute": null,
                "value": "cdn.example.com"
            }
        ],
        "headers": [
            {
                "header": "Server",
                "value": "example"
            },
            {
                "header": "Request-Id",
                "value": null
            }
        ]
    }
}
```

In the JSON file, you can define the HTML tags and HTTP headers the script should look for, to identify, if a website is using the ingredient.

As you can also see, this JSON file mentions a path to an icon, which is used to visualize the ingredient. Each favicon has a resolution of 32x32 pixels and is located inside the [icons/](https://github.com/berrysauce/ingredients/tree/main/icons) folder.

<br>


## 🤖 Using the API

Ingredients has an API you can use. This API can be used to scan sites.

> [!NOTE]  
> The API has a set of CORS origins in place as of now, so might only work locally! This might change later.

You can start a scan with one `GET` call. Just provide the URL you want to scan as a query parameter.

```http
GET  https://api.ingredients.work/ingredients?url=https://example.com
```

<br>


## ⚙️ How to add Ingredients

> [!NOTE]  
> Before you contribute, please take a look at the [CONTRIBUTING.md](https://github.com/berrysauce/ingredients/blob/main/CONTRIBUTING.md) file

To add an ingredient, create a JSON file in [ingredients/](https://github.com/berrysauce/ingredients/tree/main/ingredients) folder inside a fitting category-folder and add its icon (size 32x32 pixels, `.png` format) in the [icons/](https://github.com/berrysauce/ingredients/tree/main/icons) folder.

When defining an ingredient, follow this template:

```json
{
    "name": "Ingredient Name",
    "description": "Short description of the ingredient",
    "icon": "/icon/ingredient-name.png",
    "checks": {
        "tags": [
            (TAG CHECKS GO HERE)
        ],
        "headers": [
            (HEADER CHECKS GO HERE)
        ]
    }
}
```

<br>

### Tag checks

Tag checks are filters, which search for specific HTML tags on a website, to identify if it's using the ingredient. Here's an example:

```json
{
    "tag": "script",
    "attribute": "src",
    "value": "cdn.example.com"
}
```

Here, we're checking if the website has any `<script>` tags, which have `cdn.example.com` inside their `src` attribute.

And here, we're not defining an attribute (using `null`). This means, we're checking if the inside of the `<script>` tag has `cdn.example.com` inside:

```json
{
    "tag": "script",
    "attribute": null,
    "value": "cdn.example.com"
}
```

Like the following:

```html
<script>
    const url = "cdn.example.com"
</script>
```

Tag checks can also use wildcard values. For instance, if you need to check if a `<script>` tag's `src` attribute contains a domain and a file extension, you can do so with an asterisk (`*`). This will split your check into multiple segments. All segments must be inside the checked tag attribute somewhere. For example:

```json
{
    "tag": "script",
    "attribute": "src",
    "value": "example.com/library/*.js"
}
```

This will check if the `src` attribute of a `<script>` tag includes `example.com/library/` and `.js`.

<br>

### Header checks

Header checks are filters, which search for specific HTTP response headers when requesting the website, to identify if it's using the ingredient. Here's an example:

```json
{
    "header": "Server",
    "value": "example"
}
```

Here, we're checking if the HTTP response headers include a header called `Server` which has the value `example` inside.

And here, we're not defining a header value (using `null`). This means, we're checking if the `Request-Id` header exists at all, without explicitly checking for its value:

```json
{
    "header": "Request-Id",
    "value": null
}
```


<br>


## 📄 License

Ingredients — Website Technology Scanner

Copyright (C) 2023 Paul Haedrich (berrysauce)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
