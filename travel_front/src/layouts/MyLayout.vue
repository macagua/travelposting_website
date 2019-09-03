<template>
  <q-layout view="hHh lpr fFf">
    <q-header class="transparent">
      <div class="absolute-top row no-wrap">
        <q-toolbar class="col-sm-2 desktop-only"> </q-toolbar>
        <q-toolbar class="col-sm-8 col-xs-12">
          <q-toolbar-title>
            <strong>Travel Posting</strong>
          </q-toolbar-title>
          <q-space />
          <q-btn flat dense round icon="menu" class="mobile-only">
            <q-menu content-class="bg-primary text-white">
              <q-list style="min-width: 300px;" class="text-uppercase">
                <q-item clickable>
                  <q-item-section> Inicio </q-item-section>
                </q-item>
                <q-item clickable>
                  <q-item-section> Testimonios </q-item-section>
                </q-item>
                <q-item clickable>
                  <q-item-section> Precio </q-item-section>
                </q-item>
                <q-item clickable>
                  <q-item-section> Empresa </q-item-section>
                </q-item>
                <q-item clickable>
                  <q-item-section>
                    <q-btn flat dense round icon="search" />
                  </q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <div class="desktop-only">
            <q-btn flat dense class="q-px-md text-weight-bold"> Inicio </q-btn>
            <q-btn flat dense class="q-px-md text-weight-bold"> Testimonios </q-btn>
            <q-btn flat dense class="q-px-md text-weight-bold"> Precio </q-btn>
            <q-btn flat dense class="q-px-md text-weight-bold"> Empresa </q-btn>
            <q-btn flat dense round icon="search" />
          </div>
        </q-toolbar>
        <q-toolbar class="col-sm-2 desktop-only"> </q-toolbar>
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="transparent">
      <q-toolbar class="absolute-bottom">
        <q-toolbar-title>
          Quasar app
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
export default {
  name: 'MyLayout',
  data () { }
}
</script>

<style> </style>
