################################################################################
## Save and load
################################################################################

screen save():

    tag menu
    use menu_ui_file_slots(_("Guardar"))


screen load():

    tag menu
    use menu_ui_file_slots(_("Cargar"))


screen menu_ui_file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Página {}"),
        auto=_("Guardados automáticos"),
        quick=_("Guardados rápidos"),
    )

    use game_menu(title):

        vbox:
            style "menu_ui_file_slots_root"

            button:
                style "menu_ui_file_page_label"
                key_events True
                action page_name_value.Toggle()

                input:
                    style "menu_ui_file_page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style "menu_ui_file_slot_grid"

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        style "menu_ui_file_slot_button"
                        action FileAction(slot)
                        key "save_delete" action FileDelete(slot)

                        vbox:
                            style "menu_ui_file_slot_content"

                            fixed:
                                style "menu_ui_file_slot_preview"

                                add Solid("#dce8f4")
                                add FileScreenshot(slot):
                                    xysize (350, 190)

                                text "[slot]":
                                    style "menu_ui_file_slot_number"

                            text FileTime(
                                slot,
                                format=_("{#file_time}%d/%m/%Y · %H:%M"),
                                empty=_("Espacio vacío"),
                            ):
                                style "menu_ui_file_slot_time"

                            text FileSaveName(slot):
                                style "menu_ui_file_slot_name"

            hbox:
                style "menu_ui_file_page_navigation"

                textbutton _("‹"):
                    style "menu_ui_file_page_button"
                    action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("A"):
                        style "menu_ui_file_page_button"
                        action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("Q"):
                        style "menu_ui_file_page_button"
                        action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]":
                        style "menu_ui_file_page_button"
                        action FilePage(page)

                textbutton _("›"):
                    style "menu_ui_file_page_button"
                    action FilePageNext()

            if config.has_sync:

                textbutton (_("Subir guardados") if CurrentScreenName() == "save" else _("Descargar guardados")):
                    style "menu_ui_file_sync_button"
                    action (UploadSync() if CurrentScreenName() == "save" else DownloadSync())
