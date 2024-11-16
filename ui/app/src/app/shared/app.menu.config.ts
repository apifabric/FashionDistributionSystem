import { MenuRootItem } from 'ontimize-web-ngx';

import { BrandCardComponent } from './Brand-card/Brand-card.component';

import { CampaignCardComponent } from './Campaign-card/Campaign-card.component';

import { CollectionCardComponent } from './Collection-card/Collection-card.component';

import { DesignCardComponent } from './Design-card/Design-card.component';

import { DesignerCardComponent } from './Designer-card/Designer-card.component';

import { LocationCardComponent } from './Location-card/Location-card.component';

import { ParticipationCardComponent } from './Participation-card/Participation-card.component';

import { SaleCardComponent } from './Sale-card/Sale-card.component';

import { StockCardComponent } from './Stock-card/Stock-card.component';

import { StoreCardComponent } from './Store-card/Store-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplyCardComponent } from './Supply-card/Supply-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Brand', name: 'BRAND', icon: 'view_list', route: '/main/Brand' }
    
        ,{ id: 'Campaign', name: 'CAMPAIGN', icon: 'view_list', route: '/main/Campaign' }
    
        ,{ id: 'Collection', name: 'COLLECTION', icon: 'view_list', route: '/main/Collection' }
    
        ,{ id: 'Design', name: 'DESIGN', icon: 'view_list', route: '/main/Design' }
    
        ,{ id: 'Designer', name: 'DESIGNER', icon: 'view_list', route: '/main/Designer' }
    
        ,{ id: 'Location', name: 'LOCATION', icon: 'view_list', route: '/main/Location' }
    
        ,{ id: 'Participation', name: 'PARTICIPATION', icon: 'view_list', route: '/main/Participation' }
    
        ,{ id: 'Sale', name: 'SALE', icon: 'view_list', route: '/main/Sale' }
    
        ,{ id: 'Stock', name: 'STOCK', icon: 'view_list', route: '/main/Stock' }
    
        ,{ id: 'Store', name: 'STORE', icon: 'view_list', route: '/main/Store' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'Supply', name: 'SUPPLY', icon: 'view_list', route: '/main/Supply' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    BrandCardComponent

    ,CampaignCardComponent

    ,CollectionCardComponent

    ,DesignCardComponent

    ,DesignerCardComponent

    ,LocationCardComponent

    ,ParticipationCardComponent

    ,SaleCardComponent

    ,StockCardComponent

    ,StoreCardComponent

    ,SupplierCardComponent

    ,SupplyCardComponent

];