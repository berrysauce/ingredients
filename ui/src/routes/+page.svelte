<script lang="ts">
    let year = new Date().getFullYear();

    let categories = {};
    let ingredients = {};

    let scanURL: string = "";
    let loading: boolean = false;
    let requested: boolean = false;
    let error: null = null;

    async function handleSubmit() {
        loading = true;
        requested = false;
        error = null;

        try {
            let response = await fetch(`https://ingredients.tech/api/ingredients?url=${scanURL}&includeCategories=true`);
            // let response = await fetch(`https://dev.ingredients.tech/api/ingredients?url=${scanURL}&includeCategories=true`);
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
        <div class="p-4 p-lg-5">
            <div style="margin-bottom: 64px;">
                <h1 class="display-4" style="font-family: 'Inter Tight', sans-serif;font-weight: bold;margin-bottom: 8px;"> 🧪 Ingredients</h1>
                <p style="color: rgba(33,37,41,0.5);">Ingredients is a website scanner that is able to determine the "ingredients" (or technologies) behind a website. Ingredients can be used right here, or in form of an API.</p>
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
                    <a href="/api" target="_blank" style="font-weight: 500;color: inherit;">
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
                    <p class="text-center" style="font-weight: 500;margin-bottom: 50px;"><span class="spinner-border spinner-border-sm" role="status" style="margin-right: 10px;width: 22px;height: 22px;margin-bottom: -3px;color: rgb(49,169,0);"></span>Checking ingredients</p>
                </div>
            {/if}

            {#if requested && !loading && Object.keys(ingredients).length == 0}
                <p class="text-center" style="font-weight: 500;">
                    <svg class="icon icon-tabler icon-tabler-alert-octagon" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="color: rgb(242,113,58);font-size: 22px;margin-right: 10px;margin-bottom: 3px;">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                        <path d="M8.7 3h6.6c0.3 0 .5 .1 .7 .3l4.7 4.7c0.2 .2 .3 .4 .3 .7v6.6c0 .3 -.1 .5 -.3 .7l-4.7 4.7c-0.2 .2 -.4 .3 -.7 .3h-6.6c-0.3 0 -.5 -.1 -.7 -.3l-4.7 -4.7c-0.2 -.2 -.3 -.4 -.3 -.7v-6.6c0 -.3 .1 -.5 .3 -.7l4.7 -4.7c0.2 -.2 .4 -.3 .7 -.3z"></path>
                        <line x1="12" y1="8" x2="12" y2="12"></line>
                        <line x1="12" y1="16" x2="12.01" y2="16"></line>
                    </svg>
                    No ingredients found
                </p>
            {/if}

            {#if error != null}
                <div>
                    <p class="text-center" style="font-weight: 500;margin-bottom: 5px;"><svg class="icon icon-tabler icon-tabler-alert-triangle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="color: rgb(204,45,35);font-size: 22px;margin-right: 10px;margin-bottom: 3px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <path d="M12 9v2m0 4v.01"></path>
                            <path d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75"></path>
                        </svg>An error occurred while analyzing</p>
                    <p class="text-center" style="font-weight: 500;"><code style="color: rgb(204,45,35);padding: 5px 10px;background: rgba(204,45,35,0.1);border-radius: 5px;">{ error }</code></p>
                </div>
            {/if}

            {#if !loading && error == null}
                <div class="row row-cols-2">
                    {#each Object.keys(categories) as category (category)}
                        {#if ingredients[category]}
                            <div class="col">
                                <div style="border-width: 2px;border-top-style: solid;border-top-color: rgb(33,37,41);margin-bottom: 50px;">
                                    <h1 class="fs-5" style="font-weight: bold;margin-top: 6px;margin-bottom: 16px;">{ categories[category] }</h1>
                                    
                                    <ul class="list-unstyled">
                                        {#each ingredients[category] as ingredient}
                                            <!-- List item -->
                                            <li onclick="openDetailModal('{ ingredient.id }-modal')" style="margin-bottom: 4px;font-weight: 500;"><img class="img-fluid" alt={ ingredient.name } src="https://cdn-api.ingredients.tech{ ingredient.icon }" width="24" height="24" style="height: 24px;padding: 3px;border-radius: 4px;margin-right: 8px;margin-bottom: 3px;border: 1px solid rgb(206,207,208) ;">{ ingredient.name }</li>
                                        
                                            <!-- Detail modal -->
                                            <div id="{ ingredient.id }-modal" class="modal fade" role="dialog" tabindex="-1">
                                                <div class="modal-dialog" role="document">
                                                    <div class="modal-content">
                                                        <div class="modal-body" style="padding: 32px 42px;border-style: none;">
                                                            <h1 class="fs-5" style="font-weight: 600;margin-top: 6px;letter-spacing: -0.5px;color: rgb(33, 37, 41);margin-bottom: 10px;">
                                                                <img class="img-fluid" alt={ ingredient.name } src="https://cdn-api.ingredients.tech{ ingredient.icon }" width="24" height="24" style="height: 26px;padding: 4px;border-radius: 4px;margin-right: 10px;margin-bottom: 4px;border: 1px solid rgb(206,207,208);width: 26px;" />
                                                                { ingredient.name }
                                                                <button class="btn-close float-end" type="button" data-bs-dismiss="modal" aria-label="Close" style="font-size: 12px;margin-top: 6px;"></button>
                                                            </h1>
                                                            <p style="color: rgba(33,37,41,0.5);margin-bottom: 32px;">
                                                                { ingredient.description }
                                                            </p>
                                                            <div class="progress" style="height: 6px;border-radius: 50px;background: rgb(238,238,238);margin-bottom: 10px;">
                                                                <div class="progress-bar" aria-valuenow="{ ingredient.match_percentage }" aria-valuemin="0" aria-valuemax="100" style="width: { ingredient.match_percentage }%;background-color: rgb(49, 169, 0);"><span class="visually-hidden">{ ingredient.match_percentage }%</span></div>
                                                            </div>
                                                            <p style="color: rgba(33,37,41,0.5);margin-bottom: 16px;"><span style="color: rgb(49,169,0);font-weight: 500;">{ ingredient.match_percentage }%</span> of scans use <span style="color: rgb(49,169,0);font-weight: 500;">{ ingredient.name }</span>.</p>
                                                            <p style="color: rgba(33,37,41,0.5);margin-top: 32px;font-size: 12px;margin-bottom: 0px;padding-top: 6px;border-top: 1px solid rgba(33,37,41,0.2);"><span style="color: rgba(33, 37, 41, 0.3);">This data is based on the amount of scans that have been made since the ingredient has been added.</span></p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        {/each}
                                    </ul>

                                    <script>
                                        function openDetailModal(id) {
                                            var detailModal = new bootstrap.Modal(document.getElementById(id), {
                                              keyboard: false
                                            })
                                            
                                            detailModal.toggle()
                                        }
                                    </script>

                                </div>
                            </div>
                        {/if}
                    {/each}
                </div>

                <!-- A little tip -->
                <div style="margin-bottom: 32px;padding: 16px 22px;border: 1px solid rgb(206,207,208);border-radius: 10px;background: #fbfbfb;margin-top: 32px;">
                    <h1 class="fs-6" style="font-weight: 600;margin-top: 6px;margin-bottom: 2px;"><svg class="icon icon-tabler icon-tabler-info-circle" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="font-size: 18px;margin-bottom: 4px;margin-right: 8px;">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <circle cx="12" cy="12" r="9"></circle>
                            <line x1="12" y1="8" x2="12.01" y2="8"></line>
                            <polyline points="11 12 12 12 12 16 13 16"></polyline>
                        </svg>A little tip</h1>
                    <p style="color: rgba(33,37,41,0.5);font-size: 14px;margin-bottom: 0px;">Click on ingredients to reveal scan statistics and more details about them.</p>
                </div>
            {/if}

            <footer>
                <hr style="margin-top: 64px;margin-bottom: 16px;">
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;font-weight: 500;">Copyright © { year } berrysauce</p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;">Usage of&nbsp;Ingredients is permitted under it's&nbsp;<a href="https://github.com/berrysauce/ingredients/blob/main/FAIR_USE_POLICY.md" style="color: inherit;">Fair-use-Policy</a>. Traffic which does not comply with this policy or the <a href="https://berrysauce.me/terms" style="color: inherit;">Terms of Service</a>&nbsp;will be blocked.&nbsp;<a href="https://github.com/berrysauce/ingredients/blob/main/LICENSE.md" style="color:inherit;">View the license for this service here</a>.</p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;"></p>
                <p style="color: rgba(33,37,41,0.5);font-size: 12px;">No personal data is collected when using Ingredients (this website or its services).</p>
            </footer>
        </div>
    </div>
</section>
