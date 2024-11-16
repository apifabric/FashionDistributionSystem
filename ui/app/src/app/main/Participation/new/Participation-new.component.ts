import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Participation-new',
  templateUrl: './Participation-new.component.html',
  styleUrls: ['./Participation-new.component.scss']
})
export class ParticipationNewComponent {
  @ViewChild("ParticipationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}