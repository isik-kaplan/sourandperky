function api_urls(base) {
    return {
        entries: base + "/entries/",
        users: base + "/users/",
        titles: base + "/titles/",
        title_channels: base + "/title_channels/",
        events: base + "/events/",
        user_trophies: base + "/user_trophies/",
        notifications: base + "/notifications/",
        social_auth: {
            google: "/social_auth/google/"
        },
        auth: {
            rest_password_reset: base + "/auth/password/reset/",
            rest_password_reset_confirm: base + "/auth/password/reset/confirm/",
            rest_login: base + "/auth/login/",
            rest_logout: base + "/auth/logout/",
            rest_user_details: base + "/auth/user/",
            rest_password_change: base + "/auth/password/change/",
            rest_register: base + "/auth/registration/"
        },
        relations: {
            like_entry: base + "/relations/like_entry/",
            dislike_entry: base + "/relations/dislike_entry/",
            fav_entry: base + "/relations/fav_entry/",
            follow_user: base + "/relations/follow_user/",
            follow_title: base + "/relations/follow_title/"
        }
    }
}

const APIURLS = api_urls("/api");


const METHODS = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
    PATCH: 'PATCH',
    DELETE: 'DELETE',
};

function filter_undefined(obj) {
    return Object.fromEntries(
        Object.entries(
            obj
        ).filter(([, value]) => !(value === undefined))
    );
}


function build_url( url, parameters ) {
  const params = new URLSearchParams();
  for (const param of Object.entries(filter_undefined(parameters))) {
    params.set(...param);
  }
  return `${url}?${params.toString()}`;
}

function _interract(url, data, method, get_data, auth_token) {
    let fetch_data = {
        method: method,
        headers: {'Content-Type': 'application/json'},
        redirect: 'follow',
        referrer: 'no-referrer',
    };
    if (data !== undefined) {
        fetch_data.body = JSON.stringify(data)
    }
    if (auth_token !== undefined) {
        fetch_data.headers.Authorization = 'Token ' + auth_token
    }
    if (get_data) {
        url = build_url(url, get_data)
    }
    return fetch(url, fetch_data).then(response => response.json()).catch(err => console.log(err));
}

function interract(url, auth_token, method, is_obj, allowed_methods, default_error) {
    if (!allowed_methods.includes(method)) {
        return default_error
    } else if ((!auth_token) && ([METHODS.POST, METHODS.PATCH, METHODS.PUT].includes(method))) {
        return function () {
            throw new Error("Authentication is required to perform this action.")
        }
    } else if ((method === METHODS.GET) && !is_obj) { // list
        return function (get_data) {
            return _interract(url, undefined, method, get_data, auth_token)
        }
    } else if ((method === METHODS.GET) && is_obj) { // retrieve
        return function () {
            return _interract(url, undefined, method, undefined, auth_token)
        }
    } else if (method === METHODS.PUT) { // update
        console.log('UPDATE')
    } else if (method === METHODS.PATCH) { // update
        return function (data) {
            return _interract(url, data, method, undefined, auth_token)
        }
    } else if (method === METHODS.DELETE) { // delete
        return function () {
            return _interract(url, undefined, method, undefined, auth_token)
        }
    } else if (method === METHODS.POST) { // create
        return function (data) {
            return _interract(url, data, method, undefined, auth_token)
        }
    }
}

class CRUD_API_ENDPOINT {
    url = undefined;
    allowed_methods = [];

    default_error_function(method) {
        return function (place_holder) {
            throw new Error("This class type does not support method " + method)
        }
    }

    constructor(client) {
        this.client = client;
    }

    get_object_url(id) {
        return this.url + id
    }

    list(get_data) {
        return interract(
            this.url,
            this.client.token,
            METHODS.GET,
            false,
            this.allowed_methods,
            this.default_error_function(METHODS.GET)
        )(get_data)
    };

    create(data) {
        return interract(
            this.url,
            this.client.token,
            METHODS.POST,
            false,
            this.allowed_methods,
            this.default_error_function(METHODS.POST)
        )(data)
    };

    retrieve(id) {
        return interract(
            this.get_object_url(id),
            this.client.token,
            METHODS.GET,
            true,
            this.allowed_methods,
            this.default_error_function(METHODS.GET)
        )()
    };

    update(id, data) {
        return interract(
            this.get_object_url(id),
            this.client.token,
            METHODS.PATCH,
            true,
            this.allowed_methods,
            this.default_error_function(METHODS.PATCH)
        )(data)
    };

    destroy(id) {
        return interract(
            this.get_object_url(id),
            this.client.token,
            METHODS.DELETE,
            true,
            this.allowed_methods,
            this.default_error_function(METHODS.DELETE)
        )()
    };

    // aliases for crud methods
    get all() {
        return this.list
    }

    get new() {
        return this.create
    }

    get get() {
        return this.retrieve
    }

    get edit() {
        return this.update
    }

    get delete() {
        return this.destroy
    }

}

class Entries extends CRUD_API_ENDPOINT {
    url = APIURLS.entries;
    allowed_methods = [METHODS.GET, METHODS.POST, METHODS.PATCH, METHODS.DELETE];

    /*
    list(get_data){
        get_data = {
            page_size: integer -> item count in a page
            page: integer -> page number
            author: string -> a user id to filter with
            title: string -> a title id to filter with
            readability: boolean -> draft status
            search: string -> search for entries where entry.text contains search
            ordering: string options[points, timestamp] -> ordering of the entries
        }
    }
    */

    /*
    create(data){
        data = {
            *title: string -> a title id to filter with
            *text: string -> content of the entry
            *readability: boolean -> draft status
        }
    }
    */

    /*
    retrieve(id){
        *id = string -> entry id
    }
    */

    /*
    update(id, data){
        *id = string -> entry id
        *data = {
            title: string -> a title id to filter with
            text: string -> content of the entry
            readability: boolean -> draft status
        }
    }
    */

    /*
    delete(id){
        *id = string -> entry id
    }
    */
}

class Titles extends CRUD_API_ENDPOINT {
    url = APIURLS.titles;
    allowed_methods = [METHODS.GET, METHODS.POST];

    /* create(data){}
    text is required;
    data = {
        text: string -> the title
        channels: array[channel id] -> channels of the title
    }
    */
}

class Client {
    constructor(token) {
        this.token = token;
        this.entries = new Entries(this);
        this.titles = new Titles(this);
    }

    login(username, email, password) {
        let data = {};
        data.password = password;
        let err = "Either username or email is required for authentication.";
        if (email) {
            data.email = email
        } else if (username) {
            data.username = username
        } else {
            throw new Error(err)
        }
        fetch(
            APIURLS.auth.rest_login,
            {
                headers: {'Content-Type': 'application/json'},
                method: METHODS.POST,
                credentials: 'same-origin',
                body: JSON.stringify(data)
            }
        ).then(res => res.json()).then(resjson => this.token = resjson.key)
    }

    logout() {
        fetch(
            APIURLS.auth.rest_logout,
            {
                headers: {'Content-Type': 'application/json'},
                method: METHODS.POST,
                credentials: 'same-origin',
            }).then(res => res.json()).then(resjoson => this.token = undefined)
    }
}

let client = new Client();