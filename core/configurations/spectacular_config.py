SPECTACULAR_SETTINGS = {
    "TITLE": "Aibolit OpenAPI",
    "DESCRIPTION": "Описание нашего API в разработке...",
    'COMPONENT_SPLIT_REQUEST': True,
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
    "SERVE_AUTHENTICATION": ('rest_framework.authentication.SessionAuthentication',
                             'rest_framework.authentication.BasicAuthentication'),
    "PREPROCESSING_HOOKS": ("apps.openapi.preprocessors.get_urls_preprocessor",),
    "SWAGGER_UI_SETTINGS": {
        "docExpansion": "none",  # 'none' | 'list' | 'full'
    },
    "GENERATE_UNIQUE_PARAMETER_NAMES": True,

    # "ENUM_NAME_OVERRIDES": {
    #     "RatingsEnum": "apps.autoanswers.models.RatingChoices",
    #     "CountMonthsEnum": "api.billing.serializers.PeriodChoices",
    # },
    "SERVE_PERMISSIONS": ("rest_framework.permissions.AllowAny",)
}
