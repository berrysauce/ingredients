<script>
    let loading = false;

    let categories = {
        "ads": "Ads",
        "analytics": "Analytics",
        "auth": "Authentication",
        "builders": "Website Builders",
        "cdn": "Content Delivery Networks",
        "cms": "Content Management Systems",
        "compliance": "Compliance",
        "docs": "Documentation Tools",
        "fonts": "Fonts",
        "frameworks": "Frameworks",
        "hosts": "Hosts",
        "libraries": "Libraries",
        "monitoring": "Monitoring",
        "notifications": "Notifications",
        "payments": "Payments",
        "search": "Search",
        "security": "Security",
        "servers": "Servers",
        "storage": "Storage",
        "widgets": "Widgets",
        "other": "Other"
    }

    let scanURL = "";
    let ingredients = [];

    async function handleSubmit() {
        loading = true;
        try {
            let response = await fetch(`https://ingredients.berrysauce.me/api/ingredients?url=${scanURL}`);
            let data = await response.json();
            loading = false;
            ingredients = data.matches;
            console.log(ingredients)
        } catch (error) {
            loading = false;
            console.error("Error fetching data:", error);
        }
    }
</script>

<section class="py-4 py-xl-5">
    <div class="container" style="max-width: 600px;">
        <div class="p-4 p-lg-5">
            <div style="margin-bottom: 64px;">
                <h1 class="display-4" style="font-family: 'Inter Tight', sans-serif;font-weight: bold;margin-bottom: 8px;"> 🧪 Ingredients</h1>
                <p style="color: rgba(33,37,41,0.5);">Ingredients is an open source tool, which can find out which technologies a website uses. Ingredients can be used right here, or in form of an API.</p>
            </div>

            <style>
                #form {
                    display: block;
                }

                #error {
                    display: none;
                }
            </style>

            <div id="error">
                <p class="text-center" style="font-weight: 500;">
                    <svg class="icon icon-tabler icon-tabler-alert-triangle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="color: rgb(49,169,0);font-size: 26px;margin-right: 10px;margin-bottom: 2px;" name="url">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                        <path d="M12 9v2m0 4v.01"></path>
                        <path d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75"></path>
                    </svg>
                    An error occurred while analyzing
                </p>
            </div>

            <div id="form">
                <form on:submit|preventDefault={handleSubmit} style="margin-bottom: 32px;" method="get" enctype="application/x-www-form-urlencoded">
                    <div class="input-group" style="margin-bottom: -16px;">
                        <input class="form-control" type="url" name="url" style="padding: 8px 16px;border-radius: 10px;background: rgba(255,255,255,0);border-top-right-radius: 0px;border-bottom-right-radius: 0px;font-weight: 500;border: 2px solid #212529 ;" placeholder="https://example.com" bind:value={scanURL} required >
                        <button class="btn btn-primary float-end" type="submit" style="border-radius: 10px;background: #212529;font-weight: 500;color: #ffffff;border-top-left-radius: 0px;border-bottom-left-radius: 0px;margin-left: -2px;padding: 8px 16px;border: 2px solid #212529;">
                            <svg class="icon icon-tabler icon-tabler-scan" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="font-size: 18px;margin-bottom: 3px;margin-right: 5px;">
                                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                <path d="M4 7v-1a2 2 0 0 1 2 -2h2"></path>
                                <path d="M4 17v1a2 2 0 0 0 2 2h2"></path>
                                <path d="M16 4h2a2 2 0 0 1 2 2v1"></path>
                                <path d="M16 20h2a2 2 0 0 0 2 -2v-1"></path>
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                            </svg>
                            Scan
                        </button>
                    </div>
                </form>
                <p class="text-center" style="color: rgba(33,37,41,0.5);margin-bottom: 64px;font-size: 14px;">
                    <a href="https://github.com/berrysauce/ingredients" target="_blank" style="font-weight: 500;color: inherit;margin-right: 16px;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-star" style="margin-bottom: 2px;margin-right: 2px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M12 17.75l-6.172 3.245l1.179 -6.873l-5 -4.867l6.9 -1l3.086 -6.253l3.086 6.253l6.9 1l-5 4.867l1.179 6.873z"></path>
                        </svg>
                        Star on GitHub
                    </a>
                    <a href="/api" style="font-weight: 500;color: inherit;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-arrow-right" style="margin-bottom: 2px;margin-right: 2px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <line x1="13" y1="18" x2="19" y2="12"></line>
                            <line x1="13" y1="6" x2="19" y2="12"></line>
                        </svg>
                        Ingredients also has an API
                    </a>
                </p>
            </div>

            {#if loading}
                <div id="loading">
                    <p class="text-center" style="font-weight: 500;"><span class="spinner-border spinner-border-sm" role="status" style="margin-right: 10px;width: 22px;height: 22px;margin-bottom: -3px;color: rgb(49,169,0);"></span>Checking ingredients</p>
                </div>
            {/if}

            {#if !loading}
                {#each Object.keys(ingredients) as category (category)}
                    <div style="border-width: 2px;border-top-style: solid;border-top-color: rgb(33,37,41);margin-bottom: 50px;">
                        <h1 class="fs-5" style="font-weight: bold;margin-top: 6px;margin-bottom: 16px;">{ categories[category] }</h1>
                        <ul class="list-unstyled">
                            {#each ingredients[category] as ingredient}
                                <li style="margin-bottom: 4px;font-weight: 500;"><img class="img-fluid" src="https://ingredients.berrysauce.me/api{ ingredient.icon }" width="24" height="24" style="height: 24px;padding: 3px;border-radius: 4px;margin-right: 8px;margin-bottom: 3px;border: 1px solid rgb(206,207,208) ;">{ ingredient.name }</li>
                            {/each}
                        </ul>
                    </div>
                {/each}
            {/if}

            <footer>
                <hr style="margin-top: 64px;margin-bottom: 16px;">
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;font-weight: 500;">Copyright © 2023 berrysauce</p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;">Usage of&nbsp;Ingredients is permitted under it's&nbsp;<a href="#" style="color: inherit;">Fair-use-Policy</a>. Traffic which does not comply with this policy or the <a href="#" style="color: inherit;">Terms of Service</a>&nbsp;will be blocked.&nbsp;<a href="https://github.com/berrysauce/ingredients/blob/main/LICENSE.md" style="color:inherit;">View the license for this service here</a>.</p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;"></p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;">No personal data is collected when using Ingredients (this website or its services).</p>
            </footer>
        </div>
    </div>
</section>