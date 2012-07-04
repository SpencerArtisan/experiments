validate = (form) ->
  required_field_names = ['name','email']
  errors = []
  required_fields = ( form.elements[name] for name in required_field_names )
  (errors.push field.name if field.value == '') for field in required_fields
  report errors
  errors.length == 0

report = (errors) ->
    alert "The following fields have errors:\n\n-  " + errors.join("\n-  ") if errors.length > 0
