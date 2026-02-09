<script lang="ts">
    let year = new Date().getFullYear();
    let api_hostname = "ingredients-api.berrysauce.dev";
    
    /*
    let hostname = "ingredients.berrysauce.dev";

    import { browser } from '$app/environment';
    if (browser) {
        if (typeof window !== "undefined") {
            hostname = window.location.hostname;
        }
    }
    */

    let categories: any = {};
    let ingredients: any = {};

    let scanURL: string = "";
    let loading: boolean = false;
    let requested: boolean = false;
    let error: null = null;

    async function handleSubmit() {
        loading = true;
        requested = false;
        error = null;

        try {
            let response = await fetch(`https://${api_hostname}/ingredients?url=${scanURL}&includeCategories=true`);
            let data = await response.json();

            if (!response.ok) {
                loading = false;
                requested = false;
                error = data.detail;
                console.log(error)
                return;
            }

            loading = false;
            requested = true;
            error = null;

            ingredients = data.matches;
            categories = data.categories;
            console.log(ingredients)
        } catch (error) {
            loading = false;
            requested = false;
            error = error;

            console.error("Error fetching data:", error);
            return;
        }
    }
</script>

<section class="py-4 py-xl-5">
    <div class="container" style="max-width: 600px;">
        <div class="text-center p-4 p-lg-5">
            <h1 class="display-4 text-start" style="font-family: Lora, serif;font-weight: 700;letter-spacing: -1px;margin-bottom: 16px;"><img class="img-fluid" src="/assets/img/icon.webp" style="height: 56px;margin-top: -10px;margin-right: 10px;" alt="Salat bowl">Ingredients</h1>
            <p class="text-start" style="color: rgb(135,135,135);">Ingredients is a website scanner that is able to determine the "ingredients" (or technologies) behind a website.</p>
            
            <form on:submit|preventDefault={handleSubmit} style="margin-bottom: 32px;margin-top: 48px;" method="get" enctype="application/x-www-form-urlencoded">
                <div class="input-group" style="margin-bottom: -16px;">
                    <input class="form-control" type="url" bind:value={scanURL} style="padding: 8px 16px;border-radius: 6px;background: rgba(255,255,255,0);border-top-right-radius: 0px;border-bottom-right-radius: 0px;font-weight: 500;outline: 0px !important;box-shadow: none !important;border: 2px solid #c5c5c5 ;border-right-style: none;" placeholder="https://example.com" name="url" required>
                    <button class="btn btn-primary float-end" type="submit" style="border-radius: 6px;background: rgba(255,255,255,0);font-weight: 600;border-top-left-radius: 0px;border-bottom-left-radius: 0px;margin-left: -2px;padding: 8px 16px;color: rgb(33,37,41);outline: 0px !important;box-shadow: none !important;border: 2px solid #c5c5c5 ;border-left-style: none;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-scan" style="font-size: 18px;margin-bottom: 3px;margin-right: 5px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M4 7v-1a2 2 0 0 1 2 -2h2"></path>
                            <path d="M4 17v1a2 2 0 0 0 2 2h2"></path>
                            <path d="M16 4h2a2 2 0 0 1 2 2v1"></path>
                            <path d="M16 20h2a2 2 0 0 0 2 -2v-1"></path>
                            <path d="M5 12l14 0"></path>
                        </svg>
                        Scan
                    </button>
                </div>
            </form>

            <ul class="list-inline text-start" style="font-size: 14px;margin-bottom: 32px;">
                <li class="list-inline-item" style="margin-right: 12px;">
                    <a href="https://github.com/sponsors/berrysauce" style="color: inherit;text-decoration: underline;text-decoration-color: #c5c5c5;" target="_blank">
                        Donate
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-arrow-up-right" style="margin-top: -2px;margin-left: 2px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M17 7l-10 10"></path>
                            <path d="M8 7l9 0l0 9"></path>
                        </svg>
                    </a>
                </li>
                <li class="list-inline-item" style="margin-right: 12px;">
                    <a href="https://github.com/berrysauce/ingredients" style="color: inherit;text-decoration: underline;text-decoration-color: #c5c5c5;">
                        GitHub
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-arrow-up-right" style="margin-top: -2px;margin-left: 2px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M17 7l-10 10"></path>
                            <path d="M8 7l9 0l0 9"></path>
                        </svg>
                    </a>
                </li>
                <li class="list-inline-item">
                    <a href="https://api.ingredients.work/" style="color: inherit;text-decoration: underline;text-decoration-color: #c5c5c5;">
                        API
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-arrow-up-right" style="margin-top: -2px;margin-left: 2px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M17 7l-10 10"></path>
                            <path d="M8 7l9 0l0 9"></path>
                        </svg>
                    </a>
                </li>
            </ul>

            {#if loading}
                <div id="loading" style="margin-top:64px;margin-bottom: 64px;">
                    <p class="text-center" style="font-weight: 500;"><span class="spinner-border spinner-border-sm" role="status" style="margin-right: 10px;width: 20px;height: 20px;margin-bottom: -3px;color: rgb(33,37,41);font-size: 12px;"></span>Checking ingredients</p>
                </div>
            {/if}

            {#if requested && !loading && Object.keys(ingredients).length == 0}
                <div style="margin-top:64px;margin-bottom: 64px;">
                    <p class="text-center" style="font-weight: 500;">
                        <svg class="icon icon-tabler icon-tabler-alert-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="color: rgb(214,70,9);font-size: 22px;margin-right: 10px;margin-bottom: 3px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"></path>
                            <path d="M12 8v4"></path>
                            <path d="M12 16h.01"></path>
                        </svg>
                        No ingredients found
                    </p>
                </div>
            {/if}

            {#if error != null}
                <div style="margin-top:64px;margin-bottom: 64px;">
                    <p class="text-center" style="font-weight: 500;margin-bottom: 5px;"><svg class="icon icon-tabler icon-tabler-alert-triangle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="color: rgb(204,45,35);font-size: 22px;margin-right: 10px;margin-bottom: 3px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M12 9v2m0 4v.01"></path>
                            <path d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75"></path>
                        </svg>An error occurred while analyzing</p>
                    <p class="text-center" style="font-weight: 500;"><code style="color: rgb(204,45,35);padding: 5px 10px;background: rgba(204,45,35,0.1);border-radius: 5px;">{ error }</code></p>
                </div>
            {/if}

            {#if !loading && error == null && Object.keys(ingredients).length != 0}
                <div class="text-start" style="margin-top: 64px;margin-bottom: 64px;">
                    <div class="row row-cols-2">
                        {#each Object.keys(categories) as category (category)}
                            {#if ingredients[category]}
                                <div class="col-12 col-sm-6">
                                    <div style="border-width: 2px;border-top-style: solid;border-top-color: rgb(33,37,41);margin-bottom: 50px;">
                                        <h2 class="fs-5" style="font-weight: bold;margin-top: 6px;margin-bottom: 16px;font-family: Lora, serif;">{ categories[category] }</h2>
                                        <ul class="list-unstyled">
                                            {#each ingredients[category] as ingredient}
                                                <li style="margin-bottom: 4px;font-weight: 500;"><img class="img-fluid" alt={ ingredient.name } src="https://cdn.ingredients.work{ ingredient.icon }" width="24" height="24" style="height: 24px;padding: 3px;border-radius: 4px;margin-right: 8px;margin-bottom: 3px;border: 1px solid rgb(206,207,208) ;">
                                                    { ingredient.name }
                                                </li>
                                            {/each}
                                        </ul>
                                    </div>
                                </div>
                            {/if}
                        {/each}
                    </div>
                </div>
            {/if}

            <footer class="text-start" style="margin-top: 70px;padding-top: 24px;border-top: 2px solid rgb(197,197,197) ;">
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;font-weight: 500;">
                    Copyright © 2023-{ year } 
                    <a href="https://berrysauce.me" target="_blank" style="color: inherit;">
                        berrysauce
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-arrow-up-right" style="margin-top: -2px;margin-left: 1px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M17 7l-10 10"></path>
                            <path d="M8 7l9 0l0 9"></path>
                        </svg>
                    </a>
                </p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;">Usage of Ingredients is permitted under it's <a href="https://github.com/berrysauce/ingredients/blob/main/FAIR_USE_POLICY.md" style="color: inherit;">Fair-use-Policy</a>. Traffic which does not comply with this policy or the <a href="https://berrysauce.me/terms" style="color: inherit;">Terms of Service</a>&nbsp;will be blocked. <a href="https://github.com/berrysauce/ingredients/blob/main/LICENSE.md" style="color: inherit;">View the license for this service here</a>.</p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;">No personal data is collected when using Ingredients (this website or its services).</p>
            </footer>
        </div>
    </div>
</section>
