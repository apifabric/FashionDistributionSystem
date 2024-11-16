import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Brand', loadChildren: () => import('./Brand/Brand.module').then(m => m.BrandModule) },
    
        { path: 'Campaign', loadChildren: () => import('./Campaign/Campaign.module').then(m => m.CampaignModule) },
    
        { path: 'Collection', loadChildren: () => import('./Collection/Collection.module').then(m => m.CollectionModule) },
    
        { path: 'Design', loadChildren: () => import('./Design/Design.module').then(m => m.DesignModule) },
    
        { path: 'Designer', loadChildren: () => import('./Designer/Designer.module').then(m => m.DesignerModule) },
    
        { path: 'Location', loadChildren: () => import('./Location/Location.module').then(m => m.LocationModule) },
    
        { path: 'Participation', loadChildren: () => import('./Participation/Participation.module').then(m => m.ParticipationModule) },
    
        { path: 'Sale', loadChildren: () => import('./Sale/Sale.module').then(m => m.SaleModule) },
    
        { path: 'Stock', loadChildren: () => import('./Stock/Stock.module').then(m => m.StockModule) },
    
        { path: 'Store', loadChildren: () => import('./Store/Store.module').then(m => m.StoreModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
        { path: 'Supply', loadChildren: () => import('./Supply/Supply.module').then(m => m.SupplyModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }