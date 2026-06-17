{{- define "editor.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "editor.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "editor.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}

{{- define "editor.labels" -}}
app.kubernetes.io/name: {{ include "editor.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" }}
{{- end -}}

{{- define "editor.selectorLabels" -}}
app.kubernetes.io/name: {{ include "editor.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/* Name of the secret holding the git token (created here or referenced). */}}
{{- define "editor.gitSecretName" -}}
{{- if .Values.git.existingSecret -}}
{{- .Values.git.existingSecret -}}
{{- else -}}
{{- printf "%s-git" (include "editor.fullname" .) -}}
{{- end -}}
{{- end -}}
