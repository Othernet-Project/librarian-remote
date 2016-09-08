((window, $, templates) ->
  section = $ '#dashboard-remote'
  form = null
  errorMessage = templates.dashboardPluginError

  resizeSection = (form) ->
    form.parents('section').trigger('remax')

  submitForm = (form) ->
    method = form.attr 'method'
    url = form.attr 'action'
    data = form.serialize()
    res = $.ajax({url: url, data: data, type: method})
    res.done (result) ->
      # removes all event handlers automatically
      form.replaceWith result
      initPlugin()
    res.fail (xhr) ->
      form.prepend errorMessage
      resizeSection form

  onSubmit = (e) ->
    e.preventDefault()
    form = $ @
    submitForm form

  initPlugin = () ->
    # intercept form submission through save button
    form = section.find 'form'
    form.on 'submit', onSubmit
    # responses differ in height, so a resize of the section is triggered
    resizeSection form

  section.on 'dashboard-plugin-loaded', initPlugin

) this, this.jQuery, this.templates
