from contextlib import suppress


class ConditionalSerializerMixin:
    """@DynamicAttrs."""

    def get_fields(self):
        cls = self.__class__
        for name, serializer in self.Meta.relational_fields.items():
            setattr(cls, name, self.property_maker(name, serializer))

        fields = super().get_fields()
        conditional_fields = self.Meta.conditional_fields
        for field in conditional_fields:
            serializer = getattr(self, field)
            if serializer:
                fields[field] = serializer
        return fields

    @staticmethod
    def property_maker(name, serializer):
        def generic_property(_self):
            request = _self.context.get('request')
            GET = getattr(request, 'GET', {})
            if request and GET and GET.get('include_{}'.format(name)) == 'true':
                return serializer()

        generic_property.__name__ = name
        return property(generic_property)

    def bind(self, *a, **kw):
        with suppress(AssertionError):
            return super().bind(*a, **kw)
