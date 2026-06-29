Title: Understanding the life cycle of orders — pretix 2026.6.0.dev0 documentation

URL Source: https://docs.pretix.eu/dev/api/guides/order_lifecycle.html

Markdown Content:
[![Image 3: Logo](https://docs.pretix.eu/dev/_static/logo-white.svg) Developer Documentation](https://docs.pretix.eu/dev/index.html)

*   [REST API](https://docs.pretix.eu/dev/api/index.html)
    *   [Basic concepts](https://docs.pretix.eu/dev/api/fundamentals.html)
        *   [Authentication](https://docs.pretix.eu/dev/api/fundamentals.html#authentication)
        *   [Permissions](https://docs.pretix.eu/dev/api/fundamentals.html#permissions)
        *   [Compatibility](https://docs.pretix.eu/dev/api/fundamentals.html#compatibility)
        *   [Pagination](https://docs.pretix.eu/dev/api/fundamentals.html#pagination)
        *   [Conditional fetching](https://docs.pretix.eu/dev/api/fundamentals.html#conditional-fetching)
            *   [Object-level conditional fetching](https://docs.pretix.eu/dev/api/fundamentals.html#object-level-conditional-fetching)
            *   [List-level conditional fetching](https://docs.pretix.eu/dev/api/fundamentals.html#list-level-conditional-fetching)

        *   [Errors](https://docs.pretix.eu/dev/api/fundamentals.html#errors)
        *   [Data types](https://docs.pretix.eu/dev/api/fundamentals.html#data-types)
            *   [Query parameters](https://docs.pretix.eu/dev/api/fundamentals.html#query-parameters)

        *   [Idempotency](https://docs.pretix.eu/dev/api/fundamentals.html#idempotency)
        *   [File upload](https://docs.pretix.eu/dev/api/fundamentals.html#file-upload)

    *   [Authentication](https://docs.pretix.eu/dev/api/auth.html)
        *   [Token-based authentication](https://docs.pretix.eu/dev/api/tokenauth.html)
            *   [Obtaining an API token](https://docs.pretix.eu/dev/api/tokenauth.html#obtaining-an-api-token)
            *   [Using an API token](https://docs.pretix.eu/dev/api/tokenauth.html#using-an-api-token)

        *   [OAuth authentication / “Connect with pretix”](https://docs.pretix.eu/dev/api/oauth.html)
            *   [Registering an application](https://docs.pretix.eu/dev/api/oauth.html#registering-an-application)
            *   [Obtaining an authorization grant](https://docs.pretix.eu/dev/api/oauth.html#obtaining-an-authorization-grant)
            *   [Getting an access token](https://docs.pretix.eu/dev/api/oauth.html#getting-an-access-token)
            *   [Using the API with an access token](https://docs.pretix.eu/dev/api/oauth.html#using-the-api-with-an-access-token)
            *   [Refreshing an access token](https://docs.pretix.eu/dev/api/oauth.html#refreshing-an-access-token)
            *   [Revoking a token](https://docs.pretix.eu/dev/api/oauth.html#revoking-a-token)
            *   [Fetching the user profile](https://docs.pretix.eu/dev/api/oauth.html#fetching-the-user-profile)

        *   [Device authentication](https://docs.pretix.eu/dev/api/deviceauth.html)
            *   [Initializing a new device](https://docs.pretix.eu/dev/api/deviceauth.html#initializing-a-new-device)
            *   [Performing API requests](https://docs.pretix.eu/dev/api/deviceauth.html#performing-api-requests)
            *   [Updating the software version](https://docs.pretix.eu/dev/api/deviceauth.html#updating-the-software-version)
            *   [Device Information](https://docs.pretix.eu/dev/api/deviceauth.html#device-information)
            *   [Creating a new API key](https://docs.pretix.eu/dev/api/deviceauth.html#creating-a-new-api-key)
            *   [Removing a device](https://docs.pretix.eu/dev/api/deviceauth.html#removing-a-device)
            *   [Permissions & security profiles](https://docs.pretix.eu/dev/api/deviceauth.html#permissions-security-profiles)
            *   [Event selection](https://docs.pretix.eu/dev/api/deviceauth.html#event-selection)

    *   [Resources and endpoints](https://docs.pretix.eu/dev/api/resources/index.html)
        *   [Organizers](https://docs.pretix.eu/dev/api/resources/organizers.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/organizers.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/organizers.html#endpoints)
            *   [Organizer settings](https://docs.pretix.eu/dev/api/resources/organizers.html#organizer-settings)

        *   [Events](https://docs.pretix.eu/dev/api/resources/events.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/events.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/events.html#endpoints)
            *   [Event settings](https://docs.pretix.eu/dev/api/resources/events.html#event-settings)

        *   [Event series dates / Sub-events](https://docs.pretix.eu/dev/api/resources/subevents.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/subevents.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/subevents.html#endpoints)

        *   [Tax rules](https://docs.pretix.eu/dev/api/resources/taxrules.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/taxrules.html#resource-description)
            *   [Tax codes](https://docs.pretix.eu/dev/api/resources/taxrules.html#tax-codes)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/taxrules.html#endpoints)

        *   [Item categories](https://docs.pretix.eu/dev/api/resources/categories.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/categories.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/categories.html#endpoints)

        *   [Items](https://docs.pretix.eu/dev/api/resources/items.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/items.html#resource-description)
            *   [Notes](https://docs.pretix.eu/dev/api/resources/items.html#notes)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/items.html#endpoints)

        *   [Item variations](https://docs.pretix.eu/dev/api/resources/item_variations.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/item_variations.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/item_variations.html#endpoints)

        *   [Item bundles](https://docs.pretix.eu/dev/api/resources/item_bundles.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/item_bundles.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/item_bundles.html#endpoints)

        *   [Item add-ons](https://docs.pretix.eu/dev/api/resources/item_add-ons.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/item_add-ons.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/item_add-ons.html#endpoints)

        *   [Item Meta Properties](https://docs.pretix.eu/dev/api/resources/item_meta_properties.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/item_meta_properties.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/item_meta_properties.html#endpoints)

        *   [Item program times](https://docs.pretix.eu/dev/api/resources/item_program_times.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/item_program_times.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/item_program_times.html#endpoints)

        *   [Questions](https://docs.pretix.eu/dev/api/resources/questions.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/questions.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/questions.html#endpoints)

        *   [Question options](https://docs.pretix.eu/dev/api/resources/question_options.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/question_options.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/question_options.html#endpoints)

        *   [Quotas](https://docs.pretix.eu/dev/api/resources/quotas.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/quotas.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/quotas.html#endpoints)

        *   [Seats](https://docs.pretix.eu/dev/api/resources/seats.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/seats.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/seats.html#endpoints)

        *   [Orders](https://docs.pretix.eu/dev/api/resources/orders.html)
            *   [Order resource](https://docs.pretix.eu/dev/api/resources/orders.html#order-resource)
            *   [Order position resource](https://docs.pretix.eu/dev/api/resources/orders.html#order-position-resource)
            *   [Order payment resource](https://docs.pretix.eu/dev/api/resources/orders.html#order-payment-resource)
            *   [Order refund resource](https://docs.pretix.eu/dev/api/resources/orders.html#order-refund-resource)
            *   [List of all orders](https://docs.pretix.eu/dev/api/resources/orders.html#list-of-all-orders)
            *   [Fetching individual orders](https://docs.pretix.eu/dev/api/resources/orders.html#fetching-individual-orders)
            *   [Order ticket download](https://docs.pretix.eu/dev/api/resources/orders.html#order-ticket-download)
            *   [Updating order fields](https://docs.pretix.eu/dev/api/resources/orders.html#updating-order-fields)
            *   [Generating new secrets](https://docs.pretix.eu/dev/api/resources/orders.html#generating-new-secrets)
            *   [Deleting orders](https://docs.pretix.eu/dev/api/resources/orders.html#deleting-orders)
            *   [Creating orders](https://docs.pretix.eu/dev/api/resources/orders.html#creating-orders)
            *   [Order state operations](https://docs.pretix.eu/dev/api/resources/orders.html#order-state-operations)
            *   [Generating invoices](https://docs.pretix.eu/dev/api/resources/orders.html#generating-invoices)
            *   [Sending e-mails](https://docs.pretix.eu/dev/api/resources/orders.html#sending-e-mails)
            *   [List of all order positions](https://docs.pretix.eu/dev/api/resources/orders.html#list-of-all-order-positions)
            *   [Fetching individual positions](https://docs.pretix.eu/dev/api/resources/orders.html#fetching-individual-positions)
            *   [Order position ticket download](https://docs.pretix.eu/dev/api/resources/orders.html#order-position-ticket-download)
            *   [Manipulating individual positions](https://docs.pretix.eu/dev/api/resources/orders.html#manipulating-individual-positions)
            *   [Changing order contents](https://docs.pretix.eu/dev/api/resources/orders.html#changing-order-contents)
            *   [Order payment endpoints](https://docs.pretix.eu/dev/api/resources/orders.html#order-payment-endpoints)
            *   [Order refund endpoints](https://docs.pretix.eu/dev/api/resources/orders.html#order-refund-endpoints)
            *   [Revoked ticket secrets](https://docs.pretix.eu/dev/api/resources/orders.html#revoked-ticket-secrets)
            *   [Blocked ticket secrets](https://docs.pretix.eu/dev/api/resources/orders.html#blocked-ticket-secrets)

        *   [Invoices](https://docs.pretix.eu/dev/api/resources/invoices.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/invoices.html#resource-description)
            *   [Transmission types](https://docs.pretix.eu/dev/api/resources/invoices.html#transmission-types)
            *   [List of all invoices](https://docs.pretix.eu/dev/api/resources/invoices.html#list-of-all-invoices)
            *   [Fetching individual invoices](https://docs.pretix.eu/dev/api/resources/invoices.html#fetching-individual-invoices)
            *   [Modifying invoices](https://docs.pretix.eu/dev/api/resources/invoices.html#modifying-invoices)
            *   [Transmitting invoices](https://docs.pretix.eu/dev/api/resources/invoices.html#transmitting-invoices)

        *   [Transactions](https://docs.pretix.eu/dev/api/resources/transactions.html)
            *   [Our financial model](https://docs.pretix.eu/dev/api/resources/transactions.html#our-financial-model)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/transactions.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/transactions.html#endpoints)

        *   [Vouchers](https://docs.pretix.eu/dev/api/resources/vouchers.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/vouchers.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/vouchers.html#endpoints)

        *   [Discounts](https://docs.pretix.eu/dev/api/resources/discounts.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/discounts.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/discounts.html#endpoints)

        *   [Check-in](https://docs.pretix.eu/dev/api/resources/checkin.html)
            *   [Checking a ticket in](https://docs.pretix.eu/dev/api/resources/checkin.html#checking-a-ticket-in)
            *   [Performing a ticket search](https://docs.pretix.eu/dev/api/resources/checkin.html#performing-a-ticket-search)
            *   [Annulment of a check-in](https://docs.pretix.eu/dev/api/resources/checkin.html#annulment-of-a-check-in)
            *   [Check-in history](https://docs.pretix.eu/dev/api/resources/checkin.html#check-in-history)

        *   [Check-in lists](https://docs.pretix.eu/dev/api/resources/checkinlists.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/checkinlists.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/checkinlists.html#endpoints)
            *   [Order position endpoints](https://docs.pretix.eu/dev/api/resources/checkinlists.html#order-position-endpoints)

        *   [Waiting list entries](https://docs.pretix.eu/dev/api/resources/waitinglist.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/waitinglist.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/waitinglist.html#endpoints)

        *   [Customers](https://docs.pretix.eu/dev/api/resources/customers.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/customers.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/customers.html#endpoints)

        *   [Sales channels](https://docs.pretix.eu/dev/api/resources/saleschannels.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/saleschannels.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/saleschannels.html#endpoints)

        *   [Membership types](https://docs.pretix.eu/dev/api/resources/membershiptypes.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/membershiptypes.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/membershiptypes.html#endpoints)

        *   [Memberships](https://docs.pretix.eu/dev/api/resources/memberships.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/memberships.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/memberships.html#endpoints)

        *   [Gift cards](https://docs.pretix.eu/dev/api/resources/giftcards.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/giftcards.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/giftcards.html#endpoints)

        *   [Reusable media](https://docs.pretix.eu/dev/api/resources/reusablemedia.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/reusablemedia.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/reusablemedia.html#endpoints)

        *   [Cart positions](https://docs.pretix.eu/dev/api/resources/carts.html)
            *   [Cart position resource](https://docs.pretix.eu/dev/api/resources/carts.html#cart-position-resource)
            *   [Cart position endpoints](https://docs.pretix.eu/dev/api/resources/carts.html#cart-position-endpoints)

        *   [Teams](https://docs.pretix.eu/dev/api/resources/teams.html)
            *   [Team resource](https://docs.pretix.eu/dev/api/resources/teams.html#team-resource)
            *   [Team member resource](https://docs.pretix.eu/dev/api/resources/teams.html#team-member-resource)
            *   [Team invite resource](https://docs.pretix.eu/dev/api/resources/teams.html#team-invite-resource)
            *   [Team API token resource](https://docs.pretix.eu/dev/api/resources/teams.html#team-api-token-resource)
            *   [Team endpoints](https://docs.pretix.eu/dev/api/resources/teams.html#team-endpoints)
            *   [Team member endpoints](https://docs.pretix.eu/dev/api/resources/teams.html#team-member-endpoints)
            *   [Team invite endpoints](https://docs.pretix.eu/dev/api/resources/teams.html#team-invite-endpoints)
            *   [Team API token endpoints](https://docs.pretix.eu/dev/api/resources/teams.html#team-api-token-endpoints)

        *   [Devices](https://docs.pretix.eu/dev/api/resources/devices.html)
            *   [Device resource](https://docs.pretix.eu/dev/api/resources/devices.html#device-resource)
            *   [Device endpoints](https://docs.pretix.eu/dev/api/resources/devices.html#device-endpoints)

        *   [Webhooks](https://docs.pretix.eu/dev/api/resources/webhooks.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/webhooks.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/webhooks.html#endpoints)

        *   [Seating plans](https://docs.pretix.eu/dev/api/resources/seatingplans.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/seatingplans.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/seatingplans.html#endpoints)

        *   [Data exporters](https://docs.pretix.eu/dev/api/resources/exporters.html)
            *   [Listing available exporters](https://docs.pretix.eu/dev/api/resources/exporters.html#listing-available-exporters)
            *   [Running an export](https://docs.pretix.eu/dev/api/resources/exporters.html#running-an-export)
            *   [Downloading the result](https://docs.pretix.eu/dev/api/resources/exporters.html#downloading-the-result)

        *   [Scheduled data exports](https://docs.pretix.eu/dev/api/resources/scheduled_exports.html)
            *   [Scheduled export resource](https://docs.pretix.eu/dev/api/resources/scheduled_exports.html#scheduled-export-resource)
            *   [Special notes on permissions](https://docs.pretix.eu/dev/api/resources/scheduled_exports.html#special-notes-on-permissions)
            *   [Endpoints for event exports](https://docs.pretix.eu/dev/api/resources/scheduled_exports.html#endpoints-for-event-exports)
            *   [Endpoints for organizer exports](https://docs.pretix.eu/dev/api/resources/scheduled_exports.html#endpoints-for-organizer-exports)

        *   [Data shredders](https://docs.pretix.eu/dev/api/resources/shredders.html)
            *   [Listing available shredders](https://docs.pretix.eu/dev/api/resources/shredders.html#listing-available-shredders)
            *   [Running an export](https://docs.pretix.eu/dev/api/resources/shredders.html#running-an-export)
            *   [Downloading the result](https://docs.pretix.eu/dev/api/resources/shredders.html#downloading-the-result)
            *   [Shredding the data](https://docs.pretix.eu/dev/api/resources/shredders.html#shredding-the-data)
            *   [Checking the result](https://docs.pretix.eu/dev/api/resources/shredders.html#checking-the-result)

        *   [Bank transfer](https://docs.pretix.eu/dev/api/resources/banktransfer.html)
            *   [Bank import job resource](https://docs.pretix.eu/dev/api/resources/banktransfer.html#bank-import-job-resource)

        *   [PDF ticket output](https://docs.pretix.eu/dev/api/resources/ticketoutputpdf.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/ticketoutputpdf.html#resource-description)
            *   [Layout endpoints](https://docs.pretix.eu/dev/api/resources/ticketoutputpdf.html#layout-endpoints)
            *   [Ticket rendering endpoint](https://docs.pretix.eu/dev/api/resources/ticketoutputpdf.html#ticket-rendering-endpoint)

        *   [Badges](https://docs.pretix.eu/dev/api/resources/badges.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/badges.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/badges.html#endpoints)

        *   [Scheduled email rules](https://docs.pretix.eu/dev/api/resources/sendmail_rules.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/sendmail_rules.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/sendmail_rules.html#endpoints)

        *   [Auto check-in rules](https://docs.pretix.eu/dev/api/resources/auto_checkin_rules.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/auto_checkin_rules.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/auto_checkin_rules.html#endpoints)

        *   [Campaigns](https://docs.pretix.eu/dev/api/resources/campaigns.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/campaigns.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/campaigns.html#endpoints)

        *   [Certificates of attendance](https://docs.pretix.eu/dev/api/resources/certificates.html)
            *   [Certificate download](https://docs.pretix.eu/dev/api/resources/certificates.html#certificate-download)

        *   [Digital content](https://docs.pretix.eu/dev/api/resources/digital.html)
            *   [URL interpolation and JWT authentication](https://docs.pretix.eu/dev/api/resources/digital.html#url-interpolation-and-jwt-authentication)
            *   [API Resource description](https://docs.pretix.eu/dev/api/resources/digital.html#api-resource-description)
            *   [API Endpoints](https://docs.pretix.eu/dev/api/resources/digital.html#api-endpoints)

        *   [Exhibitors](https://docs.pretix.eu/dev/api/resources/exhibitors.html)
            *   [REST API](https://docs.pretix.eu/dev/api/resources/exhibitors.html#rest-api)
            *   [App API](https://docs.pretix.eu/dev/api/resources/exhibitors.html#app-api)

        *   [Secrets Import](https://docs.pretix.eu/dev/api/resources/imported_secrets.html)
            *   [API Resource description](https://docs.pretix.eu/dev/api/resources/imported_secrets.html#api-resource-description)
            *   [API Endpoints](https://docs.pretix.eu/dev/api/resources/imported_secrets.html#api-endpoints)

        *   [Offline sales](https://docs.pretix.eu/dev/api/resources/offlinesales.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/offlinesales.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/offlinesales.html#endpoints)

        *   [Shipping](https://docs.pretix.eu/dev/api/resources/shipping.html)
            *   [Shipping address resource](https://docs.pretix.eu/dev/api/resources/shipping.html#shipping-address-resource)
            *   [Shipping status resource](https://docs.pretix.eu/dev/api/resources/shipping.html#shipping-status-resource)
            *   [Print job resource](https://docs.pretix.eu/dev/api/resources/shipping.html#print-job-resource)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/shipping.html#endpoints)

        *   [pretix Hosted billing invoices](https://docs.pretix.eu/dev/api/resources/billing_invoices.html)
            *   [Resource description](https://docs.pretix.eu/dev/api/resources/billing_invoices.html#resource-description)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/billing_invoices.html#endpoints)

        *   [pretix Hosted reseller API](https://docs.pretix.eu/dev/api/resources/billing_var.html)
            *   [Reseller account resource](https://docs.pretix.eu/dev/api/resources/billing_var.html#reseller-account-resource)
            *   [Endpoints](https://docs.pretix.eu/dev/api/resources/billing_var.html#endpoints)

    *   [Rate limiting](https://docs.pretix.eu/dev/api/ratelimit.html)
    *   [Webhooks](https://docs.pretix.eu/dev/api/webhooks.html)
        *   [Configuring webhooks](https://docs.pretix.eu/dev/api/webhooks.html#configuring-webhooks)
        *   [Receiving webhooks](https://docs.pretix.eu/dev/api/webhooks.html#receiving-webhooks)
        *   [Responding to a webhook](https://docs.pretix.eu/dev/api/webhooks.html#responding-to-a-webhook)
        *   [Debugging webhooks](https://docs.pretix.eu/dev/api/webhooks.html#debugging-webhooks)

    *   [API Usage Guides](https://docs.pretix.eu/dev/api/guides/index.html)
        *   [Understanding the life cycle of orders](https://docs.pretix.eu/dev/api/guides/order_lifecycle.html#)
            *   [Order states](https://docs.pretix.eu/dev/api/guides/order_lifecycle.html#order-states)
            *   [Object types](https://docs.pretix.eu/dev/api/guides/order_lifecycle.html#object-types)

        *   [Creating an external checkout process](https://docs.pretix.eu/dev/api/guides/custom_checkout.html)
            *   [Creating orders](https://docs.pretix.eu/dev/api/guides/custom_checkout.html#creating-orders)
            *   [Handling payments yourself](https://docs.pretix.eu/dev/api/guides/custom_checkout.html#handling-payments-yourself)
            *   [Using pretix payment providers](https://docs.pretix.eu/dev/api/guides/custom_checkout.html#using-pretix-payment-providers)
            *   [Optional: Cart reservations](https://docs.pretix.eu/dev/api/guides/custom_checkout.html#optional-cart-reservations)

*   [Plugin & core development](https://docs.pretix.eu/dev/development/index.html)
    *   [Concepts and Terminology](https://docs.pretix.eu/dev/development/concepts.html)
        *   [The components](https://docs.pretix.eu/dev/development/concepts.html#the-components)
        *   [Users and events](https://docs.pretix.eu/dev/development/concepts.html#users-and-events)
        *   [Items and variations](https://docs.pretix.eu/dev/development/concepts.html#items-and-variations)
        *   [Quotas](https://docs.pretix.eu/dev/development/concepts.html#quotas)
        *   [Vouchers](https://docs.pretix.eu/dev/development/concepts.html#vouchers)
        *   [Orders](https://docs.pretix.eu/dev/development/concepts.html#orders)

    *   [Development setup](https://docs.pretix.eu/dev/development/setup.html)
        *   [Obtain a copy of the source code](https://docs.pretix.eu/dev/development/setup.html#obtain-a-copy-of-the-source-code)
        *   [External Dependencies](https://docs.pretix.eu/dev/development/setup.html#external-dependencies)
        *   [Your local python environment](https://docs.pretix.eu/dev/development/setup.html#your-local-python-environment)
        *   [Working with the code](https://docs.pretix.eu/dev/development/setup.html#working-with-the-code)
            *   [Run the development server](https://docs.pretix.eu/dev/development/setup.html#run-the-development-server)
            *   [Run the widget development server](https://docs.pretix.eu/dev/development/setup.html#run-the-widget-development-server)
            *   [Code checks and unit tests](https://docs.pretix.eu/dev/development/setup.html#code-checks-and-unit-tests)
            *   [Working with mails](https://docs.pretix.eu/dev/development/setup.html#working-with-mails)
            *   [Working with periodic tasks](https://docs.pretix.eu/dev/development/setup.html#working-with-periodic-tasks)
            *   [Working with translations](https://docs.pretix.eu/dev/development/setup.html#working-with-translations)

        *   [Working with the documentation](https://docs.pretix.eu/dev/development/setup.html#working-with-the-documentation)
        *   [Working with frontend assets](https://docs.pretix.eu/dev/development/setup.html#working-with-frontend-assets)

    *   [Contributing to pretix](https://docs.pretix.eu/dev/development/contribution/index.html)
        *   [Contribution workflow](https://docs.pretix.eu/dev/development/contribution/general.html)
            *   [Discussion & Design](https://docs.pretix.eu/dev/development/contribution/general.html#discussion-design)
            *   [Development](https://docs.pretix.eu/dev/development/contribution/general.html#development)
            *   [Sending a patch](https://docs.pretix.eu/dev/development/contribution/general.html#sending-a-patch)

        *   [Coding style and quality](https://docs.pretix.eu/dev/development/contribution/style.html)
            *   [Code](https://docs.pretix.eu/dev/development/contribution/style.html#code)
            *   [Commits and Pull Requests](https://docs.pretix.eu/dev/development/contribution/style.html#commits-and-pull-requests)

        *   [AI-assisted contribution policy](https://docs.pretix.eu/dev/development/contribution/ai.html)
        *   [Code of Conduct](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html)
            *   [Our Pledge](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html#our-pledge)
            *   [Our Standards](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html#our-standards)
            *   [Our Responsibilities](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html#our-responsibilities)
            *   [Scope](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html#scope)
            *   [Enforcement](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html#enforcement)
            *   [Attribution](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html#attribution)

    *   [Implementation and Utilities](https://docs.pretix.eu/dev/development/implementation/index.html)
        *   [Data model](https://docs.pretix.eu/dev/development/implementation/models.html)
            *   [User model](https://docs.pretix.eu/dev/development/implementation/models.html#user-model)
            *   [Organizers and events](https://docs.pretix.eu/dev/development/implementation/models.html#organizers-and-events)
            *   [Items](https://docs.pretix.eu/dev/development/implementation/models.html#items)
            *   [Carts and Orders](https://docs.pretix.eu/dev/development/implementation/models.html#carts-and-orders)
            *   [Logging](https://docs.pretix.eu/dev/development/implementation/models.html#logging)
            *   [Invoicing](https://docs.pretix.eu/dev/development/implementation/models.html#invoicing)
            *   [Vouchers](https://docs.pretix.eu/dev/development/implementation/models.html#vouchers)

        *   [Working with URLs](https://docs.pretix.eu/dev/development/implementation/urlconfig.html)
            *   [URL routing](https://docs.pretix.eu/dev/development/implementation/urlconfig.html#url-routing)
            *   [URL reversal](https://docs.pretix.eu/dev/development/implementation/urlconfig.html#url-reversal)
            *   [Implementation details](https://docs.pretix.eu/dev/development/implementation/urlconfig.html#implementation-details)

        *   [Internationalization](https://docs.pretix.eu/dev/development/implementation/i18n.html)
            *   [Forms](https://docs.pretix.eu/dev/development/implementation/i18n.html#forms)
            *   [Useful utilities](https://docs.pretix.eu/dev/development/implementation/i18n.html#useful-utilities)

        *   [Settings storage](https://docs.pretix.eu/dev/development/implementation/settings.html)
            *   [`SettingsSandbox`](https://docs.pretix.eu/dev/development/implementation/settings.html#pretix.base.settings.SettingsSandbox)
            *   [Forms](https://docs.pretix.eu/dev/development/implementation/settings.html#forms)
            *   [Defaults in plugins](https://docs.pretix.eu/dev/development/implementation/settings.html#defaults-in-plugins)

        *   [Background tasks](https://docs.pretix.eu/dev/development/implementation/background.html)
            *   [Implementing a task](https://docs.pretix.eu/dev/development/implementation/background.html#implementing-a-task)
            *   [Tasks in the request-response flow](https://docs.pretix.eu/dev/development/implementation/background.html#tasks-in-the-request-response-flow)

        *   [Sending Email](https://docs.pretix.eu/dev/development/implementation/email.html)
            *   [`mail()`](https://docs.pretix.eu/dev/development/implementation/email.html#pretix.base.services.mail.mail)

        *   [Permissions](https://docs.pretix.eu/dev/development/implementation/permissions.html)
            *   [Requiring permissions for a view](https://docs.pretix.eu/dev/development/implementation/permissions.html#requiring-permissions-for-a-view)
            *   [Requiring permissions in the REST API](https://docs.pretix.eu/dev/development/implementation/permissions.html#requiring-permissions-in-the-rest-api)
            *   [Checking permission in code](https://docs.pretix.eu/dev/development/implementation/permissions.html#checking-permission-in-code)
            *   [Staff sessions](https://docs.pretix.eu/dev/development/implementation/permissions.html#staff-sessions)
            *   [Adding permissions](https://docs.pretix.eu/dev/development/implementation/permissions.html#adding-permissions)

        *   [Logging and notifications](https://docs.pretix.eu/dev/development/implementation/logging.html)
            *   [Logging changes](https://docs.pretix.eu/dev/development/implementation/logging.html#logging-changes)
            *   [Sending notifications](https://docs.pretix.eu/dev/development/implementation/logging.html#sending-notifications)
            *   [Logging technical information](https://docs.pretix.eu/dev/development/implementation/logging.html#logging-technical-information)

        *   [Resource locking](https://docs.pretix.eu/dev/development/implementation/locking.html)
        *   [Time machine mode](https://docs.pretix.eu/dev/development/implementation/timemachine.html)
            *   [`time_machine_now()`](https://docs.pretix.eu/dev/development/implementation/timemachine.html#pretix.base.timemachine.time_machine_now)
            *   [Background tasks](https://docs.pretix.eu/dev/development/implementation/timemachine.html#background-tasks)

    *   [Algorithms](https://docs.pretix.eu/dev/development/algorithms/index.html)
        *   [Pricing algorithms](https://docs.pretix.eu/dev/development/algorithms/pricing.html)
            *   [Computation of listed prices](https://docs.pretix.eu/dev/development/algorithms/pricing.html#computation-of-listed-prices)
            *   [Guarantees on listed prices](https://docs.pretix.eu/dev/development/algorithms/pricing.html#guarantees-on-listed-prices)
            *   [Computation of cart prices](https://docs.pretix.eu/dev/development/algorithms/pricing.html#computation-of-cart-prices)
            *   [Discounts](https://docs.pretix.eu/dev/development/algorithms/pricing.html#discounts)
            *   [Flowchart](https://docs.pretix.eu/dev/development/algorithms/pricing.html#flowchart)
            *   [Rounding of taxes](https://docs.pretix.eu/dev/development/algorithms/pricing.html#rounding-of-taxes)

        *   [Check-in algorithms](https://docs.pretix.eu/dev/development/algorithms/checkin.html)
            *   [Server-side](https://docs.pretix.eu/dev/development/algorithms/checkin.html#server-side)
            *   [Client-side](https://docs.pretix.eu/dev/development/algorithms/checkin.html#client-side)

        *   [Ticket layout](https://docs.pretix.eu/dev/development/algorithms/layouts.html)

    *   [Plugin development](https://docs.pretix.eu/dev/development/api/index.html)
        *   [Creating a plugin](https://docs.pretix.eu/dev/development/api/plugins.html)
            *   [Plugin metadata](https://docs.pretix.eu/dev/development/api/plugins.html#plugin-metadata)
            *   [Plugin registration](https://docs.pretix.eu/dev/development/api/plugins.html#plugin-registration)
            *   [Signals](https://docs.pretix.eu/dev/development/api/plugins.html#signals)
            *   [Registries](https://docs.pretix.eu/dev/development/api/plugins.html#registries)
            *   [Views](https://docs.pretix.eu/dev/development/api/plugins.html#views)

        *   [Writing an exporter plugin](https://docs.pretix.eu/dev/development/api/exporter.html)
            *   [Exporter registration](https://docs.pretix.eu/dev/development/api/exporter.html#exporter-registration)
            *   [The exporter class](https://docs.pretix.eu/dev/development/api/exporter.html#the-exporter-class)

        *   [Writing a ticket output plugin](https://docs.pretix.eu/dev/development/api/ticketoutput.html)
            *   [Output registration](https://docs.pretix.eu/dev/development/api/ticketoutput.html#output-registration)
            *   [The output class](https://docs.pretix.eu/dev/development/api/ticketoutput.html#the-output-class)

        *   [Writing a payment provider plugin](https://docs.pretix.eu/dev/development/api/payment.html)
            *   [Provider registration](https://docs.pretix.eu/dev/development/api/payment.html#provider-registration)
            *   [The provider class](https://docs.pretix.eu/dev/development/api/payment.html#the-provider-class)
            *   [Additional views](https://docs.pretix.eu/dev/development/api/payment.html#additional-views)

        *   [Writing an HTML e-mail renderer plugin](https://docs.pretix.eu/dev/development/api/email.html)
            *   [Output registration](https://docs.pretix.eu/dev/development/api/email.html#output-registration)
            *   [The renderer class](https://docs.pretix.eu/dev/development/api/email.html#the-renderer-class)
            *   [Helper class for template-base renderers](https://docs.pretix.eu/dev/development/api/email.html#helper-class-for-template-base-renderers)

        *   [Writing a template placeholder plugin](https://docs.pretix.eu/dev/development/api/placeholder.html)
            *   [Placeholder registration](https://docs.pretix.eu/dev/development/api/placeholder.html#placeholder-registration)
            *   [Context mechanism](https://docs.pretix.eu/dev/development/api/placeholder.html#context-mechanism)
            *   [The placeholder class](https://docs.pretix.eu/dev/development/api/placeholder.html#the-placeholder-class)
            *   [Helper class for simple placeholders](https://docs.pretix.eu/dev/development/api/placeholder.html#helper-class-for-simple-placeholders)
            *   [Signals](https://docs.pretix.eu/dev/development/api/placeholder.html#signals)

        *   [Writing an invoice renderer plugin](https://docs.pretix.eu/dev/development/api/invoice.html)
            *   [Output registration](https://docs.pretix.eu/dev/development/api/invoice.html#output-registration)
            *   [The renderer class](https://docs.pretix.eu/dev/development/api/invoice.html#the-renderer-class)
            *   [Helper class for reportlab-base renderers](https://docs.pretix.eu/dev/development/api/invoice.html#helper-class-for-reportlab-base-renderers)

        *   [Writing an invoice transmission plugin](https://docs.pretix.eu/dev/development/api/invoicetransmission.html)
            *   [Output registration](https://docs.pretix.eu/dev/development/api/invoicetransmission.html#output-registration)
            *   [The provider class](https://docs.pretix.eu/dev/development/api/invoicetransmission.html#the-provider-class)

        *   [Writing a data shredder](https://docs.pretix.eu/dev/development/api/shredder.html)
            *   [Shredder registration](https://docs.pretix.eu/dev/development/api/shredder.html#shredder-registration)
            *   [The shredder class](https://docs.pretix.eu/dev/development/api/shredder.html#the-shredder-class)
            *   [Example](https://docs.pretix.eu/dev/development/api/shredder.html#example)

        *   [Extending the import process](https://docs.pretix.eu/dev/development/api/import.html)
            *   [Import process](https://docs.pretix.eu/dev/development/api/import.html#import-process)
            *   [Column registration](https://docs.pretix.eu/dev/development/api/import.html#column-registration)
            *   [The column class API](https://docs.pretix.eu/dev/development/api/import.html#the-column-class-api)
            *   [Example](https://docs.pretix.eu/dev/development/api/import.html#example)

        *   [Creating custom views](https://docs.pretix.eu/dev/development/api/customview.html)
            *   [Control panel views](https://docs.pretix.eu/dev/development/api/customview.html#control-panel-views)
            *   [Event settings view](https://docs.pretix.eu/dev/development/api/customview.html#event-settings-view)
            *   [Frontend views](https://docs.pretix.eu/dev/development/api/customview.html#frontend-views)
            *   [REST API viewsets](https://docs.pretix.eu/dev/development/api/customview.html#rest-api-viewsets)

        *   [Handling cookie consent](https://docs.pretix.eu/dev/development/api/cookieconsent.html)
            *   [Server-side integration](https://docs.pretix.eu/dev/development/api/cookieconsent.html#server-side-integration)
            *   [JavaScript-side integration](https://docs.pretix.eu/dev/development/api/cookieconsent.html#javascript-side-integration)

        *   [Pluggable authentication backends](https://docs.pretix.eu/dev/development/api/auth.html)
            *   [`UserManager`](https://docs.pretix.eu/dev/development/api/auth.html#pretix.base.models.auth.UserManager)
            *   [The backend interface](https://docs.pretix.eu/dev/development/api/auth.html#the-backend-interface)
            *   [Logging users in](https://docs.pretix.eu/dev/development/api/auth.html#logging-users-in)

        *   [Data sync providers](https://docs.pretix.eu/dev/development/api/datasync.html)
            *   [Property mappings](https://docs.pretix.eu/dev/development/api/datasync.html#property-mappings)
            *   [Implementation examples](https://docs.pretix.eu/dev/development/api/datasync.html#implementation-examples)
            *   [The OutboundSyncProvider base class](https://docs.pretix.eu/dev/development/api/datasync.html#the-outboundsyncprovider-base-class)
            *   [Property mapping format](https://docs.pretix.eu/dev/development/api/datasync.html#property-mapping-format)
            *   [Translating mappings on Event copy](https://docs.pretix.eu/dev/development/api/datasync.html#translating-mappings-on-event-copy)

        *   [General APIs](https://docs.pretix.eu/dev/development/api/general.html)
            *   [Core](https://docs.pretix.eu/dev/development/api/general.html#module-pretix.base.signals)
            *   [Frontend](https://docs.pretix.eu/dev/development/api/general.html#module-pretix.presale.signals)
            *   [Backend](https://docs.pretix.eu/dev/development/api/general.html#module-pretix.control.signals)
            *   [API](https://docs.pretix.eu/dev/development/api/general.html#api)

        *   [Plugin quality checklist](https://docs.pretix.eu/dev/development/api/quality.html)
            *   [A. Meta](https://docs.pretix.eu/dev/development/api/quality.html#a-meta)
            *   [B. Isolation](https://docs.pretix.eu/dev/development/api/quality.html#b-isolation)
            *   [C. Security](https://docs.pretix.eu/dev/development/api/quality.html#c-security)
            *   [D. Privacy](https://docs.pretix.eu/dev/development/api/quality.html#d-privacy)
            *   [E. Internationalization](https://docs.pretix.eu/dev/development/api/quality.html#e-internationalization)
            *   [F. Functionality](https://docs.pretix.eu/dev/development/api/quality.html#f-functionality)
            *   [G. Code quality](https://docs.pretix.eu/dev/development/api/quality.html#g-code-quality)
            *   [H. Specific to pretix.eu](https://docs.pretix.eu/dev/development/api/quality.html#h-specific-to-pretix-eu)

    *   [Directory structure](https://docs.pretix.eu/dev/development/structure.html)
    *   [Translating pretix](https://docs.pretix.eu/dev/development/translation/index.html)
        *   [Official and inofficial languages](https://docs.pretix.eu/dev/development/translation/index.html#official-and-inofficial-languages)
        *   [Using our translation platform](https://docs.pretix.eu/dev/development/translation/index.html#using-our-translation-platform)

    *   [NFC media](https://docs.pretix.eu/dev/development/nfc/index.html)
        *   [UID-based](https://docs.pretix.eu/dev/development/nfc/uid.html)
        *   [Mifare Ultralight AES](https://docs.pretix.eu/dev/development/nfc/mf0aes.html)
            *   [Random UIDs](https://docs.pretix.eu/dev/development/nfc/mf0aes.html#random-uids)
            *   [Key management](https://docs.pretix.eu/dev/development/nfc/mf0aes.html#key-management)
            *   [Encoding a chip](https://docs.pretix.eu/dev/development/nfc/mf0aes.html#encoding-a-chip)
            *   [Usage](https://docs.pretix.eu/dev/development/nfc/mf0aes.html#usage)

 2026.6 

[pretix](https://docs.pretix.eu/dev/index.html)

*   [Docs](https://docs.pretix.eu/dev/index.html) »
*   [REST API](https://docs.pretix.eu/dev/api/index.html) »
*   [API Usage Guides](https://docs.pretix.eu/dev/api/guides/index.html) »
*   Understanding the life cycle of orders
*   [View page source](https://docs.pretix.eu/dev/_sources/api/guides/order_lifecycle.rst.txt)

* * *

# Understanding the life cycle of orders[¶](https://docs.pretix.eu/dev/api/guides/order_lifecycle.html#understanding-the-life-cycle-of-orders "Link to this heading")

When integrating pretix with other systems, it is important that you understand how orders and related objects such as order positions, fees, payments, refunds, and invoices work together, in order to react to their changes properly and map them to processes in your system.

## Order states[¶](https://docs.pretix.eu/dev/api/guides/order_lifecycle.html#order-states "Link to this heading")

Generally, an order can be in six states. For compatibility reasons, the `status` field only allows four values and the two remaining states are modeled through the `require_approval` field and the number of positions within an order. The states and their allowed changes are shown in the following graph:

![Image 4: ../../_images/order_states.png](https://docs.pretix.eu/dev/_images/order_states.png)
## Object types[¶](https://docs.pretix.eu/dev/api/guides/order_lifecycle.html#object-types "Link to this heading")

Order
One order represents one purchase. It’s the main object you interact with and bundles all the other objects together. Orders can change in many ways during their lifetime, but will never be deleted (unless `testmode` is set to `true`).

Order position
An order position represents one product contained in the order. Orders can usually have multiple positions. There might be a parent-child relation between order positions if one position is an add-on to another position. Order positions can change in many ways during their lifetime, and can also be removed or added to an order.

Order fees
A fee represents a charge that is not related to a product. Examples include shipping fees, service fees, and cancellation fees. Order fees can change in many ways during their lifetime, and can also be removed or added to an order.

Order payment
An order payment represents one payment attempt with a specific payment method and amount. An order can have multiple payments attached. Order payments have their own state diagram. Apart from their state and their meta information (e.g. used credit card, …) they usually don’t change. They may be added at any time, but will never be deleted.

Order refund
An order payment represents one refund attempt with a specific payment method and amount. An order can have multiple refunds attached. Order refunds have their own state diagram. Apart from their state and their meta information (e.g. used credit card, …) they usually don’t change. They may be added at any time, but will never be deleted.

Invoice
An invoice represents a legal document stating the contents of an order. While the backend technically allows to update an invoice in some situations, invoices are generally considered immutable. Once they are issued, they no longer change. If the order changes substantially (e.g. prices change), an invoice is canceled through creation of a new invoice with the opposite amount, plus the issuance of a new invoice.

Here’s an example of how they all play together:

![Image 5: ../../_images/order_objects.png](https://docs.pretix.eu/dev/_images/order_objects.png)

[Next](https://docs.pretix.eu/dev/api/guides/custom_checkout.html "Creating an external checkout process")[Previous](https://docs.pretix.eu/dev/api/guides/index.html "API Usage Guides")

* * *

© Copyright 2014-2026, rami.io GmbH.

Built with [Sphinx](http://sphinx-doc.org/) using a theme that is based on a [theme](https://github.com/snide/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).[Imprint](https://pretix.eu/about/en/imprint) · [Privacy](https://pretix.eu/about/en/privacy)
