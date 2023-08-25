/*

import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ resolve, event }) => {

  // Apply CORS header for API routes
  if (event.url.pathname.startsWith("/api")) {
    // Required for CORS to work
    if(event.request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Headers": "*",
        }
      });
    }
  }

  const response = await resolve(event);
  if (event.url.pathname.startsWith("/api")) {
        response.headers.append("Access-Control-Allow-Origin", `*`);
  }
  return response;
};

*/

import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ resolve, event }) => {

  // Apply CORS header for API routes
  if (event.url.hostname === "ingredients-cdn.berrysauce.me") {
    // Required for CORS to work
    if(event.request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Headers": "*",
        }
      });
    }
  }

  const response = await resolve(event);
  if (event.url.hostname === "ingredients-cdn.berrysauce.me") {
        response.headers.append("Access-Control-Allow-Origin", `*`);
  }
  return response;
};