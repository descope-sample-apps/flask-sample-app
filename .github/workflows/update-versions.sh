#!/bin/bash

# Fetch the latest version numbers
WEB_COMPONENT_VERSION=$(npm view @descope/web-component version)
WEB_JS_SDK_VERSION=$(npm view @descope/web-js-sdk version)

echo "Latest @descope/web-component version: $WEB_COMPONENT_VERSION"
echo "Latest @descope/web-js-sdk version: $WEB_JS_SDK_VERSION"

# Update HTML and JavaScript files
find . -type f \( -iname \*.html -o -iname \*.js \) -exec sed -i "s/@descope\/web-component@[0-9]*\.[0-9]*\.[0-9]*/@descope\/web-component@$WEB_COMPONENT_VERSION/g" {} +
find . -type f \( -iname \*.html -o -iname \*.js \) -exec sed -i "s/@descope\/web-js-sdk@[0-9]*\.[0-9]*\.[0-9]*/@descope\/web-js-sdk@$WEB_JS_SDK_VERSION/g" {} +
