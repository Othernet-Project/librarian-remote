<%namespace name="forms" file="/ui/forms.tpl"/>

${h.form('post', action=i18n_url('remote:setup'), tabindex=1)}
    % if message:
        ${forms.form_message(message)}
    % endif

    % if error:
        ${forms.form_errors([error])}
    % endif

    ${forms.field(form.key)}
    ${forms.field(form.hostname)}
    ${forms.field(form.host)}
    ${forms.field(form.port)}
    ${forms.field(form.enabled)}
    <p class="buttons">
        <button type="submit" class="primary">${_('Apply')}</button>
    </p>
</form>
