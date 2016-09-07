<%inherit file="/narrow_base.tpl"/>
<%namespace name="remote_form" file="_remote_form.tpl"/>

<%block name="title">
${_('Remote Access Setup')}
</%block>

<h2>${_('Remote Access Setup')}</h2>

${remote_form.body()}
